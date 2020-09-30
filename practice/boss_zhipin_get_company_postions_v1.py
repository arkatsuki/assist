import re
import requests
# from BeautifulSoup4 import *
# import BeautifulSoup4
from bs4 import BeautifulSoup
# from lxml import html
import os
from practice.download_zhihu_all_answers_content_v3 import dowmload_answers
import json
import sys
import time

# 设置最大递归层数 否则递归深了会报错 maximum recursion depth exceeded while calling a Python object
sys.setrecursionlimit(10000)


def get_company_postions_url(url_init):

    print('url_init:', url_init)

    # url = 'https://www.zhipin.com/gongsir/29c1ab68d5e3d3360nN63Q~~.html?ka' \
    #                   '=search_rcmd_joblist_29c1ab68d5e3d3360nN63Q~~ '

    url_prefix = 'https://www.zhipin.com'

    url_list_job_detail = []
    url_next_page = ''

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        # ,'authority': 'www.zhihu.com',
        # 'referer' : 'https://www.zhihu.com/question/300415423',
        ,'cookie' : 'lastCity=101280600; t=ePAH64gcnMMtNefh; wt=ePAH64gcnMMtNefh; '
                    '_bl_uid=UwkXafjUe7s3hs07pn5vtkbrbOzC; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1600613083,'
                    '1600697963,1600786574,1601457358; __g=-; __c=1601457359; '
                    '__l=l=%2Fwww.zhipin.com%2Fgongsir%2F29c1ab68d5e3d3360nN63Q~~.html%3Fpage%3D2&r=&g=&friend_source'
                    '=0&friend_source=0; __a=29091850.1596342561.1600786575.1601457359.395.28.9.395; '
                    'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1601459842; '
                    '__zp_stoken__=0138bGiIsUWg%2FB2hDOgh1fwYjFEB8UWRkC2V2IUgWOzF2Jyd%2BME8pP0IKAj8gC2l'
                    '%2BTxwJdy4vJTtHb0wXXnpgHT5tWy4xNXAXShUqCAwXVFFiRGI6QwcqMyQFFF5qEWAXSU0DZDVbIEQ3GFp0RQ%3D%3D '
    }
    result = requests.get(url_init, headers=headers)
    print('result.content:', result.content)
    soup = BeautifulSoup(result.content, 'html.parser', from_encoding='gb18030') # 取标签内的汉字时，避免乱码
    for box in soup.findAll('div', class_='job-list'):
        print('find class job-list')
        for a in box.findAll('a'):
            if a.get('ka') == 'page-next':
                url_next_page = url_prefix + a.get('href')
                pass
            else:
                href_attr = a.get('href')
                if href_attr.startswith('/job_detail'):
                    print('/job_detail', url_prefix + href_attr)
                    url_list_job_detail.append(url_prefix + href_attr)
                    pass

            pass

        pass
    return url_next_page, url_list_job_detail


if __name__ == '__main__':


    # url_init = 'https://www.zhipin.com/gongsir/29c1ab68d5e3d3360nN63Q~~.html?ka' \
    #                       '=search_rcmd_joblist_29c1ab68d5e3d3360nN63Q~~ '

    url_init = 'https://www.zhipin.com/gongsir/29c1ab68d5e3d3360nN63Q~~.html?ka=company-jobs'

    url_next_page, url_list_job_detail = get_company_postions_url(url_init)
    print('url_next_page:', url_next_page)
    print('url_list_job_detail:', url_list_job_detail)
