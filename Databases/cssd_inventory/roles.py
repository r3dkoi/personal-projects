import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 
#Table for user roles


cursor = conn.cursor() 
cursor.execute("""
               INSERT INTO `roles`(`RoleName`, `Description`, `ActiveStatus`)
               VALUES
               ("Sterile Services Manager", "Edit instrument records. Has access to staff records, salary, hospital departments, vendors, sterilisers, washers, preparation areas, theatres", 1),
               ("Sterile Services Team Leader", "View and edit records Does not have access to staff records, other departments, theatre records. Can issue repairs and restocking inventory", 1),
               ("Sterile Services Employee", "Print barcodes and scan items,  Process and pass/fail loads, does not have access to staff records and inventory records", 1), 
               ("Inventory Administrator", "Access the inventory table records. Able to order and restock inventory.", 1),
               ("Guest", "None", 0)
               """)
conn.commit()
conn.close()  # closes my  connection when done


