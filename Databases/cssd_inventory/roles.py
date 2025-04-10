import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 

cursor = conn.cursor() 

#List of privileges to grant
privileges = ['SELECT']

#List of tables to grant privileges on
tables = [
    '`instrument inventory`',
    '`inventory`',
    '`storage_locations`',
    '`suppliers`'
]

#Granting privileges to roles
for table in tables: 
    for privilege in privileges:
        try:
            grant_sql_privileges = f"GRANT {privilege} ON cssd_inventory.{table} TO '`Sterile Services Employee`'@'localhost'" 
            cursor.execute(grant_sql_privileges)
            conn.commit()
            print(f"Successfully granted {privilege} on {table}")
        except mysql.connector.Error as err:
            print(f"Error granting {privilege} on {table}: {err}")
        
cursor.close()
conn.close()  # closes my connection when done


