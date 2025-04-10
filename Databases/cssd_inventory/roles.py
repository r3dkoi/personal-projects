import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 

cursor = conn.cursor() 
#Creating Roles
#Assigning privileges to roles

# Execute GRANT statements one at a time
create_role = [
    "CREATE ROLE 'Sterile Services Manager'",
    "CREATE ROLE 'Sterile Services Team Leader'",
    "CREATE ROLE 'Sterile Services Employee'",
    "CREATE ROLE 'Inventory Administrator'"
]

for role in create_role:
    try:
        cursor.execute(role)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error executing {grant}: {err}")

cursor.close()
conn.close()  # closes my connection when done


