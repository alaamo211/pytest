# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:09:24 2019

@author: ShenR
"""

import re
test= '_'
if re.match('[0-9a-zA-Z\_]',test):
    print('ok')
else:
    print('failed')
    