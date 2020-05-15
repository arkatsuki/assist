import re
import requests
# from BeautifulSoup4 import *
# import BeautifulSoup4
from bs4 import BeautifulSoup
# from lxml import html
import os
from practice.download_zhihu_all_answers_html_comment import get_zhihu_comments


def dowmload_answers(answer_url):
    """
    缺点：有些答案，返回的是登录页面。所以，后续要考虑增加登录功能
    :param html:
    :return:
    """
    headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    result = requests.get(answer_url, headers=headers)
    # print('html:', html, '\n')
    html = result.content

    # html.replace('<br>', '\n').replace('<br/>', '\n')   # 会报错a bytes-like object is required, not 'str'
    # soup = BeautifulSoup(html, fromEncoding='utf-8')
    soup = BeautifulSoup(html, fromEncoding='gb18030') # 取标签内的汉字时，避免乱码
    # soup = BeautifulSoup(html, 'lxml')
    i = 0
    # 从url中截取答案的编号
    begin = answer_url.rfind('/')
    answer_num = answer_url[begin+1:]
    # print('编号：', answer_num)

    # 如果文件已经存在，先删除
    file_path_prefix = 'D:\\temp\\testdir\\' + '20岁的自己发现自己46岁的妈妈出轨了怎么办_' + answer_num
    i = i + 1
    file_path = file_path_prefix + '_' + '{0:0>4}'.format(str(i)) +'.txt'
    if os.path.exists(file_path):
        os.remove(file_path)
        pass
    with open(file_path, 'a+', encoding='gb18030') as fp_content:
        fp_content.write('\n\n\n' + answer_url)
        fp_content.write('\n\n\n')

        # for box in soup.findAll('div', class_='RichContent RichContent--unescapable'):
        for box in soup.findAll('div', class_='RichContent RichContent--unescapable'):
            print('box:', box, '\n')

            # b = str(b).replace('<br>', '\n').replace('<br/>', '\n') # 这样做后续就没法get_text()了
            txt = box.get_text('\n', 'br')  # 把<br>标签替换成换行
            # txt = b.get_text()
            print('txt:', txt)

            fp_content.write(txt)
            fp_content.write('\n')

            for a in box.findAll('img'):
                # src = a.get('src')
                src = a.get('src')
                if src is not None:
                    print('src:', src, '\n')
                    try:
                        pic = requests.get(src, timeout=60)
                        # '{0:0>4}'.format(1) 第二个0表示前面补0, 4表示一共4位，'>'表示右对齐，'<'表示左对齐。
                        # dir = file_path + '{0:0>4}'.format(str(++i)) + '.' + src[src.rfind(
                        #     '.') + 1:]
                        i = i + 1
                        dir = file_path_prefix + '_' + '{0:0>4}'.format(str(i)) + '.' + src[src.rfind(
                            '.') + 1:]
                        print("dir:", dir)

                        fp = open(dir, 'wb')
                        fp.write(pic.content)
                        fp.close()
                        print('download end')
                    # except requests.exceptions.ConnectionError:
                    except Exception:
                        print('【错误】当前图片无法下载')
                        pass
                    with open('D:\\temp\\testdir\\pic_src.txt', 'a+') as fp_pic_src:
                        fp_pic_src.write(src + '\n')
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

    print('i:', i)


if __name__ == '__main__':
    # url = 'https://www.zhihu.com/question/385655582/answer/1164227477'
    answer_url = 'https://www.zhihu.com/question/319637812/answer/844124334'
    # url = 'https://www.zhihu.com/api/v4/answers/997190122/root_comments?order=normal&limit=20&offset=20&status=open'
    # url = 'https://www.zhihu.com/question/375265966/answer/1135813803'
    dowmload_answers(answer_url)
