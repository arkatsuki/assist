import redis
import re

# 清空菜单权限
# r = redis.Redis(host='192.168.200.229',port=6379,db=23,password='jiufu@redis.ecs4')
r = redis.Redis(host='123.57.56.45',port=6379,db=4,password='jiufu@redis.ecs4')

# r.set('guo','shuai')
# r.delete('SS_menu')
# r.delete('shiro_cache_com.gep.web.security.SecurityRealm.authorizationCache')
# 获取所有的key，返回是一个数组，每个key是redis原始类型（大部分是byte？？？）
for key_name in r.keys():
    # key_name_str = key_name.decode('utf-8')
    # key_name_str = str(key_name)
    r.delete(key_name)


