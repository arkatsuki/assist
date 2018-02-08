import ftplib
import paramiko
import os
import configparser


def get_files_from_dir(dir_path):
    """
    目录转换成文件名list
    :param dir_path:
    :return:
    """
    file_list = []
    if os.path.isdir(dir_path):
        for parent, dirnames, filenames in os.walk(dir_path):
            for filename in filenames:
                file_path = os.path.join(parent, filename)
                print('file_path:',file_path)
                file_list.append(file_path)
                pass
            pass
        pass
    return file_list
    pass


def get_files_from_dir(local_dir, remote_dir):
    file_pair_list = [] # 存放 本地&服务器 文件名对
    local_file_path = []

    pass


def send_file_sftp(host, port, username, password, local_path, remote_path):
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

        local_file_list = []   # 保存所有的本地文件
        if os.path.isdir(local_path):
            local_file_list = get_files_from_dir(local_path)
            pass
        else:
            local_file_list.append(local_path)

        # 无论上传还是下载，两个路径都必须到文件名，不能到目录
        sftp.put(localpath=local_path, remotepath=remote_path)
        # sftp.get(remote_path, local_path)
        trans.close()
    except Exception as e:
        print(e)
        raise

    pass


def exec_command_sftp():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('cd /app/apache-tomcat-7-sc')
    pass


def exec_command_ssh(ssh):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('cd /app/apache-tomcat-7-sc')
    pass


def exec_command_ftp(host, port):
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

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    # result = excel_operation.read_excel(excelFile)
    # for row_val in result:
    #     local_remote_path = get_class_paths(row_val[0], local_class_dir, remote_class_dir)
    #     send_file_sftp(host,password,local_remote_path[0],local_remote_path[1])
    #     pass
    # print(result)
    # D:\workplace\eclipse\cnweb_sc\target\classes
    host = config.get('sendToServer', 'local_host'); port = 22;
    username = config.get('sendToServer', 'local_username'); password = config.get('sendToServer', 'local_pw');
    # host = '192.168.200.238'; port = 22; username = 'dev-sc'; password = 'hgHHJ?@!#'
    # loacl_path = 'C:/Users/duanyaochang/Desktop/temp/temp-sql.txt'
    # remote_path = '/app/apache-tomcat-7-sc/webapps/temp-sql.txt'
    # loacl_path = 'D:/workplace/eclipse/cnweb_sc/target/classes'
    # remote_path = '/app/apache-tomcat-7-sc/webapps/SC/WEB-INF/classes'
    # send_file_sftp(hostname, port, username, password,
    #                loacl_path, remote_path)
    restart_server(host, port, username, password)
    pass

