import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 
cursor = conn.cursor() 

# Creating Product_Inventory Table 

#Don't forget to add the foreign keys to the inventory table once the Product and Location tables are created
# FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
# FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
# FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) in instruments inventory table
cursor.execute("""
             ALTER TABLE `Instrument Inventory` 
                ADD COLUMN `ShelfLife` TEXT AFTER `Class`;
            
             """)
conn.commit()
conn.close()  # closes my  connection when done


