from math import *
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="Ayirus@123",database='sakila')

mycursor = mydb.cursor()

mycursor.execute("select * from student")

for i in mycursor:
    print(i)
