# -*- coding:utf-8 -*-

import re
from distutils.log import warn as printf
import os

'''
System Idle Process              0 Services                   0         24 K
System                           4 Services                   0      2,596 K
smss.exe                       480 Services                   0        200 K
csrss.exe                      664 Services                   0      1,956 K
csrss.exe                      720 Console                    1     76,428 K
wininit.exe                    728 Services                   0        484 K
winlogon.exe                   776 Console                    1      1,688 K
services.exe                   808 Services                   0      5,820 K
lsass.exe                      836 Services                   0      6,636 K
lsm.exe                        844 Services                   0      1,736 K
svchost.exe                    940 Services                   0      4,160 K
QQPCRTP.exe                    536 Services                   0     22,740 K
svchost.exe                   1108 Services                   0      4,608 K
svchost.exe                   1208 Services                   0     13,000 K
'''

pattern = "([\w.]+(?: [\w.]+)*)\s\s+(\d+)\s(\w+)\s\s+(\d)\s\s+([\d,]+\sK)"
# 没有?:会在第二位多一个空的字符串
# 先分组。分成5组。每组进行匹配
# 第一个组有点问题
with os.popen('tasklist', 'r') as f:
    for eachLine in f:
        # printf(re.split(r'\s\s+', eachLine.strip()))
        printf(re.findall(pattern,eachLine.rstrip()))

'''
[('System Idle Process', '0', 'Services', '0', '24 K')]
[('System', '4', 'Services', '0', '2,660 K')]
[('smss.exe', '480', 'Services', '0', '200 K')]
[('csrss.exe', '664', 'Services', '0', '2,056 K')]
[('csrss.exe', '720', 'Console', '1', '79,064 K')]
[('wininit.exe', '728', 'Services', '0', '484 K')]
[('winlogon.exe', '776', 'Console', '1', '1,604 K')]
'''