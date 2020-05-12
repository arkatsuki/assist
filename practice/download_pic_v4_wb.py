import re
import requests
# from BeautifulSoup4 import *
# import BeautifulSoup4
from bs4 import BeautifulSoup
# from lxml import html


def dowmloadPic(html):
    print('html:', html, '\n')

    # html.replace('<br>', '\n').replace('<br/>', '\n')   # 会报错a bytes-like object is required, not 'str'
    soup = BeautifulSoup(html, fromEncoding='utf-8')
    # soup = BeautifulSoup(html, fromEncoding='gb18030') # 取标签内的汉字时，避免乱码
    # soup = BeautifulSoup(html, 'lxml')
    i = 0
    # for box in soup.findAll('div', class_='WB_cardwrap WB_feed_type S_bg2 WB_feed_vipcover WB_feed_like'):
    for box in soup.findAll('div', class_='WB_feed WB_feed_v3 WB_feed_v4'):
        print('box:', box, '\n')

        for a in box.findAll('img'):
            src = a.get('src')
            # src = a.get('ess-data')
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
                dir = 'D:\\temp\\testdir\\' + '20200428_' + '{0:0>4}'.format(str(i)) + '.jpg'
                print("dir:", dir)
                fp = open(dir, 'wb')
                fp.write(pic.content)
                fp.close()
                print('download end')
                pass

    print('i:', i)


if __name__ == '__main__':
    url = 'https://weibo.com/p/1005056556637551/home?profile_ftype=1&is_all=1#_0'
    headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    dowmloadPic(result.content)
