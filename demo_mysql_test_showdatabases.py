# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:52:27 2019

@author: ShenR
"""

import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "password"
        )

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)