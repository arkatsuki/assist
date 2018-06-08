import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import time
import json

# 获取当前时间，并改成当月1号
current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
begin_date = current_date[:len(current_date)-2] + '01'
print(current_date)

# LOGIN_URL = 'http://192.168.200.248:8080//selfservice/login/'
LOGIN_URL = "http://192.168.200.248:8080/accounts/login/"
values = {'username': 'js', 'password': '999999'} # , 'submit' : 'Login'
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
    page = response.read().decode()
    print(page)
except urllib.error.URLError as e:
    print(e.code, ':', e.reason)

cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
print(cookie)
for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)

# get_url = r'http://192.168.200.248:8080/data/worktable/'  # 利用cookie请求访问另一个网址
# # get_request = urllib.request.Request(get_url, headers=headers)
# get_request = urllib.request.Request(get_url)
# get_response = opener.open(get_request)
# # print(get_response.read().decode())
# f = open(r'F:\py\lib-svn\outputSvn.txt', 'w', encoding='utf-8')
# f.write(get_response.read().decode())  # write的参数需要是字符串，不能是List

static_detail_url = r'http://192.168.200.248:8080/grid/att/RecAbnormite/'
search_params = {'page': '1',
                 'rp': '20',
'sortname':'undefined',
'sortorder':'undefined',
'query':'',
'qtype':'',
                 'emp_dept_all':'on',
                 'ComeTime':begin_date,
'deptIDs':'15',
'DeptIDs':'',
'deptIDschecked_child':'on',
'multipleFieldName':'emp',
'UserIDs':'1432',
'isForce':'0',
'emp':'1432',
'dept_child':'0',
'EndTime':current_date,
'change_search':'d,e,f'
                 }
post_search_params = urllib.parse.urlencode(search_params).encode()
request = urllib.request.Request(static_detail_url, post_search_params)
response = opener.open(request)
json_obj = json.loads(response.read().decode())   # 这里是转换成了dict
# 遍历dict，同时遍历key和value
for k,v in json_obj.items():
    print('k:',k, 'v:',v)

rows_data = json_obj['rows']     # 是个list
row_num = len(rows_data)    # 行数。因为url的分页参数是20，所以最多是20，不到20的话是最后一页

# 保存输出信息
out_text = []

# 遍历，获取每一行信息
for row in rows_data:
    # print('name:',row['name'], 'NewType:',row['NewType'], 'checktime:',row['checktime'])
    out_line = row['name'] + '\t' + row['NewType'] + '\t' + row['checktime'] + '\t'
    out_text.append(out_line)

f = open(r'F:\py\lib-svn\outputSvn.txt', 'w', encoding='utf-8')
f.write('\n'.join(out_text))  # write的参数需要是字符串，不能是List

# print(type(rows_data))
# f = open(r'F:\py\lib-svn\outputSvn.txt', 'w', encoding='utf-8')
# f.write(response.read().decode())  # write的参数需要是字符串，不能是List
