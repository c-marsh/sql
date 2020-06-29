import os
# import date time
import datetime
import pymysql

# get username
username = os.getenv('C9_USER')

# connect
connection = pymysql.connect(host='localhost', user=username,
                             password="", db="Chinook")

try:
    with connection.cursor() as cursor:
        cursor.execute("Update Friends SET age = %s WHERE name = %s;", (59, 'ainsley'))
        connection.commit()
finally:
    connection.close()
