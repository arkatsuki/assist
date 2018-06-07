import ftplib
import paramiko
import os
import configparser


def te_listdir():
    dir_path = r'E:\tools-dev\dabangongju\sc-uat\output\Exported\target'
    for f in os.listdir(dir_path):
        print(f)
        pass
    pass


def te_link():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(hostname='123.57.56.45', port=22, username='appuser', password='c@c@i1go')
    # ssh.connect(hostname='123.57.56.45', port=22, username='appuser', password='FM1KfZU$')
    ssh.connect(hostname='123.57.56.45', port=22, username='appuser', password='FM1KfZU$')
    # ssh.connect(hostname='123.57.56.45', port=22, username='cndev2', password='xOM!!2*x')
    stdin, stdout, stderr = ssh.exec_command('cd /app/logs')
    print('stdout:', stdout)
    print('stderr:', stderr)
    ssh.close()
    pass


def te_str():
    cmd = 'cd {0}; rm -rf {0}20*;' + \
          'curdate=`date +%Y%m%d%H%M%S`;echo $curdate;tar -zcf {0}${{curdate}}.tar.gz {0}'
    print(cmd.format('WEB-INFO'))
    pass


if __name__ == "__main__":
    te_str()

    pass

