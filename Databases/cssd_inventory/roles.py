import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 

cursor = conn.cursor() 

# Execute GRANT statements one at a time
grants = [
    "GRANT SELECT, INSERT, UPDATE, DELETE ON cssd_inventory.`inventory` TO `Inventory Administrator`",
    "GRANT SELECT, INSERT, UPDATE, DELETE ON cssd_inventory.`instrument inventory` TO `Inventory Administrator`",
    "GRANT SELECT, INSERT, UPDATE, DELETE ON cssd_inventory.`storage_locations` TO `Inventory Administrator`",
    "GRANT SELECT, INSERT, UPDATE, DELETE ON cssd_inventory.`suppliers` TO `Inventory Administrator`",
    "GRANT SELECT, INSERT, UPDATE, DELETE ON cssd_inventory.`users` TO `Sterile Services Manager`"
    
]

for grant in grants:
    try:
        cursor.execute(grant)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error executing {grant}: {err}")

cursor.close()
conn.close()  # closes my connection when done


