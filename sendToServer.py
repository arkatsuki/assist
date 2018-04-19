import ftplib
import paramiko
import os
import configparser


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
    pass



def send_file_sftp_single(host, port, username, password, local_path, remote_path):
    """
    :param local_path:
    :param remote_path:
    :return:
    """
    try:
        # trans = paramiko.Transport((host, port))
        trans = paramiko.Transport(host, port)
        trans.connect(username=username, password=password)
        # sftp = paramiko.SFTPClient.from_transport(trans)
        sftp = paramiko.sftp_client.SFTPClient.from_transport(trans)

        # 无论上传还是下载，两个路径都必须到文件名，不能到目录
        sftp.put(localpath=local_path, remotepath=remote_path)
        # sftp.get(remote_path, local_path)
        trans.close()
    except Exception as e:
        print(e)
        raise

    pass


def send_file_sftp_pair(host, port, username, password, path_pair):
    """
    :param local_path:
    :param remote_path:
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


def exec_command_sftp():
    '''
    sftp连接并执行命令
    :return:
    '''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('cd /app/apache-tomcat-7-sc')
    pass


def exec_command_ssh(ssh):
    '''
    ssh连接并执行命令
    :param ssh:
    :return:
    '''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('cd /app/apache-tomcat-7-sc')
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


def backup_remote():
    pass


def restart_server(host, port, username, password):
    """
    ssh连接服务器，执行shell命令
    :return:
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=username, password=password)
    # ssh.connect(hostname='192.168.48.128', port=22, username='root', password='centos2018')
    # stdin, stdout, stderr = ssh.exec_command('cd /app/apache-tomcat-7-sc/bin')
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
    # print('stdout:',out)
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


def deploy_all_files():
    '''
    全量部署，除了部分配置文件
    :return:
    '''
    # 编译
    compile_rs = os.popen(r'compile.bat')
    print('compile result:', compile_rs.read())
    continue_flag = input('press any key to continue')
    if 'n'==continue_flag:
        print('return !!!')
        return
    print('continue !!!')
    config = configparser.ConfigParser()
    config.read('config-uncommit.ini')
    class_file_dir = config.get('sendToServer','class_file_dir')
    all_deploy_file_list = []
    # 不更新的文件
    exclude_file_list = ['applicationContext.xml','applicationContext-shiro.xml','disconf.properties'
                         ,'dubbo.properties','ehcache.xml','jdbc.properties','log4j.properties','mail.properties'
                         ,'mybatis-config.xml','redis.properties','spring-mvc.xml']
    all_deploy_file_list.extend(get_files_from_dir(class_file_dir))
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
    remote_class_dir = config.get('sendToServer','remote_class_dir')
    file_path_pair = convert_to_path_pair(final_file_list, class_file_dir, remote_class_dir)
    host = config.get('sendToServer','dev_host')
    name = config.get('sendToServer','dev_username')
    password = config.get('sendToServer','dev_pw')
    send_file_sftp_pair(host, 22, name, password, file_path_pair)
    restart_server(host, 22, username, password)
    pass

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config-uncommit.ini')

    # host = config.get('sendToServer', 'local_host'); port = 22;
    # username = config.get('sendToServer', 'local_username'); password = config.get('sendToServer', 'local_pw');
    host = '192.168.200.238'; port = 22; username = 'dev-sc'; password = 'hgHHJ?@!#'
    # restart_server(host, port, username, password)
    deploy_all_files()
    # b = os.popen(r'D:/compile.bat')

    pass

