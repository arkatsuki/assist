import re
import requests
# from BeautifulSoup4 import *
# import BeautifulSoup4
from bs4 import BeautifulSoup
# from lxml import html


def dowmloadPic(html):
    # print('html:', html, '\n')

    soup = BeautifulSoup(html, fromEncoding='utf-8')
    # soup = BeautifulSoup(html, fromEncoding='gb18030')
    # soup = BeautifulSoup(html, 'lxml')
    i = 0
    for box in soup.findAll('div', class_='tpc_content do_not_catch'):
        print('box:', box, '\n')
        for a in box.findAll('img'):
            # src = a.get('src')
            src = a.get('ess-data')
            if src is not None:
                print('src:', src, '\n')
                i += 1

                # if i <= 20:
                #     continue

                try:
                    pic = requests.get(src, timeout=60)
                # except requests.exceptions.ConnectionError:
                except Exception:
                    with open('D:\\temp\\testdir\\fail.txt', 'a+') as fp_fail:
                        fp_fail.write(src + '\t' + str(i) + '\n')

                    print('【错误】当前图片无法下载')
                    continue

                # '{0:0>4}'.format(1) 第二个0表示前面补0, 4表示一共4位，'>'表示右对齐，'<'表示左对齐。
                dir = 'D:\\temp\\testdir\\' + '20200426_' + '{0:0>4}'.format(str(i)) + '.jpg'
                print("dir:", dir)
                fp = open(dir, 'wb')
                fp.write(pic.content)
                fp.close()
                print('download end')
                pass

    print('i:', i)


if __name__ == '__main__':
    url = 'https://cl.n2sa.xyz/htm_data/2003/7/3861851.html'
    # url = 'https://cl.fc55.cf/htm_data/2003/7/3861851.html'
    result = requests.get(url)
    # dowmloadPic(result.text)
    dowmloadPic(result.content)
