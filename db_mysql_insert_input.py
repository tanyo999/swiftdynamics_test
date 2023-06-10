
import mysql.connector as m
c = None
try:
    c = m.connect(host='localhost', user='root', passwd='', db='employee')
    cur = c.cursor()    
    cur.execute('SET NAMES utf8;')
    loop = 1;
    while loop==1:
        name = input('Name: ')
        division = input('Division: ')
        position = input('Position: ')
        if name=='exit' or division=='exit' or position=='exit':
            loop = 0
            continue
        
        sql = f"INSERT INTO `employee` ( `name` , `division`, `position` ) VALUE ( '{name} ','{division}', '{position}') ;" 
        sql = sql.encode('utf-8')
        try:
            print(sql)
            cur.execute(sql)
            c.commit()
            print('Success')
        except:
            c.rollback()
            print('Error')
    
except m.Error:
    print('Can not Connect database')

if c:
    c.close()