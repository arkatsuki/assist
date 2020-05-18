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

# 设置最大递归层数 否则递归深了会报错 maximum recursion depth exceeded while calling a Python object
sys.setrecursionlimit(10000)


def get_all_answer_url(*params):
    """
    获取某个问题的所有答案的url
    :param params:
    :return:
    """
    limit = 5
    offset = 0
    # if dowmloadPic.__code__.co_argcount >1:
    if len(params) >1:
        limit = params[0]
        offset = params[1]
        pass
    # print('limit:', limit, 'offset:', offset)
    # 成功的一个question_num: 367881928
    # question_num = '308085320' # 舔狗到底有多么卑微
    question_num = '300415423' # 舔狗到底有多卑微
    # question_num = '289633855' # 处女情结怎么克服啊 我男友特别喜欢我 但是他是真的有处女情节啊 怎么破
    # question_num = '309196396' # 有没有男人真的没有处女情结
    # question_num = '312334173' # 有你是否有处女 男情结 如果有 为什么
    # question_num = '29570644' # 有处女情结是错吗
    # question_num = '357824038' # 你喜欢的人和别人发生了关系你有什么感受
    # question_num = '307189774' # 发现自己舔的女神是别人的舔狗是种怎样的体验
    # question_num = '326181194' # 当你知道自己被带绿帽子是什么感觉
    # question_num = '31068506' # 男生得知自己被绿了是种怎样的体验
    # question_num = '301837738' # 女生得知自己被绿了是种怎样的体验
    url_get_answers = 'https://www.zhihu.com/api/v4/questions/' + question_num + '/answers?include=data%5B%2A%5D.is_normal' \
          '%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail' \
          '%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent' \
          '%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time' \
          '%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized' \
          '%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info' \
          '%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge' \
          '%5B%2A%5D.topics&limit='+ str(limit) + '&offset='+ str(offset) + '&platform=desktop&sort_by=default '

    # url_get_answers = 'https://www.zhihu.com/api/v4/questions/' + question_num + '/answers?include=data%5B%2A%5D.is_normal' \
    #       '%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail' \
    #       '%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent' \
    #       '%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time' \
    #       '%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized' \
    #       '%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info' \
    #       '%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge' \
    #       '%5B%2A%5D.topics&limit='+ str(limit) + '&offset='+ str(offset) + '&platform=desktop&sort_by=default '
    # print('url_get_answers:', url_get_answers)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        ,'authority': 'www.zhihu.com',
        'referer' : 'https://www.zhihu.com/question/300415423',
        'cookie' : '_zap=37a92473-e671-4bf0-94ec-68ebacdcef12; '
                   'd_c0="AECg1FwpXRCPTr593iMS_eqQZzKJYEWy9vI=|1573909874"; _xsrf=o8GnotMOZgGFJC2HVuekmVAWkS39Nh2s; '
                   '_ga=GA1.2.1704039401.1583584893; tst=r; '
                   'q_c1=c129a4aa8651406a8192191a16831f20|1587977475000|1587977475000; '
                   '_gid=GA1.2.1679089183.1589164550; __utma=51854390.1704039401.1583584893.1589555489.1589695987.3; '
                   '__utmz=51854390.1589695987.3.3.utmcsr=zhihu.com|utmccn=('
                   'referral)|utmcmd=referral|utmcct=/question/300415423/answer/574881894; '
                   '__utmv=51854390.100-1|2=registration_date=20130620=1^3=entry_date=20130620=1; '
                   'capsion_ticket="2|1:0|10:1589717495|14:capsion_ticket|44'
                   ':NGQ3YTFkMzhlN2QzNGU1MTg3YTQzNzY0M2QxOWJjYzA'
                   '=|a1d57bb24bc48be7d3284e4657583ea9c48d970ec0ec33632bd7c8fba3994982"; '
                   'z_c0="2|1:0|10:1589717503|4:z_c0|92'
                   ':Mi4xWVEycEFBQUFBQUFBUUtEVVhDbGRFQ1lBQUFCZ0FsVk5fM2V1WHdEcXkzUDNBenlOYnBpb0NYWE5oSGQ2OGMwVm9B'
                   '|c710098eaf5b712ac93d033833037b4d1ff69f705ca55e613ca2f71e45446389"; '
                   'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1589697063,1589717467,1589720846,1589755881; '
                   '_gat_gtag_UA_149949619_1=1; SESSIONID=t0vU37BEQL5q7lbiOOdv0JdAqVSn5RTL2UjYzA64oPz; '
                   'JOID=VFwUBk2ywOupXHM1b7Fy8z9NOX55xPWZ_29Gci7jjtvcaB9VA19-LfRedDRoXhLIKkJatDmsbxarYKz_tuAjPUE=; '
                   'osd=W1gWCk69xOmlX3wxbb1x_DtPNX12wPeV_GBCcCLggd_eZBxaB11yLvtadjhrURbKJkFVsDugbBmvYqD8ueQhMUI=; '
                   'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1589755905; '
                   'KLBRSID=4efa8d1879cb42f8c5b48fe9f8d37c16|1589755924|1589755879 '
    }
    result = requests.get(url_get_answers, headers=headers)
    # print('result.status_code:', result.status_code)
    # print('json:', comment_json, '\n')
    result_json = json.loads(result.content)
    # print('result_json:', result_json)
    # if 'error' in result_json.keys():
    #     print('error')
    #     pass
    if result_json['paging']['is_end']:
        return
    for single_data in result_json['data']:
        question_url = single_data['question']['url']
        # print('question url:', question_url)
        question_num = question_url[question_url.rfind('/')+1:]

        answer_url = single_data['url']
        answer_num = answer_url[answer_url.rfind('/')+1:]
        answer_url_get = 'https://www.zhihu.com/question/'+ question_num +'/answer/' + answer_num
        with open('D:\\temp\\testdir\\answer_url.txt', 'a+', encoding='gb18030') as fp_content:
            fp_content.write(answer_url_get + '\n')
            pass
        print('answer_url_get:', answer_url_get)
        dowmload_answers(answer_url_get)
        pass

    offset = offset + limit
    get_all_answer_url(limit, offset)
    pass


if __name__ == '__main__':
    get_all_answer_url()
