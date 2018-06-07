import os
from shutil import copy


if __name__ == "__main__":
    file_backup_path = r'E:\temp\backup\pom-p_web.xml'
    file_dest_path = r'D:\workspace\eclipse-oxygen\p_web2\pom.xml'
    copy(file_backup_path, file_dest_path)
    pass


