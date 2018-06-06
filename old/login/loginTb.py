import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import time
import json

# LOGIN_URL = 'http://192.168.200.248:8080//selfservice/login/'
# LOGIN_URL = "https://login.tmall.com/?redirectURL=https%3A%2F%2Fwww.tmall.com%2F"
LOGIN_URL = "https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.tmall.com%2F"

values = {'TPL_username': 'sandline', 'TPL_password': r'15yre4tb.#1'} # , 'submit' : 'Login'
postdata = urllib.parse.urlencode(values).encode()
# user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
# headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

cookie_filename = r'F:\py\lib-svn\cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

# request = urllib.request.Request(LOGIN_URL, postdata, headers)
request = urllib.request.Request(LOGIN_URL, postdata)
try:
    response = opener.open(request)
    # page = response.read().decode()
    # 有时候会碰到默认的utf8无法解码的字节，所以改gbk
    page = response.read().decode('gbk')
    # print(page)
except urllib.error.URLError as e:
    print(e.code, ':', e.reason)

cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
# print(cookie)
# for item in cookie:
#     print('Name = ' + item.name)
#     print('Value = ' + item.value)

# https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm?spm=a1z09.2.1997525045.2.1f30a53fTAU0Sw

list_buyed_order_url = 'https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm'
list_buyed_order_request = urllib.request.Request(list_buyed_order_url)
list_buyed_order_response = opener.open(list_buyed_order_request)
list_buyed_order_response_str = list_buyed_order_response.read().decode('gbk')
# print('list_buyed_order_response_str:',list_buyed_order_response_str)
print('type:',type(list_buyed_order_response_str))
# arr = list_buyed_order_response_str.split('\n')
list_buyed_order_response_arr = list_buyed_order_response_str.split('\n')
for html_line in list_buyed_order_response_arr:
    if html_line.strip().startswith('var data = JSON.parse'):
        print('html_line:',html_line.strip())
    pass
# print('arr[1] len',len(arr))
# print('arr[1]',arr[1])
# print('arr[2]',arr[2])
# print('arr[3]',arr[3])

# delete_order_url = 'https://buyertrade.taobao.com/trade/itemlist/asyncBought.htm?' \
#                    'action=itemlist/RecyleAction&event_submit_do_delete=1&_input_charset=utf8' \
#                    '&order_ids=replaceid&isArchive=false'

