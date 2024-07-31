# MySql integration with Python

#Beginning
## Steps to download
1. Go to website
2. depending upon your operating system download the compatible version
3. click on `no just start my download`

## Setup
1. setup type: `custom`
2. select product:
   - MySql server
   - MySql Shell 
   - Workbench
3. Downloading will be completed

```python
import pymysql
con = pymysql.connect(host = 'localhost', user = 'root', password = 'arunrockstar',database = 'l')

c = con.cursor()
query  = "insert into sbank values({},'{}',{},{})".format(s,name,money,password)
c.execute(query)
conn.commit()
```
