import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 

cursor = conn.cursor() 

# List of roles to manage privileges for
roles = [
    "Sterile Services Employee"
]

# List of privileges to grant
privileges = ['SHOW VIEW', 'SELECT']

for role in roles:
    for privilege in privileges:
        try:
            cursor.execute(f"GRANT {privilege} ON cssd_inventory.* TO `{role}`@'localhost'")
            conn.commit()
            print(f"Successfully granted {privilege} to {role}")
        except mysql.connector.Error as err:
            print(f"Error granting {privilege} to {role}: {err}")

# Grant SHOW DATABASES privilege (global privilege)
for role in roles:
    try:
        cursor.execute(f"GRANT SHOW DATABASES ON *.* TO `{role}`@'localhost'")
        conn.commit()
        print(f"Successfully granted SHOW DATABASES to {role}")
    except mysql.connector.Error as err:
        print(f"Error granting SHOW DATABASES to {role}: {err}")

# Flush privileges to ensure changes take effect
try:
    cursor.execute("FLUSH PRIVILEGES")
    conn.commit()
    print("Successfully flushed privileges")
except mysql.connector.Error as err:
    print(f"Error flushing privileges: {err}")

cursor.close()
conn.close()  # closes my connection when done