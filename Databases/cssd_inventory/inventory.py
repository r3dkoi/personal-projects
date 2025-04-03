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
             CREATE TABLE `inventory` (
            InventoryID int AUTO_INCREMENT PRIMARY KEY,
            ProductID int,
            LocationID int,
            QuantityAvailable int,
            MinimumStockLevel int,
            LastRestockDate datetime,
            ExpiryDate date
);
               """)
conn.commit()
conn.close()  # Always close your connection when done
