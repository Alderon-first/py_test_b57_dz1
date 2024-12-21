import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("SELECT id, firstname, lastname FROM addressbook")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
