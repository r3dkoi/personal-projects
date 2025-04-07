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
             INSERT INTO `storage_locations` (`LocationID`, `Location_Name`, `Department`, `Department_Contact_Information`, `Opening Hours`)
             VALUES
                (2459273000, "Central Sterile Stores", "Sterile Services", 6345, "24/7"),
                (1663742000, "Cardiac Catheterisation Laboratory", "CCL", 9961, "0800-1800"),
                (784631548, "Consumables Store", "Main Theatres", 4591, "0600-2100");
               """)
conn.commit()
conn.close()  # closes my  connection when done


