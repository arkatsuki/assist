import re
import requests
# from BeautifulSoup4 import *
# import BeautifulSoup4
from bs4 import BeautifulSoup
# from lxml import html
import os


def dowmloadPic(html):
    """
    缺点：有些答案，返回的是登录页面。所以，后续要考虑增加登录功能
    :param html:
    :return:
    """
    # print('html:', html, '\n')

    # html.replace('<br>', '\n').replace('<br/>', '\n')   # 会报错a bytes-like object is required, not 'str'
    # soup = BeautifulSoup(html, fromEncoding='utf-8')
    soup = BeautifulSoup(html, fromEncoding='gb18030') # 取标签内的汉字时，避免乱码
    # soup = BeautifulSoup(html, 'lxml')
    i = 0

    # 如果文件已经存在，先删除
    file_path = 'D:\\temp\\testdir\\content.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
        pass
    # for box in soup.findAll('div', class_='RichContent RichContent--unescapable'):
    for box in soup.findAll('div', class_='RichContent RichContent--unescapable'):
        print('box:', box, '\n')

        # b = str(b).replace('<br>', '\n').replace('<br/>', '\n') # 这样做后续就没法get_text()了
        txt = box.get_text('\n', 'br')  # 把<br>标签替换成换行
        # txt = b.get_text()
        print('txt:', txt)
        with open(file_path, 'a+', encoding='gb18030') as fp_content:
            fp_content.write(txt)
            fp_content.write('\n')
        pass

        for a in box.findAll('img'):
            # src = a.get('src')
            src = a.get('src')
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
                dir = 'D:\\temp\\testdir\\' + '20200427_' + '{0:0>4}'.format(str(i)) + '.jpg'
                print("dir:", dir)
                fp = open(dir, 'wb')
                fp.write(pic.content)
                fp.close()
                print('download end')
                pass

    print('i:', i)


if __name__ == '__main__':
    # url = 'https://www.zhihu.com/question/385655582/answer/1164227477'
    url = 'https://www.zhihu.com/question/319637812/answer/844124334'
    # url = 'https://www.zhihu.com/api/v4/answers/997190122/root_comments?order=normal&limit=20&offset=20&status=open'
    # url = 'https://www.zhihu.com/question/375265966/answer/1135813803'
    headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    dowmloadPic(result.content)
