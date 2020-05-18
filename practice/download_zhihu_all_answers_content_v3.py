import re
import requests
# from BeautifulSoup4 import *
# import BeautifulSoup4
from bs4 import BeautifulSoup
# from lxml import html
import os
from practice.download_zhihu_all_answers_comment_v3 import get_zhihu_comments


def dowmload_answers(answer_url):
    """
    缺点：有些答案，返回的是登录页面。所以，后续要考虑增加登录功能
    :param html:
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        ,'authority': 'www.zhihu.com',
        # 'referer' : 'https://www.zhihu.com/question/300415423',
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
    # print('answer_url', answer_url)
    result = requests.get(answer_url, headers=headers)
    html = result.content
    # print('html:', html, '\n')
    # html.replace('<br>', '\n').replace('<br/>', '\n')   # 会报错a bytes-like object is required, not 'str'
    # soup = BeautifulSoup(html, fromEncoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser', fromEncoding='gb18030') # 取标签内的汉字时，避免乱码
    # soup = BeautifulSoup(html, 'lxml')

    # print('prettify', soup.prettify())
    i = 0
    # 从url中截取答案的编号
    begin = answer_url.rfind('/')
    answer_num = answer_url[begin+1:]
    # print('编号：', answer_num)

    # 如果文件已经存在，先删除
    file_path_prefix = 'D:\\temp\\testdir\\' + '舔狗到底有多卑微_' + answer_num
    # file_path_prefix = 'D:\\temp\\testdir\\' + '你喜欢的人和别人发生了关系你有什么感受_' + answer_num
    # file_path_prefix = 'D:\\temp\\testdir\\' + '发现自己舔的女神是别人的舔狗是种怎样的体验_' + answer_num
    i = i + 1
    file_path = file_path_prefix + '_' + '{0:0>4}'.format(str(i)) +'.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
        pass
    with open(file_path, 'a+', encoding='gb18030') as fp_content:
        fp_content.write('\n\n\n' + answer_url)
        fp_content.write('\n\n\n')

        for box in soup.findAll('div', class_='RichContent RichContent--unescapable'):
            # print('box:', box, '\n')

            # b = str(b).replace('<br>', '\n').replace('<br/>', '\n') # 这样做后续就没法get_text()了
            txt = box.get_text('\n', 'br')  # 把<br>标签替换成换行
            # txt = b.get_text()
            # print('txt:', txt)

            fp_content.write(txt)
            fp_content.write('\n')

            with open('D:\\temp\\testdir\\pic_src.txt', 'a+') as fp_pic_src:
                for a in box.findAll('img'):
                    # src = a.get('src')
                    src = a.get('src')
                    if src is not None and src.find('http') == 0:
                        fp_pic_src.write(answer_num + ':' + src + '\n')
                        # print('src:', src, '\n')
                        try:
                            pic = requests.get(src, timeout=60)
                            # '{0:0>4}'.format(1) 第二个0表示前面补0, 4表示一共4位，'>'表示右对齐，'<'表示左对齐。
                            # dir = file_path + '{0:0>4}'.format(str(++i)) + '.' + src[src.rfind(
                            #     '.') + 1:]
                            i = i + 1
                            dir = file_path_prefix + '_' + '{0:0>4}'.format(str(i)) + '.' + src[src.rfind(
                                '.') + 1:]
                            # print("dir:", dir)

                            fp = open(dir, 'wb')
                            # print('pic.status_code:', pic.status_code)
                            pic_len = len(pic.content)
                            # print('len(pic.content)：', pic_len)
                            # 单位是字节，所以小于1k的应该都是空文件
                            if pic_len <= 1000:
                                with open('D:\\temp\\testdir\\pic_src_fail_size0.txt', 'a+') as fp_pic_src_fail_size0:
                                    fp_pic_src_fail_size0.write(answer_num + ':' + src + ':' + dir + '\n')
                                    pass
                                pass
                            fp.write(pic.content)
                            fp.close()
                            # print('download end')
                        # except requests.exceptions.ConnectionError:
                        except Exception:
                            with open('D:\\temp\\testdir\\pic_src_fail.txt', 'a+') as fp_pic_src_fail:
                                fp_pic_src_fail.write(answer_num + ':' + src + '\n')
                                pass
                            print('【错误】当前图片无法下载')
                            pass

                        pass
                        pass
                    pass



                pass

            pass
        pass
    pass

    i = i + 1
    comment_file_path = file_path_prefix + '_' + '{0:0>4}'.format(str(i)) + '评论' + '.txt'
    get_zhihu_comments(answer_num, comment_file_path)

    # print('i:', i)


if __name__ == '__main__':
    # url = 'https://www.zhihu.com/question/385655582/answer/1164227477'
    answer_url = 'https://www.zhihu.com/question/300415423/answer/606123351'
    # url = 'https://www.zhihu.com/api/v4/answers/997190122/root_comments?order=normal&limit=20&offset=20&status=open'
    # url = 'https://www.zhihu.com/question/375265966/answer/1135813803'
    dowmload_answers(answer_url)
