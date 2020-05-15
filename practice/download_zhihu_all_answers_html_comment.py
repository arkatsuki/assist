import re
import requests
# from BeautifulSoup4 import *
# import BeautifulSoup4
from bs4 import BeautifulSoup
# from lxml import html
import json
import os
from urllib import parse


def get_zhihu_comments(*params):
    """
    获取知乎某个回答下面的评论
    缺点：
    :param comment_json:
    :return:
    """
    answer_num = params[0]
    file_path = params[1]
    # comments_url = answer_url + '/root_comments?order=normal&limit=20&offset=0&status=open'
    # comments_url = 'https://www.zhihu.com/api/v4/answers/997190122/root_comments?order=normal&limit=20&offset=0&status=open'
    comments_url = 'https://www.zhihu.com/api/v4/answers/' + answer_num + '/root_comments?order=normal&limit=20&offset=0&status=open'
    # 如果文件已经存在，先删除
    if file_path is None:
        file_path = 'D:\\temp\\testdir\\content.txt'
        pass


    if os.path.exists(file_path):
        os.remove(file_path)
        pass
    # print('comments_url11:', comments_url)
    get_zhihu_comments_from_comments_url(comments_url, file_path)


def get_zhihu_comments_from_comments_url(comments_url, file_path):
    headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    result = requests.get(comments_url, headers=headers)
    # print('json:', comment_json, '\n')
    comment_json = json.loads(result.content)
    comment_num = comment_json['common_counts']  # 这个包括子评论，不能用于评论的分页
    comment_paging_is_end = comment_json['paging']['is_end']  # 是不是最后一页
    comment_paging_totals = comment_json['paging']['totals']
    # print('comment_num:', comment_num)
    # page_num = 1
    # url_params = parse.parse_qs(parse.urlparse(comments_url).query)
    # print('url_params:', url_params)
    # page_num = 0
    # if url_params['offset'] is not None:
    #     page_num = url_params['offset'] / 20 + 1
    #     pass
    # print('page_num:', page_num)

    # print('comments_url:', comments_url)
    print_comments(comment_json, file_path)


    # cycle_num = comment_paging_totals/20
    # print('cycle_num:', cycle_num)
    if not comment_paging_is_end:
        # print('continue')
        # comments_url = answer_url + '/root_comments?order=normal&limit=20&offset='+ page_num*20 +'&status=open'
        next_comments_url = comment_json['paging']['next']
        get_zhihu_comments_from_comments_url(next_comments_url, file_path)
    pass


def print_comments(comment_json, file_path):

    for single_comment in comment_json['data']:
        comment_text_str = single_comment['author']['member']['name'] + ': ' + single_comment['content']
        # print(single_comment['author']['member']['name'], ': ', single_comment['content'])
        with open(file_path, 'a+', encoding='gb18030') as fp_content:
            # fp_content.write('page_num:' + str(page_num))
            # fp_content.write('\n')
            fp_content.write(comment_text_str)
            fp_content.write('\n')
            pass
        # child_comment_url = 'https://www.zhihu.com/api/v4/comments/832887873/child_comments'
        child_comment_count = single_comment['child_comment_count']
        # child_comments = single_comment['child_comments']

        # 子评论 注意 也会分页，有child_comment_json
        # 'https://www.zhihu.com/api/v4/comments/834740835/child_comments'
        if single_comment['child_comment_count'] != 0:
            child_comment_url = single_comment['url'] + '/child_comments'
            print_child_comments(child_comment_url, file_path)
            pass


        # 这种方式只能获取展示出来的前两个，折叠的那些没法获取
        # for child_comment in single_comment['child_comments']:
        #     # print('\t', 'reply: ', child_comment['author']['member']['name'], ': ', child_comment['content'])
        #     with open(file_path, 'a+', encoding='gb18030') as fp_content:
        #         child_comment_text_str = '\t' + 'reply: ' + child_comment['author']['member']['name'] + ': ' + child_comment['content']
        #         fp_content.write(child_comment_text_str)
        #         fp_content.write('\n')
        #         pass
        #     pass



        pass
    pass


def print_child_comments(child_comment_url, file_path):
    """
    加载子评论，包括“查看全部xx条回复”按钮展示的那些.
    :param child_comment_url:
    :param file_path:
    :return:
    """
    headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    result = requests.get(child_comment_url, headers=headers)
    child_comment_json = json.loads(result.content)
    # print('child_comment_json:', child_comment_json)
    for single_child_comment in child_comment_json['data']:
        with open(file_path, 'a+', encoding='gb18030') as fp_content:
            child_comment_text_str = '\t' + 'reply: ' + single_child_comment['author']['member']['name'] + ': ' + \
                                     single_child_comment['content']
            fp_content.write(child_comment_text_str)
            fp_content.write('\n')
            pass
        pass
    if not child_comment_json['paging']['is_end']:
        next_comments_url = child_comment_json['paging']['next']
        print_child_comments(next_comments_url, file_path)
    pass


if __name__ == '__main__':
    # url = 'https://www.zhihu.com/question/357824038/answer/997190122'
    # url = 'https://www.zhihu.com/api/v4/answers/997190122'
    # url = 'https://www.zhihu.com/api/v4/answers/997190122/root_comments?order=normal&limit=20&offset=20&status=open'
    answer_num = ''
    get_zhihu_comments(answer_num)
