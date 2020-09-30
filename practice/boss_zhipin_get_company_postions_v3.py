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
import random

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
        , 'cookie': 'lastCity=101280600; t=ePAH64gcnMMtNefh; wt=ePAH64gcnMMtNefh; '
                    '_bl_uid=UwkXafjUe7s3hs07pn5vtkbrbOzC; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1600613083,'
                    '1600697963,1600786574,1601457358; __g=-; __c=1601457359; '
                    '__l=l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3Djava%26city%3D101280600%26industry%3D'
                    '%26position%3D&r=&g=&friend_source=0&friend_source=0; '
                    '__a=29091850.1596342561.1600786575.1601457359.407.28.21.407; '
                    '__zp_stoken__=0138bGiIsUWg%2FB0hpUWs2fwYjFEA8IyNrID92IUgWO2ERE292IE8pP0IKCyMlcSl'
                    '%2BTxwJdy4vUk5dEWoXNw00b1USWkU4Pw4RN3UldhZ1VFFiRGI6Q0dQNjgMFF5qEWAHSU0DZDVbIEQ3GFp0RQ%3D%3D; '
                    'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1601460703 '
    }
    result = requests.get(url_init, headers=headers)
    print('result.contentL:', result.content)
    print('result.status_code:', result.status_code)

    cookie = requests.utils.dict_from_cookiejar(result.cookies)
    print('cookie:', cookie)

    with open('D:\\temp\\testdir\\cookie.txt', 'a+') as fp_cookie:
        fp_cookie.write(cookie + '\n')
        pass

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

    pass


def get_all_company_postions_urls(url_init):

    url_list_job_detail_all = []

    # url_next_page, url_list_job_detail = get_company_postions_url(url_init)
    # print(url_next_page)
    # print(url_list_job_detail)
    # url_list_job_detail_all.extend(url_list_job_detail)

    url_next_page = url_init

    while url_next_page != '':
        time.sleep(random.randint(3, 9))
        url_next_page, url_list_job_detail = get_company_postions_url(url_next_page)
        print(url_list_job_detail)
        url_list_job_detail_all.extend(url_list_job_detail)
        pass

    with open('D:\\temp\\testdir\\url.txt', 'a+') as fp:

        for url in url_list_job_detail_all:
            fp.write(url + '\n')
            pass


        pass

    pass


if __name__ == '__main__':

    # bug: cookie会更新 失效，需要每次请求取新的cookie设置到下一次请求中

    url_init = 'https://www.zhipin.com/gongsir/29c1ab68d5e3d3360nN63Q~~.html?ka=company-jobs'

    get_all_company_postions_urls(url_init)
