import os


def rename_to_txt(dir_path):
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            if not filename.endswith('.txt'):
                # print('filename:',filename)

                if filename.find('.') > -1:
                    filename_new = filename[:filename.find('.')] + '$' + filename[filename.find('.')+1:] + '.txt'
                    os.rename(os.path.join(parent, filename), os.path.join(parent, filename_new))
                    pass

                pass
            pass
        pass
    pass

def rename_to_original(dir_path):
    for parent, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename.find('$') > -1:
                # print('filename:',filename)
                filename_new = filename[:filename.find('.')]
                filename_new = filename_new.replace('$', '.')
                os.rename(os.path.join(parent, filename), os.path.join(parent, filename_new))

                pass
            pass
        pass
    pass


if __name__ == "__main__":
    # os.rename(r'E:\git\transfer\transfer\offsite\sf-off\do_o.py', r'E:\git\transfer\transfer\offsite\sf-off\do_o.txt')
    # dir_path = r'E:\git\transfer\transfer\offsite'
    dir_path = r'D:\work-all\workplace\repository\transfer\offsite'
    # rename_to_txt(dir_path)
    rename_to_original(dir_path)
    pass
