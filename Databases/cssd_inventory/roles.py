import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 

cursor = conn.cursor() 

try:
    # Grant SHOW VIEW privilege to the role
    cursor.execute("GRANT SHOW VIEW ON cssd_inventory.* TO `Sterile Services Employee`@'localhost'")
    conn.commit()
    print("Successfully granted SHOW VIEW privilege")

except mysql.connector.Error as err:
    print(f"Error: {err}")

cursor.close()
conn.close()  # closes my connection when done


