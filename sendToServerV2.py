import ftplib
import paramiko
import os
import configparser


"""
ok 
需要实现的功能：
编译；服务器进行备份；文件夹发送到服务器；重启tomcat；
之前还需要：合并代码；抽取svn记录；抽取需要增量部署的文件；
"""


def get_files_from_dir(dir_path):
    """
    目录转换成文件名list, 文件名是完整路径
    :param dir_path:
    :return:
    """
    file_list = []
    if os.path.isdir(dir_path):
        for parent, dirnames, filenames in os.walk(dir_path):
            for filename in filenames:
                # 完整路径
                file_path = os.path.join(parent, filename).replace('\\','/')
                # print('file_path:',file_path)
                file_list.append(file_path)
                pass
            pass
        pass
    return file_list


def send_file_sftp_pair(host, port, username, password, path_pair):
    """
    :param host:
    :param port:
    :param username:
    :param password:
    :param path_pair: 是一个list，每个元素也是一个list：本地路径和远程的路径。
    :return:
    """
    try:
        # trans = paramiko.Transport((host, port))
        trans = paramiko.Transport(host, port)
        trans.connect(username=username, password=password)
        # sftp = paramiko.SFTPClient.from_transport(trans)
        sftp = paramiko.sftp_client.SFTPClient.from_transport(trans)
        for single_pair in path_pair:
            # 无论上传还是下载，两个路径都必须到文件名，不能到目录
            sftp.put(localpath=single_pair[0], remotepath=single_pair[1])
            pass

        # sftp.get(remote_path, local_path)
        trans.close()
    except Exception as e:
        print(e)
        raise
    pass


def exec_command_ssh():
    '''
    ssh连接并执行命令
    :param ssh:
    :return:
    '''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('cd /app/apache-tomcat-7-sc')
    ssh.close()
    pass


def exec_command_ftp(host, port):
    '''
    ftp连接并执行命令
    '''
    conn = ftplib.FTP()
    conn.connect(host,port)
    conn.login(username,password)
    conn.set_pasv(False)
    conn.cwd('/app/apache-tomcat-7-sc')
    conn.close()
    pass


def get_class_paths(java_path, local_class_dir, remote_class_dir):
    start_idx = java_path.find('src/main/java')
    result = []
    if start_idx>-1:
        result.append(local_class_dir + '/' + ''.join(java_path[start_idx+1:]).replace('.java', '.class'))
        result.append(remote_class_dir + '/' + ''.join(java_path[start_idx+1:]).replace('.java', '.class'))
        pass

    start_idx = java_path.find('src/main/resources')
    result = []
    if start_idx > -1:
        result.append(local_class_dir + '/' + ''.join(java_path[start_idx + 1:]))
        result.append(remote_class_dir + '/' + ''.join(java_path[start_idx + 1:]))
        pass
    pass



def restart_server(host, port, username, password):
    """
    ssh连接服务器，执行shell命令
    :return:
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=username, password=password)
    restart_server_ssh(ssh)
    ssh.close()
    pass


def restart_server_ssh(ssh):
    stdin, stdout, stderr = ssh.exec_command("ps -ef|grep apache-tomcat-7-sc|awk '!/00:00:0./ {print $2}'")
    out = bytes.decode(stdout.read())
    out_li = out.split('\n')
    print('find process num',len(out_li))
    if len(out_li)>2:
        return
    for line in out_li:
        if line.strip()!='':
            print('line strip:',line)
            ssh.exec_command('kill -9 ' + line.strip())
        pass
    # stdin, stdout, stderr = ssh.exec_command('/app/apache-tomcat-7-sc/bin/startup.sh')
    stdin, stdout, stderr = ssh.exec_command('source /etc/profile;/app/apache-tomcat-7-sc/bin/startup.sh')
    print('stdout result:', bytes.decode(stdout.read()))
    print('stderr result:', bytes.decode(stderr.read()))
    # 先不关闭，由建立ssh的那个调用方负责关闭
    # ssh.close()
    pass


def convert_to_absolute_path(file_name, root_dir):
    '''
    在指定目录里搜索，将文件名转换成完整路径
    需要把路径分隔符（正反斜杠）转换成一致
    :return:
    '''
    absolute_file_name = ''
    if os.path.isdir(root_dir):
        for parent, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename==file_name:
                    # 完整路径
                    absolute_file_name = os.path.join(parent, filename)
                    # 可以返回了
                    return absolute_file_name.replace('\\','/')
                pass
            pass
        pass
    return absolute_file_name
    pass


def convert_to_path_pair(local_file_list, class_file_dir, remote_class_dir):
    '''
    把文件转换成一个list：[本地完整路径, 远程完整路径]
    :param local_file_list:
    :param class_file_dir:
    :param remote_class_dir:
    :return:
    '''
    path_pair = []
    for local_file in local_file_list:
        remote_file = local_file.replace(class_file_dir, remote_class_dir)
        path_pair.append([local_file, remote_file])
        pass
    return path_pair
    pass


def backup_remote_dir(remote_dir_path, ssh):
    # rm -rf WEB-INF2018*;curdate=`date +%Y%m%d%H%M%S`;echo $curdate;tar -zcf WEB-INF${curdate}.tar.gz WEB-INF
    check_dir_cmd = 'if [ ! -d "' + remote_dir_path +'" ]; then echo "n"; else echo "y"; fi;'
    # check_dir_cmd = 'if [ ! -d "' + remote_dir_path +'" ]; then exit 1; else exit 2; fi;'
    print('check_dir_cmd:', check_dir_cmd)
    stdin, stdout, stderr = ssh.exec_command(check_dir_cmd)
    std_our_str = bytes.decode(stdout.read()).strip()
    print('if stdout result:', std_our_str)
    print('if stderr result:', bytes.decode(stderr.read()))
    if std_our_str == 'n':
        print('go n')
        ssh.exec_command('mkdir -p ' + remote_dir_path)
        pass
    cmd = 'cd ' + remote_dir_path + ';cd ..; rm -rf WEB-INF20*;' + \
          'curdate=`date +%Y%m%d%H%M%S`;echo $curdate;tar -zcf WEB-INF${curdate}.tar.gz WEB-INF'
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print('stdout result:', bytes.decode(stdout.read()))
    print('stderr result:', bytes.decode(stderr.read()))
    pass


def send_dir_to_remote(local_dir_path, remote_dir_path, sftp, ssh, exclude_file_list=[]):
    """
    本地文件夹发送到远程目录。
    sftp只支持文件put，所以需要遍历目录。
    如果远程文件夹不存在是否需要先新建？
    :param local_dir_path:
    :param remote_dir_path:
    :param sftp:
    :return:
    """
    all_deploy_file_list = []
    # 不更新的文件
    # exclude_file_list = ['applicationContext.xml', 'applicationContext-shiro.xml', 'disconf.properties'
    #     , 'dubbo.properties', 'ehcache.xml', 'jdbc.properties', 'log4j.properties', 'mail.properties'
    #     , 'mybatis-config.xml', 'redis.properties', 'spring-mvc.xml']
    all_deploy_file_list.extend(get_files_from_dir(local_dir_path))
    final_file_list = []
    final_file_list.extend(all_deploy_file_list)
    # 如果一边循环一边删除，再加上内部的判断，会出现错乱
    for deploy_file in all_deploy_file_list:
        # print('deploy_file:', deploy_file)
        for exclude_file in exclude_file_list:
            if deploy_file.endswith(exclude_file):
                final_file_list.remove(deploy_file)
                break
        pass
    for file in final_file_list:
        remote_file_path = file.replace(local_dir_path, remote_dir_path)
        print('localpath:', file)
        print('local_dir_path:', local_dir_path)
        print('remote_dir_path:', remote_dir_path)
        print('remotepath:', remote_file_path)
        dir_path = remote_file_path.replace(os.path.basename(remote_file_path), '')
        stdin, stdout, stderr = ssh.exec_command('mkdir -p ' + dir_path)
        print('dir_path:', dir_path)
        print('mkdir stdout result:', bytes.decode(stdout.read()))
        print('mkdir stderr result:', bytes.decode(stderr.read()))
        sftp.put(localpath=file, remotepath=remote_file_path)
        pass
    pass


def check_dir_exists(path, seperator='/'):
    path.split(seperator)
    path = path.replace(os.path.basename(path),'')
    print('path:', path)
    pass


def deploy_all_files():
    '''
    全量部署，除了部分配置文件
    :return:
    '''
    # 编译
    # compile_rs = os.popen(r'compile.bat')
    # print('compile result:', compile_rs.read())
    # continue_flag = input('press "r" to return, press other keys to continue')
    # if 'r'==continue_flag:
    #     print('return !!!')
    #     return
    # print('continue !!!')
    config = configparser.ConfigParser()
    config.read('config-uncommit.ini')
    class_file_dir = config.get('sendToServer','class_file_dir')

    # remote_class_dir = config.get('sendToServer','remote_class_dir')
    remote_class_dir = r'/app/apache-tomcat-7-sc/webapps/SC/test-dir/classes'
    # get ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    host = '192.168.200.238'; port = 22; username = 'dev-sc'; password = 'hgHHJ?@!#'
    ssh.connect(hostname=host, port=port, username=username, password=password)
    # 备份服务器的文件
    backup_remote_dir(remote_class_dir, ssh)
    # 本地文件夹copy到远程，覆盖操作
    # 不更新的文件
    exclude_file_list = ['applicationContext.xml', 'applicationContext-shiro.xml', 'disconf.properties'
        , 'dubbo.properties', 'ehcache.xml', 'jdbc.properties', 'log4j.properties', 'mail.properties'
        , 'mybatis-config.xml', 'redis.properties', 'spring-mvc.xml']
    trans = paramiko.Transport(host, port)
    trans.connect(username=username, password=password)
    sftp = paramiko.sftp_client.SFTPClient.from_transport(trans)

    # send_dir_to_remote(class_file_dir, remote_class_dir, sftp, ssh, exclude_file_list)
    # 重启tomcat
    # restart_server(host, 22, username, password)
    # restart_server_ssh(ssh)
    ssh.close()
    sftp.close()
    pass

if __name__ == "__main__":
    # config = configparser.ConfigParser()
    # config.read('config-uncommit.ini')
    host = '192.168.200.238'; port = 22; username = 'dev-sc'; password = 'hgHHJ?@!#'
    # restart_server(host, port, username, password)
    deploy_all_files()
    # check_dir_exists('/app/apache-tomcat-7-sc/webapps/SC/test-dir/classes')
    pass

