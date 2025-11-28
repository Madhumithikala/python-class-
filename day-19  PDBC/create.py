import mysql.connector

dbcon = None
cursor = None

try:
    dbcon = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db5'
    )

    cursor = dbcon.cursor()

    # Create table 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user(
            uid INT,
            uname VARCHAR(32),
            usal float
        );
    ''')
    sql_st = "INSERT INTO user   VALUES (%s,%s,%s)"

    # Data to insert
    name = [
        (105, "madhu", 12.00),
        (104, "sai",13.00),
        (103, "srinithi",24.00),
        (102, "chandu",56.00),
        (101, "gnana",34.00)
    ]

    #  executemany() takes SQL + list of tuples
    cursor.executemany(sql_st,name)
    dbcon.commit()

    print(' New MySQL table created and data inserted successfully!')

except mysql.connector.Error as err:
    print(" Error:", err)

finally:
        cursor.close()
        dbcon.close()
