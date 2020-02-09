# (c) 2020 Keker LLC

import mysql.connector
import time
import os

cnx = mysql.connector.connect(user='max', password='Hunter2', host='192.168.2.87', database='plexSleepTimer')
mycursor = cnx.cursor()

mycursor.execute("SELECT * FROM users")

myresult = list(mycursor.fetchall())

currentUser = myresult[0][0]
minute = type(int(myresult[0][1]))

for x in minute:
    mycursor.execute("UPDATE users SET minuteValue='" + minute - 1 + "' WHERE user='" + currentUser + "'")
    time.sleep(60)
    
os.system("kill_a_stream.py -u" + currentUser)

