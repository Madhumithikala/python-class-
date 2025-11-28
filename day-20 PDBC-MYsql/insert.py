import mysql.connector
dbcon=None 
cursor=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='db4') 
    print(dbcon.is_connected())
    cursor=dbcon.cursor()
    sql_st='''
           insert into employees (eid,ename,email,city) values(%s,%s,%s,%s);
           '''
    employees=[
        (102,"sahul","sa@gmail.com","wayanad"),
        (103,"madhu","madhu@gmail.com","hyderabad"),
        (104,"balaji","balaji@gmail.com","new delhi"),
        (105,"gnaana","gnana@gmail.com","Bengalore")
    ]
        
    cursor.executemany(sql_st,employees)
    dbcon.commit()
    print("Data Inserted Successfully!")
except mysql.connector.Error as err:
    print(err)
finally:
    cursor.close()
    dbcon.close()