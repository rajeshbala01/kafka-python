import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:database-1.cf2dqu6kr5nt.ap-south-1.rds.amazonaws.com,1433' 
database = 'myProjectDB' 
username = 'admin' 
password = 'welcome123' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Creating table as per requirement
##cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Insert the data into table
sql = ('''INSERT INTO dbo.customers (name, address) VALUES (?, ?)''')
val = ("Rajesh", "Blue Village")
cursor.execute(sql, val)
cnxn.commit()

## select query to fetch the data
cursor.execute("SELECT * FROM customers")
myresult = cursor.fetchall()

for x in myresult:
  print(x)