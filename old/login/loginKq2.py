from pyquery import PyQuery as pq
# from lxml import etree
# import urllib

# import os

# 下面3行是python2为了设置默认utf-8编码
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''

# d = pq("<html></html>")
# d = pq(etree.fromstring("<html></html>"))
# d = pq(url='http://google.com/')
# d = pq(url='http://google.com/', opener=lambda url, **kw: urllib.urlopen(url).read())
# d = pq(filename=path_to_html_file)
# d = pq(url='https://www.renrendai.com/')

d = pq(url='http://192.168.200.248:8080/accounts/login/')
# content = d('[class="uplan"]')
# content = d('[class="uplan-list"]').find('li').each(lambda e:print('\n\n',e))
# content = d('[class="uplan-list"]')

'''
for i in content.items('li'):
	print(i.html())
'''

# 写xml文件
# out_file = open(r'F:\py\lib-urllib2\output.txt', 'w', encoding='utf-8')  # 需要有 “encoding=”
out_file = open(r'F:\py\lib-svn\outputSvn.txt', 'w', encoding='utf-8')
out_file.write(d.html())
# out_file.write(d.html())




