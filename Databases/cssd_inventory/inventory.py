import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 

cursor = conn.cursor() 

# Creating Inventory Table 

#Don't forget to add the foreign keys to the table once the Product and Location tables are created
# FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
# FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)    
cursor.execute("""
               ALTER TABLE `inventory` 
               ADD FOREIGN KEY (LocationID) REFERENCES `storage_locations`(LocationID);
               """)
conn.commit()
conn.close()  # closes my  connection when done

""" 
VALUES (482038, 70, 9295860c, 150, 2025-03-06)
VALUES (485285, 5,  2ec486fc, 10, 2025-03-21)
               VALUES (485285, 100, 632ab1dc, 200, 2025-03-21)
               VALUES (307331, 15, 2ec486fc, 25, 2025-02-19)
               VALUES (307331, 0,  9295860c, 8, 2025-02-19)
               VALUES (236314, 44, 632ab1dc, 120, 2025-03-16)"""


