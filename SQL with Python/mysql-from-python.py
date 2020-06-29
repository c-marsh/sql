import os
import pymysql

# get username
username = os.getenv('C9_USER')

# connect
connection = pymysql.connect(host='localhost', user=username,
                             password="", db="Chinook")

try:
    # run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close connection for security, even if nothing returned
    connection.close()

# connect
connection = pymysql.connect(host='localhost', user=username,
                             password="", db="Chinook")


try:
    # run a query with Dictcursor which returns dictionaries
    # instead of tuples - meaning we can see colummn titles instead of Ids

    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    connection.close()
