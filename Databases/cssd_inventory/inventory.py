import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 

cursor = conn.cursor() 

#Don't forget to add the foreign keys to the table once the Product and Location tables are created
# FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
# FOREIGN KEY (LocationID) REFERENCES Locations(LocationID) 

#Update LocationID for different inventory items
updates = [
    (2459273000, 2),
    (1663742000, 3),
    (784631548, 4),
    (1663742000, 5),
    (2459273000, 6),
    (784631548, 7)
]
for location_id, inventory_id in updates:
    cursor.execute("""
               UPDATE `inventory`
               SET `LocationID` = %s
               WHERE `InventoryID` = %s;
               """, (location_id, inventory_id))
conn.commit()
conn.close()  # closes my  connection when done


