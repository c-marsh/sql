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
        rows = [(23, 'Charles'),
                (60, 'ainsley')]
        cursor.executemany("Update Friends SET age = %s WHERE name = %s;",
                           rows)
        connection.commit()
finally:
    connection.close()
