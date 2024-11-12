import pyodbc as odbc
import csv

#def Excercise1(SQLcommandtorun):

conn_str = (
        r'Driver=SQL Server;' +
        r'Server=DESKTOP-PKEQGVU\MSSQLSERVERAJS;' +
        r'Database=NYCTaxi;' +
        r'Trusted_Connection=yes;'
    )

conn = odbc.connect(conn_str)

with conn.cursor() as cursor:
    sql = "SELECT * FROM Employee"
    cursor.execute(sql)

    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    c = csv.writer(open("temp.csv","w"))
    c.writerows(rows)


    #Excercise1("Select * From Employee")