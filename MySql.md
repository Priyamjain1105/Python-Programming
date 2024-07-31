# MySql integration with Python

#Beginning
## Steps to download
1. Go to website
2. depending upon your operating system download the compatible version
3. click on `no just start my download`

## Setup
1. Setup Type: `custom`

2. Select Product:
   - MySql server
   - MySql Shell 
   - Workbench

3. Downloading will be completed

4. Type and networking (under connectivity protocol)
   - TCP/IP
   - open windonw firewall port

5. Account and Roles
   - choose your password

6. Configuration
  - check all the things and finish

```python
import pymysql
con = pymysql.connect(host = 'localhost', user = 'root', password = 'arunrockstar',database = 'l')

c = con.cursor()
query  = "insert into sbank values({},'{}',{},{})".format(s,name,money,password)
c.execute(query)
conn.commit()
```
