import re
import requests
# from BeautifulSoup4 import *
# import BeautifulSoup4
from bs4 import BeautifulSoup
# from lxml import html
import os
from practice.download_zhihu_all_answers_html_content import dowmload_answers
# from practice.download_zhihu_all_answers_html_comment import get_zhihu_comments


def dowmloadPic():
    html = ''
    with open('D:\\temp\\testdir\\response_html.txt', 'r', encoding='utf-8') as fp_content:
        html = fp_content.read()
        pass

    # print('html:', html, '\n')

    # html.replace('<br>', '\n').replace('<br/>', '\n')   # 会报错a bytes-like object is required, not 'str'
    # soup = BeautifulSoup(html, fromEncoding='utf-8')
    soup = BeautifulSoup(html, fromEncoding='gb18030') # 取标签内的汉字时，避免乱码
    # soup = BeautifulSoup(html, 'lxml')
    i = 0
    # for box in soup.findAll('div', class_='RichContent RichContent--unescapable'):

    for box in soup.findAll('meta', itemprop='url'):
        answer_url = box.get('content')
        if 'answer' in answer_url:
            print('answer_url:', answer_url, '\n')
            dowmload_answers(answer_url)
            # begin = answer_url.rfind('/')
            # answer_num = answer_url[begin + 1:]
            # get_zhihu_comments(answer_num)
            pass
        pass
    pass


if __name__ == '__main__':
    dowmloadPic()
