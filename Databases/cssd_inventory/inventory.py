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

# Update ProductID for different inventory items
updates = [
    (485285, 3),
    (485285, 4),
    (307331, 5),
    (307331, 6),
    (236314, 7)
]

for product_id, inventory_id in updates:
    cursor.execute("""
        UPDATE `inventory`
        SET `ProductID` = %s
        WHERE `InventoryID` = %s
    """, (product_id, inventory_id))
    conn.commit()

conn.close()  # closes my connection when done


