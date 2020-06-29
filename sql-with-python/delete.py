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
        cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        connection.commit()
finally:
    connection.close()
