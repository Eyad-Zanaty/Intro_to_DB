import mysql.connector
mydb= mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "012303210eyadzanaty",
    )
mycursor = mydb.cursor()
try:
    mycursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store;')
except Exception as e:
    print(e)
else:
    print("Database 'alx_book_store' created successfully!")