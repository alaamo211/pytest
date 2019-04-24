# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:54:18 2019

@author: ShenR
"""

import mysql.connector
 
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="runoob_db"
    )
mycursor = mydb.cursor()
 
mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")