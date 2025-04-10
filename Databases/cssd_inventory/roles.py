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

#List of roles to grant privileges to
roles = [
    '`Sterile Services Manager`',
    '`Sterile Services Team Leader`',
    '`Sterile Services Employee`',
    '`Inventory Administrator`'
]

#Granting privileges to roles
for role in roles:
    for privilege in privileges:
        grant_sql_privileges = f"GRANT {privilege} ON cssd_inventory.* TO '{role}'@`localhost`"
        cursor.execute(grant_sql_privileges)
        conn.commit()
cursor.close()
conn.close()  # closes my connection when done


