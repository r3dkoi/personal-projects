import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 

cursor = conn.cursor() 

# Adding a new column to the Inventory Table
cursor.execute("""
               ALTER TABLE `inventory`
               ADD COLUMN ProductName VARCHAR(255) AFTER MinimumStockLevel
               """)

# Creating Inventory Table 

#Don't forget to add the foreign keys to the table once the Product and Location tables are created
# FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
# FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)    
cursor.execute("""
               INSERT INTO `inventory` (MinimumStockLevel, QuantityAvailable, LastRestockDate)
               VALUES (44, 120, '2025-03-16')
               """)
conn.commit()
conn.close()  # closes my  connection when done


