import re
import os
import configparser

from te_sth_cla import *

config = configparser.ConfigParser()
config.read('config.ini')
svn_addr = config.get('svn','svn_addr')
print('svn_addr:',svn_addr)

config.add_section("School")
config.set("School","IP","192.168.1.120")
config.set("School","Mask","255.255.255.0")
config.set("School","Gateway","192.168.1.1")
config.set("School","DNS","211.82.96.1")
config.write(open("config.ini", "w"))

