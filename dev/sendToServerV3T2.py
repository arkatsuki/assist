import ftplib
import paramiko
import os
import configparser


"""
get_files_from_dir: 获取某个目录中中所有文件名（包括子目录里面的）的list。
restart_server: 重启tomcat。
restart_server_ssh: 重启tomcat。
backup_remote_dir: 备份远程及其上的指定目录（压缩打包成.tar.gz）。
send_dir_to_remote: 把本地目录发送到远程机器上的指定目录下。
deploy_all_files: 全量部署web服务。
"""


def get_files_from_dir(dir_absolute_path):
    """
    获取目录中所有文件名的list, 文件名是完整路径，斜杠分隔。
    :param dir_absolute_path:
    :return:
    """
    file_list = []
    if os.path.isdir(dir_absolute_path):
        for parent, dirnames, filenames in os.walk(dir_absolute_path):
            for filename in filenames:
                # 完整路径
                file_path = os.path.join(parent, filename).replace('\\','/')
                # print('file_path:',file_path)
                file_list.append(file_path)
                pass
            pass
        pass
    return file_list


def restart_server(host, port, username, password):
    """
    重启tomcat
    :return:
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=username, password=password)
    restart_server_ssh(ssh)
    ssh.close()
    pass


def restart_server_ssh(ssh):
    """
    重启tomcat
    :param ssh:
    :return:
    """
    # arr=`ps -ef|grep apache-tomcat-7-sc|awk '!/00:00:0./ {print $2}'`;len=${#arr[@]};echo "len="${len};echo "process num="${arr[0]};kill -9 ${arr[0]}
    stdin, stdout, stderr = ssh.exec_command("ps -ef|grep apache-tomcat-7-sc|awk '!/00:00:0./ {print $2}'")
    out = bytes.decode(stdout.read())
    out_li = out.split('\n')
    print('find process num',len(out_li))
    # if len(out_li)>2:
    #     return
    for line in out_li:
        if line.strip()!='':
            print('line strip:',line)
            ssh.exec_command('kill -9 ' + line.strip())
        pass
    # stdin, stdout, stderr = ssh.exec_command('/app/apache-tomcat-7-sc/bin/startup.sh')
    stdin, stdout, stderr = ssh.exec_command('source /etc/profile;/app/apache-tomcat-7-sc/bin/startup.sh')
    print('startup stdout result:', bytes.decode(stdout.read()))
    print('startup stderr result:', bytes.decode(stderr.read()))
    # 先不关闭，由建立ssh的那个调用方负责关闭
    # ssh.close()
    pass


def backup_remote_dir(dir_absolute_path, ssh):
    """
    备份目录。会删除上一次的备份。
    :param dir_absolute_path:
    :param ssh:
    :return:
    """
    # rm -rf WEB-INF2018*;curdate=`date +%Y%m%d%H%M%S`;echo $curdate;tar -zcf WEB-INF${curdate}.tar.gz WEB-INF
    check_dir_cmd = 'if [ ! -d "{}" ]; then echo "n"; else echo "y"; fi;'.format(dir_absolute_path)
    print('check_dir_cmd:', check_dir_cmd)
    stdin, stdout, stderr = ssh.exec_command(check_dir_cmd)
    std_our_str = bytes.decode(stdout.read()).strip()
    print('if stdout result:', std_our_str)
    print('if stderr result:', bytes.decode(stderr.read()))
    if std_our_str == 'n':
        ssh.exec_command('mkdir -p ' + dir_absolute_path)
        pass
    # 大括号里面的是占位符（可以有位置占位符和关键字占位符）
    # 对大括号转义：再额外加一个大括号。
    # cmd = 'cd {0}; rm -rf {1}20*;' + \
    #       'curdate=`date +%Y%m%d%H%M%S`;' \
    #       'echo $curdate;tar -zcf {1}${{curdate}}.tar.gz {1}' \
    #       ''.format(remote_dir_path, remote_dir_path.replace(os.path.basename(remote_dir_path), ''))
    cmd = 'cd ..; rm -rf {dir_name}20*;' + \
          'curdate=`date +%Y%m%d%H%M%S`;' \
          'echo $curdate;tar -zcf {dir_name}${{curdate}}.tar.gz {dir_name}' \
          ''.format(dir_name=dir_absolute_path.replace(os.path.basename(dir_absolute_path), ''))
    print(cmd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print('tar stdout result:', bytes.decode(stdout.read()))
    print('tar stderr result:', bytes.decode(stderr.read()))
    pass


def send_dir_to_remote(local_dir_path, remote_dir_path, sftp, ssh, exclude_file_list=[]):
    """
    另外一种方法：用库压缩成zip，然后单个文件发送linux，在linux解压zip。
    本地文件夹发送到远程目录。
    sftp只支持文件put，所以需要遍历目录。
    如果远程文件夹不存在会先新建。
    :param local_dir_path:  本地目录路径
    :param remote_dir_path: 远程目录路径
    :param sftp: sftp客户端
    :param ssh: ssh客户端
    :param exclude_file_list: 不更新的文件 
    :return: 
    """""
    all_deploy_file_list = []
    all_deploy_file_list.extend(get_files_from_dir(local_dir_path))
    final_file_list = []   # 保存最终需要传输的所有文件。
    final_file_list.extend(all_deploy_file_list)
    # 如果一边循环一边删除，再加上内部的判断，会出现错乱
    for deploy_file in all_deploy_file_list:
        for exclude_file in exclude_file_list:
            if deploy_file.endswith(exclude_file):
                final_file_list.remove(deploy_file)
                break
        pass
    for file in final_file_list:
        remote_file_path = file.replace(local_dir_path, remote_dir_path)
        dir_path = remote_file_path.replace(os.path.basename(remote_file_path), '')
        stdin, stdout, stderr = ssh.exec_command('mkdir -p ' + dir_path)
        err_msg = bytes.decode(stderr.read()).strip()
        if err_msg != '':
            print('mkdir stdout result:', bytes.decode(stdout.read()))
            print('mkdir stderr result:', err_msg)
            pass
        else:
            print('err_msg is null')
            pass
        # print('dir_path:', dir_path)
        # print('mkdir stdout result:', bytes.decode(stdout.read()))
        # print('mkdir stderr result:', bytes.decode(stderr.read()))
        sftp.put(localpath=file, remotepath=remote_file_path)
        pass
    pass


def ssh_info(ssh, instruction):
    """
    执行ssh命令并打印输出
    :param ssh:
    :param instruction:
    :return:
    """
    stdin, stdout, stderr = ssh.exec_command(instruction)
    # print('instruction:', instruction)
    print(bytes.decode(stdout.read()))
    print(bytes.decode(stderr.read()))
    pass


def error_info(ssh, instruction):
    """
    执行ssh命令并在出现异常时打印输出
    :param ssh:
    :param instruction:
    :return:
    """
    stdin, stdout, stderr = ssh.exec_command(instruction)
    err_msg = bytes.decode(stderr.read()).strip()
    if err_msg != '':
        print('instruction error:', instruction)
        print('mkdir stdout result:', bytes.decode(stdout.read()))
        print('mkdir stderr result:', err_msg)
        pass
    pass


def deploy_all_files():
    '''
    全量部署，除了部分配置文件。
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
    remote_class_dir = config.get('sendToServer','remote_class_dir')
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
    send_dir_to_remote(class_file_dir, remote_class_dir, sftp, ssh, exclude_file_list)
    # 重启tomcat
    restart_server_ssh(ssh)
    ssh.close()
    sftp.close()
    pass

if __name__ == "__main__":
    # config = configparser.ConfigParser()
    # config.read('config-uncommit.ini')
    host = '192.168.200.238'; port = 22; username = 'dev-sc'; password = 'hgHHJ?@!#'
    # restart_server(host, port, username, password)
    deploy_all_files()

    pass

