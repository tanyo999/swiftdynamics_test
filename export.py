import csv
import mysql.connector as m
c = None
try:
    c = m.connect(host='localhost', user='root', passwd='', db='employee')
    cur = c.cursor()    
    cur.execute('SET NAMES utf8;')
    
    
    sql = "SELECT Employee.id,Employee.name,Employee.division,Position.name AS PositionName, Salary.salary FROM Employee JOIN Position ON Employee.position = Position.id JOIN Salary ON Employee.id = Salary.id ORDER BY Employee.id "
    sql = sql.encode('utf-8')
    try:
        print(sql)
        cur.execute(sql)
        myresult = cur.fetchall()
        print(myresult)
        with open("emp.csv","w") as file:
            writer=csv.writer(file)
#           myresult = [list(row) for row in myresult]
            writer.writerows(myresult)
#            for row in myresult:
#                writer.writerow(row)
        print('Success')
    except:
          
        print('Error')
    
except m.Error:
    print('Can not Connect database')

if c:
    c.close()