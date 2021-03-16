import sqlite3

db_connection = sqlite3.connect("flaskprojectdemo.db")#flaskproject.db ==> database name

print("Connected to Database")

db_cursor = db_connection.cursor()

db_cursor.execute(" create table registeruser(id integer primary key autoincrement,name text not null,gender text not null,email text unique not null,mobile text unique not null,password text not null) ")
db_connection.commit()#it is optional

print("Table is Created Successfully")

db_cursor.close()