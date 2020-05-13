import re
import requests
# from BeautifulSoup4 import *
# import BeautifulSoup4
from bs4 import BeautifulSoup
# from lxml import html
import os


def dowmloadPic(url, file_path):
    headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    html = result.content
    # print('html:', html, '\n')

    # html.replace('<br>', '\n').replace('<br/>', '\n')   # 会报错a bytes-like object is required, not 'str'
    # soup = BeautifulSoup(html, fromEncoding='utf-8')
    soup = BeautifulSoup(html, fromEncoding='gb18030') # 取标签内的汉字时，避免乱码
    # soup = BeautifulSoup(html, 'lxml')
    i = 0
    # for box in soup.findAll('div', class_='RichContent RichContent--unescapable'):


    for box in soup.findAll('div', id='postlist'):
        # print('box:', box, '\n')

        for lable_td in box.findAll('td', class_='t_f'):
            # b = str(b).replace('<br>', '\n').replace('<br/>', '\n') # 这样做后续就没法get_text()了
            txt = lable_td.get_text('\n', 'br')  # 把<br>标签替换成换行
            # txt = b.get_text()
            # print('txt:', txt)
            with open(file_path, 'a+', encoding='gb18030') as fp_content:
                fp_content.write(txt)
                fp_content.write('\n')
            pass
        pass
    # 下面这样可以获取“下一页”按钮的url
    page_lable = soup.find('div', class_='pgs mtm mbm cl').find('a', class_='nxt')
    if page_lable is not None:
        next_url = page_lable['href']
        print('next_url:', next_url)
        dowmloadPic('http://7.emoyiyi.com/' + next_url + '&_dsign=d4dcdec8', file_path)
        pass



    pass


if __name__ == '__main__':
    # 如果文件已经存在，先删除
    file_path = 'D:\\temp\\testdir\\content.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
        pass
    # url = 'https://www.zhihu.com/question/385655582/answer/1164227477'
    url = 'http://7.emoyiyi.com/forum.php?mod=viewthread&tid=1136068&page=1&_dsign=d4dcdec8'
    dowmloadPic(url, file_path)
