import redis
import re

# 清redis权限
# r = redis.Redis(host='192.168.200.229',port=6379,db=23,password='jiufu@redis.ecs4')
r = redis.Redis(host='123.57.56.45',port=6379,db=4,password='jiufu@redis.ecs4')
# 获取所有的key，返回是一个数组，每个key是redis原始类型（大部分是byte？？？）
for key_name in r.keys():
    key_name_str = key_name.decode('utf-8')
    # key以week/month开头
    if re.match(r'^(week|months)[\d|\D]*$', key_name_str):
        r.delete(key_name)

