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

# static_detail_url = r'http://192.168.200.248:8080/grid/att/RecAbnormite/'
# 汇总最早和最晚 url
first_last_url = r'http://192.168.200.248:8080/grid/att/FirstLast/'
# 异常考勤 url
abnormal_url = r'http://192.168.200.248:8080/grid/att/DayAbnormal/'

# 请求参数
# 成佳林  1609
# self 1432
# 小骥  2088
# 李利  2108
# 李芳  2981
# 秀莲  1953
user_id = 2088
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
'UserIDs':user_id,
'isForce':'0',
'emp':user_id,
'dept_child':'0',
'EndTime':current_date,
'change_search':'d,e,f'
                 }
post_search_params = urllib.parse.urlencode(search_params).encode()

# 保存输出信息
out_text = []

# 异常信息统计，数据
abnormal_request = urllib.request.Request(abnormal_url, post_search_params)
abnormal_response = opener.open(abnormal_request)
abnormal_json_obj = json.loads(abnormal_response.read().decode())   # 这里是转换成了dict
rows_data = abnormal_json_obj['rows']     # 是个list
row_num = len(rows_data)    # 行数。因为url的分页参数是20，所以最多是20，不到20的话是最后一页
# 遍历，获取每一行信息

out_line_abnormal_title = '姓名' + '\t\t' + '日期' + '\t\t' + '迟到分钟' + '\t\t'\
    + '早退分钟' + '\t\t' + '旷工时间' + '\t\t' + '迟到次数' + '\t\t'
out_text.append(out_line_abnormal_title)
for row in rows_data:
    # print('name:',row['name'], 'NewType:',row['NewType'], 'checktime:',row['checktime'])
    out_line = row['name'] + '\t\t' + row['att_date'] + '\t\t' + str(row['late']) + '\t\t'\
    + str(row['early']) + '\t\t' + str(row['absent']) + '\t\t' + str(row['late_times']) + '\t\t'
    out_text.append(out_line)

out_text.append('\n\n')
# 汇总最早和最晚，数据
first_last_request = urllib.request.Request(first_last_url, post_search_params)
first_last_response = opener.open(first_last_request)
first_last_json_obj = json.loads(first_last_response.read().decode())   # 这里是转换成了dict
# 遍历dict，同时遍历key和value
for k,v in abnormal_json_obj.items():
    print('k:',k, 'v:',v)

rows_data = first_last_json_obj['rows']     # 是个list
row_num = len(rows_data)    # 行数。因为url的分页参数是20，所以最多是20，不到20的话是最后一页

out_line_first_last_title = '姓名' + '\t\t' + '最早时间' + '\t\t' + '最晚时间' + '\t\t'\
    + '日期' + '\t'
out_text.append(out_line_first_last_title)
# 遍历，获取每一行信息
for row in rows_data:
    # print('name:',row['name'], 'NewType:',row['NewType'], 'checktime:',row['checktime'])
    out_line = row['name'] + '\t\t' + row['first'] + '\t\t' + row['last'] + '\t\t'\
    + row['card_date'] + '\t'
    out_text.append(out_line)

# f = open(r'F:\py\lib-svn\outputSvn.txt', 'w', encoding='utf-8')
with open(r'F:\py\lib-svn\outputSvn.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_text))  # write的参数需要是字符串，不能是List


