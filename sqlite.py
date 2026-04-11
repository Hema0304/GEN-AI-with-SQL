import sqlite3


##connect to squlite
connection=sqlite3.connect("student.db")

#create cursor object to insert record,create table
cursor=connection.cursor()

cursor.execute("DROP TABLE IF EXISTS STUDENT")


#create table 
table_info = """
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR (25),
SECTION VARCHAR(25), MARKS INT)
"""
cursor.execute(table_info)

#insert records
cursor.execute(''' Insert Into STUDENT values('Hema','Data Science','A',90)''')
cursor.execute(''' Insert Into STUDENT values('Harini','Data Science','A',95)''')
cursor.execute(''' Insert Into STUDENT values('Mukesh','Data Science','A',90)''')
cursor.execute(''' Insert Into STUDENT values('Joe','DEVOPS','B',86)''')
cursor.execute(''' Insert Into STUDENT values('Jon','DEVEOPS','B',80)''')

#display records
print("the inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data :
    print(row)
    
#commit changes in database
connection.commit()
connection.close()