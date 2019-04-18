# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:32:56 2019

@author: ShenR
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value 
      
        