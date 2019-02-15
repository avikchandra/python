import sqlite3

# establishing database connection
con = sqlite3.connect('E:\\LEARNING FOLDER\\Python Advanced\TEST.db')

# preparing cursor object
cursor = con.cursor()

# preparing sql statements
sql1 = 'drop table if exists employee'

sql2 = '''
create table employee (
    empid int(6) not null,
    name char(20) not null, 
    age int,
    sex char(1),
    income float
)
'''

# Preparing insert statement
rec = (456789,'Frodo',45,'M',100000)
records = [
    (123456, 'John', 25, 'M', 50000.00),
    (234651, 'Juli', 35, 'F', 75000.00),
    (345121, 'Fred', 48, 'M', 125000.00),
    (562412, 'Rosy', 28, 'F', 52000.00)
]
sql3 = '''
insert into employee values (?,?,?,?,?)

'''

# executing sql statements 
cursor.execute(sql1)
cursor.execute(sql2)


# executing sql statements in try except blocks
try:
    cursor.execute(sql3, rec)
    cursor.executemany(sql3, records)
    con.commit()
except Exception as e:
    print("Error message: ",str(e))
    con.rollback()

try:
    cursor.execute('select * from employees')
    recs=cursor.fetchall()
    for rec in recs:
        print(rec)
except Exception as e:
    print("Error in fetching: ",str(e))

# closing the connection
con.close()
