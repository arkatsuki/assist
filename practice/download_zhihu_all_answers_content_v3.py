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
        # ,'authority': 'www.zhihu.com',
        # # 'referer' : 'https://www.zhihu.com/question/300415423',
        # 'cookie' : 'SESSIONID=drP1XPI8adCHcZrFwRupYCVzUUAwC3GvyRHec3XHuz0; '
        #            'JOID=W1wdBkoYOjnn9SOmPBRP5FnaLewsNhUXwN4NiRIzFBbJ0giIEz2n97XwIqc1TGrZFJOAS5k1wK-v0bVMl8msTaQ=; '
        #            'osd=VFkSAU8XPzbg8CyjMxNK61zVKukjMxoQxdEIhhU2GxPG1Q2HFjKg8rr1LaAwQ2_WE5aPTpYyxaCq3rJJmMyjSqE=; '
        #            'BAIDU_SSP_lcr=https://www.baidu.com/link?url'
        #            '=VQWAuzsBCacWhLb9wnAd0kGgWGvSgDPhRgu3O5txPDa2rjUwTy0sKB7bNUTEqoak3zjX0xcs5v_2cRTg5uINTa&wd=&eqid'
        #            '=a85ee2ee002c4f23000000025ec745a2; SESSIONID=CoUCGEJyq8xlChiyYWtTICMZO14HQTJ4iowzf4robkF; '
        #            'JOID=VVoVAkhOA-VqmRl_eUjitIbQ-TBvaCLHS74_XltpJcRIuD5ZWNR_ITKYHnx6aDTA0DlM8k6WyFYXdTw7F2xa8Gg=; '
        #            'osd=UV0VBUJKBOVtkx14eU_osIHQ_jprbyLAQbo4XlxjIcNIvzRdX9R4KzafHntwbDPA1zNI9U6RwlIQdTsxE2ta92I=; '
        #            '_zap=37a92473-e671-4bf0-94ec-68ebacdcef12; '
        #            'd_c0="AECg1FwpXRCPTr593iMS_eqQZzKJYEWy9vI=|1573909874"; _xsrf=o8GnotMOZgGFJC2HVuekmVAWkS39Nh2s; '
        #            '_ga=GA1.2.1704039401.1583584893; tst=r; '
        #            'q_c1=c129a4aa8651406a8192191a16831f20|1587977475000|1587977475000; '
        #            '_gid=GA1.2.1679089183.1589164550; '
        #            '__utmv=51854390.100-1|2=registration_date=20130620=1^3=entry_date=20130620=1; '
        #            'capsion_ticket="2|1:0|10:1589949700|14:capsion_ticket|44'
        #            ':MWEyN2RhNDg5ODg3NDNmOGIxNmQ5NjhiMTEzYzc4NGU'
        #            '=|582ea03a9dd12a612d3289815a3d28561fe6a9ca529e76ba2fcfb129014be7a8"; '
        #            'z_c0="2|1:0|10:1589949704|4:z_c0|92'
        #            ':Mi4xTF9jT0FBQUFBQUFBUUtEVVhDbGRFQ1lBQUFCZ0FsVk5DQU95WHdBM2JKYUg2dWgxVnlVSnBVbUxYalNrbDl1ZG5R'
        #            '|89a52e6e28d3b3feb36a740e934ef1661a1991eecfb05d0b631c4bcda45088bc"; '
        #            '__utma=51854390.1704039401.1583584893.1590054500.1590122202.7; __utmc=51854390; '
        #            '__utmz=51854390.1590122202.7.7.utmcsr=zhihu.com|utmccn=('
        #            'referral)|utmcmd=referral|utmcct=/question/355075920; '
        #            'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1590117735,1590117800,1590132588,1590132588; '
        #            'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1590140060; '
        #            'KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1590140101|1590136903 '
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
    file_path_prefix = 'D:\\temp\\testdir\\' + '你有哪些秘密只敢匿名说出来_' + answer_num
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
    answer_url = 'https://www.zhihu.com/question/31068506/answer/1281943955'
    # url = 'https://www.zhihu.com/api/v4/answers/997190122/root_comments?order=normal&limit=20&offset=20&status=open'
    # url = 'https://www.zhihu.com/question/375265966/answer/1135813803'
    dowmload_answers(answer_url)
