import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 
cursor = conn.cursor() 

# Creating Storage_Locations Table 

#Don't forget to add the foreign keys to the table once the Product and Location tables are created
# FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
# FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
# FOREIGN KEY (SupplierID) REFERENCES Supplers(SupplierID)    
cursor.execute("""
             CREATE TABLE `storage_locations` (
                LocationID int AUTO_INCREMENT PRIMARY KEY,
                Location_Name varchar(255),
                Department varchar(255),
                Department_Contact_Information varchar(255)
             );
             """)
conn.commit()
conn.close()  # closes my  connection when done


