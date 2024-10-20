import mysql.connector
try:
    mydb= mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "012303210eyadzanaty",
        database = "alx_book_store" 
    )
except Exception as e:
    print(e)
else:
    print("Database 'alx_book_store' created successfully!")