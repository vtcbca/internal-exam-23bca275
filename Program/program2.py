Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3 as sq
... import csv
... conn=sq.connect("D:/pythonSQL/sqlite-tools-win-x64-3460000/database/emp275.db")
... cur=conn.cursor()
... cur.execute("create table if not exists emp28(eid,ename,salary)")
... <sqlite3.Cursor at 0x15de5029940>
... cur.execute("insert into emp28 values(1,'om',9000)")
... <sqlite3.Cursor at 0x15de5029940>
... cur.execute("insert into emp28 values(2,'sa',8000)")
... <sqlite3.Cursor at 0x15de5029940>
... cur.execute("insert into emp28 values(3,'ram',8000)")
... <sqlite3.Cursor at 0x15de5029940>
... cur.execute("insert into emp28 values(4,'sufiyan',16000)")
... <sqlite3.Cursor at 0x15de5029940>
... cur.execute("insert into emp28 values(5,'saif',11000)")
... <sqlite3.Cursor at 0x15de5029940>
... cur.execute("insert into emp28 values(6,'sajid',10000)")
... <sqlite3.Cursor at 0x15de5029940>
... cur.execute("insert into emp28 values(7,'adil',9500)")
... <sqlite3.Cursor at 0x15de5029940>
... cur.execute("insert into emp28 values(8,'ammar',6000)")
... <sqlite3.Cursor at 0x15de5029940>
... cur.execute("select * from emp28 where salary > 10000")
... <sqlite3.Cursor at 0x15de5029940>
... rec=cur.fetchall()
... print(rec)
... [(4, 'sufiyan', 16000), (5, 'saif', 11000)]
... f = open("D:\\pythonSQL\\sqlite-tools-win-x64-3460000\\csv\\b.csv","w")
... wo = csv.writer(f, delimiter = ',')
... wo.writerow([(4, 'sufiyan', 16000), (5, 'saif', 11000)])
... 46
