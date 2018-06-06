import re
import os
import configparser

from te_sth_cla import *

config = configparser.ConfigParser()
config.read('config.ini')
svn_addr = config.get('svn','svn_addr')

b = svn_addr.split('/')[-2]

print('svn_addr:',b)

