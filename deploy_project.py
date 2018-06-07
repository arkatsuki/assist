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
    host = '192.168.200.238'; port = 22; username = 'dev-sc'; password = 'hgHHJ?@!#'
    # restart_server(host, port, username, password)
    deploy_all_files()
    pass

