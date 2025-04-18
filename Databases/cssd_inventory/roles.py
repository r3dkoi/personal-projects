import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 

cursor = conn.cursor() 
roles = [ 
    'Sterile Services Employee',
]

for role in roles:
    try:
        cursor.execute(f"CREATE ROLE IF NOT EXISTS `{role}`")
        conn.commit()
        print(f"Successfully created role: {role}")
    except mysql.connector.Error as err:
        print(f"Error creating role: {err}")

cursor.execute("FLUSH PRIVILEGES")
conn.commit()

cursor.close()
conn.close()  # closes my connection when done


