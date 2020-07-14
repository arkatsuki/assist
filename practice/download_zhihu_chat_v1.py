import re
import requests
# from BeautifulSoup4 import *
# import BeautifulSoup4
from bs4 import BeautifulSoup
# from lxml import html
import json
import os
from urllib import parse


def get_chat(*params):
    """
    获取知乎某个回答下面的评论
    缺点：
    :param comment_json:
    :return:
    """
    # answer_num = params[0]

    # comments_url = answer_url + '/root_comments?order=normal&limit=20&offset=0&status=open'
    # comments_url = 'https://www.zhihu.com/api/v4/answers/997190122/root_comments?order=normal&limit=20&offset=0&status=open'
    # url = 'https://www.zhihu.com/api/v4/chat?sender_id=6328d70d5a017590dd00a9a6400b5323&limit=20'
    # url = 'https://www.zhihu.com/messages?sender_id=6328d70d5a017590dd00a9a6400b5323\u0026after_id=1259253898768048128\u0026limit=20'
    url = 'https://www.zhihu.com/messages?sender_id=6328d70d5a017590dd00a9a6400b5323&after_id=1259253898768048128&limit=20'
    file_path = 'D:\\temp\\testdir\\chat.txt'
    # 如果文件已经存在，先删除
    if len(params) > 1:
        file_path = params[1]
        pass


    if os.path.exists(file_path):
        os.remove(file_path)
        pass
    # print('comments_url11:', comments_url)
    headers = {
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        ,
        'cookie' : '_zap=37a92473-e671-4bf0-94ec-68ebacdcef12; '
                   'd_c0="AECg1FwpXRCPTr593iMS_eqQZzKJYEWy9vI=|1573909874"; _ga=GA1.2.1704039401.1583584893; tst=r; '
                   '__utmv=51854390.100-1|2=registration_date=20130620=1^3=entry_date=20130620=1; '
                   'q_c1=c129a4aa8651406a8192191a16831f20|1590650327000|1587977475000; '
                   '_gid=GA1.2.881508125.1591272343; '
                   'capsion_ticket="2|1:0|10:1592476778|14:capsion_ticket|44'
                   ':NmFkNzg0NDU5NjliNDY5ZDhmZjdiYTdhNTExZDM4Y2M'
                   '=|467bdca16e16e56083a0297db141ed436b488b4e6b9b92317b665ac434031c3f"; '
                   'z_c0="2|1:0|10:1592476783|4:z_c0|92'
                   ':Mi4xTF9jT0FBQUFBQUFBUUtEVVhDbGRFQ1lBQUFCZ0FsVk5iNUxZWHdBelk3R3V2RzM4WFFfYWFpendvOWk3TG1OQWxB'
                   '|9af2ce1a533e5a517a954f9c1da6ba905dded0e6f8c475d8819ef08af15aa619"; '
                   '__utma=51854390.1704039401.1583584893.1592818174.1592883910.23; '
                   '__utmz=51854390.1592883910.23.23.utmcsr=zhihu.com|utmccn=('
                   'referral)|utmcmd=referral|utmcct=/question/326401244; _xsrf=1ea28fe2-f2a6-46c9-a224-e9497b6951f0; '
                   'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1592993274,1592993556,1593006664,1593011286; '
                   'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1593012215; '
                   'SESSIONID=yBKUGYkXRIlYVvgn4IKnJW1lv7q4LzV3MrSjcx9soez; '
                   'JOID=UFkSAk51DFW8-U6FVnYYCyD6gvhCD0gY7bkU6AggRj_jqz_hPoZjpOH9S4VU_r1FCmOCE2DcdqjrUCmnIGXlx7I=; '
                   'osd=VFwXAENxCVC-9EqAU3QVDyX_gPVGCk0a4L0R7QotQjrmqTLlO4NhqeX4TodZ-rhACG6GFmXee6zuVSuqJGDgxb8=; '
                   'KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1593012254|1593006661 '
    }
    result = requests.get(url, headers=headers)
    print('result:', result.content)
    comment_json = json.loads(result.content)
    print('comment_json:', comment_json, '\n')
    if 'error' in comment_json.keys():
        # print('error')
        return
        pass
    # comment_num = comment_json['common_counts']  # 这个包括子评论，不能用于评论的分页
    # try:
    #     # 有些回答没有评论，执行这一行就会报错
    #     comment_num = comment_json['common_counts']  # 这个包括子评论，不能用于评论的分页
    #     pass
    # except Exception:
    #     return
    #     pass

    # comment_paging_is_end = comment_json['paging']['is_end']  # 是不是最后一页
    pass




if __name__ == '__main__':
    # url = 'https://www.zhihu.com/question/357824038/answer/997190122'
    # url = 'https://www.zhihu.com/api/v4/answers/997190122'
    # url = 'https://www.zhihu.com/api/v4/answers/997190122/root_comments?order=normal&limit=20&offset=20&status=open'
    # answer_num = '1203841586'
    get_chat()
