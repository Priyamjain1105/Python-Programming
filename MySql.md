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
  
7. connect workbench
   - click + button
   - username: root
   - password: yourPassword
   - Connection will be created

# Procedure to connect with Python
1. in terminal: `pip install mysql-connector-python`
2. `import mysql.connector`
3. ```python
   mydb = mysql.connector.connect(
           host = "localhost",
           user = "root",
           password = "your-password",
           database = "<database-name>")
   ```



```python
import pymysql
con = pymysql.connect(host = 'localhost', user = 'root', password = 'arunrockstar',database = 'l')

c = con.cursor()
query  = "insert into sbank values({},'{}',{},{})".format(s,name,money,password)
c.execute(query)
conn.commit()
```
