# MySql integration with Python
```
import pymysql
con = pymysql.connect(host = 'localhost', user = 'root', password = 'arunrockstar',database = 'l')

c = con.cursor()
query  = "insert into sbank values({},'{}',{},{})".format(s,name,money,password)
c.execute(query)
conn.commit()
```
