import mysql.connector as ct

# setup file to create table used in various interfaces..

db = ct.connect(host="localhost", user="root", passwd="12345")
mcursor = db.cursor()

# mcursor.execute("create database hello;")
db.commit()


mydb = ct.connect(host="localhost", user="root", passwd="12345", database="hello")
mycursor = mydb.cursor()
# mycursor.execute("drop table test;")

# mycursor.execute(f"create table test (queno int primary key AUTO_INCREMENT, question varchar(300), \
# optionA varchar(100), optionB varchar(100), optionC varchar(100), \
# optionD varchar(100), ans varchar(10) );")


mycursor.execute(f'''insert into test values(null,"what is your name","Astha","Lovepreet","Ritika","Hardik","Gurpreet");''')
mydb.commit()
mycursor.execute(f''' insert into student values("Astha", 10, "MCA", 15); ''') 

#mycursor.execute("create table student(name varchar(20), rno int(10), department varchar(20), marks int(5));")

mydb.commit()

mycursor.execute("select * from student")
# mycursor.execute("describe table student;")
# mycursor.execute("drop table student;")

for i in mycursor:
    print(i)
