import re
import requests
# from BeautifulSoup4 import *
# import BeautifulSoup4
from bs4 import BeautifulSoup
# from lxml import html


def dowmloadPic(html):
    # print('html:', html, '\n')

    # html.replace('<br>', '\n').replace('<br/>', '\n')   # 会报错a bytes-like object is required, not 'str'
    # soup = BeautifulSoup(html, fromEncoding='utf-8')
    soup = BeautifulSoup(html, fromEncoding='gb18030') # 取标签内的汉字时，避免乱码
    # soup = BeautifulSoup(html, 'lxml')
    i = 0
    for box in soup.findAll('div', class_='tpc_content do_not_catch'):
        print('box:', box, '\n')

        # b = str(b).replace('<br>', '\n').replace('<br/>', '\n') # 这样做后续就没法get_text()了
        txt = box.get_text('\n', 'br')  # 把<br>标签替换成换行
        # txt = b.get_text()
        print('txt:', txt)
        with open('D:\\temp\\testdir\\content.txt', 'a+', encoding='gb18030') as fp_content:
            fp_content.write(txt)
            fp_content.write('\n')
        pass

        for a in box.findAll('img'):
            # src = a.get('src')
            src = a.get('ess-data')
            if src is None:
                src = a.get('data-src')
                pass
            if src is not None:
                print('src:', src, '\n')
                i += 1

                # if i <= 21:
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
                dir = 'D:\\temp\\testdir\\' + '20200522_' + '{0:0>4}'.format(str(i)) + '.' + src[src.rfind(
                    '.') + 1:]
                print("dir:", dir)
                fp = open(dir, 'wb')
                fp.write(pic.content)
                fp.close()
                print('download end')
                pass

    print('i:', i)


if __name__ == '__main__':
    # url = 'https://cl.n2sa.xyz/htm_data/2002/7/3829905.html'
    url = 'https://c1.a9ae.icu/htm_data/2002/7/3818711.html'
    result = requests.get(url)
    dowmloadPic(result.content)
