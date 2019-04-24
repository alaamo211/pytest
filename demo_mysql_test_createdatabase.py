ww# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:49:19 2019

@author: ShenR
"""

import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "password"
        )

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE runoob_db")
