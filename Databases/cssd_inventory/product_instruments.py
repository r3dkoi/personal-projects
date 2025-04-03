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
# FOREIGN KEY (SupplierID) REFERENCES Supplers(SupplierID)    
cursor.execute("""
             CREATE TABLE `Instrument Inventory` (
                ProductID int AUTO_INCREMENT PRIMARY KEY,
                Name_and_Description varchar(255),
                Category varchar(255),
                Cost int,
                SupplierID int,
                SKU int,
                Sterilisation_Method varchar(255)
             );
             """)
conn.commit()
conn.close()  # closes my  connection when done


