import pyodbc 
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:database-1.cf2dqu6kr5nt.ap-south-1.rds.amazonaws.com,1433' 
database = 'myProjectDB' 
username = 'admin' 
password = input('Enter the passdowrd: ') 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Creating table as per requirement
##cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
"""
# Insert the data into table
items = [(101, 'Nik D300', 'Nik D300', 'DSLR Camera', 3),
             (102, 'Can 1300', 'Can 1300', 'DSLR Camera', 5),
             (103, 'gPhone 13S', 'gPhone 13S', 'Mobile', 10),
             (104, 'Mic canvas', 'Mic canvas', 'Tab', 5),
             (105, 'SnDisk 10T', 'SnDisk 10T', 'Hard Drive', 1)
             ]
sql_insert = '''INSERT into dbo.ITEMS (item_id, item_name, item_description,item_category, quantity_in_stock) values (?,?,?,?,?)'''
cursor.executemany(sql_insert,items)
cnxn.commit()
"""
 #Add code for updating quantity_in_stock
sql_update = '''update items set quantity_in_stock = ? where item_id = ?'''
record_update = [(4,103),(2,101),(0,105)]
cursor.executemany(sql_update,record_update)
cnxn.commit()
  