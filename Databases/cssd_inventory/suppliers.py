import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 
cursor = conn.cursor() 

# Creating Suppliers Table

#Don't forget to add the foreign keys to the inventory table once the Product and Location tables are created
# FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
# FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
# FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) in instruments inventory table
cursor.execute("""
               INSERT INTO `suppliers` (`SupplierID`, `Supplier_Name`, `Contact_Number`, `Contact_Email`, `Address`, `Opening Hours`)
               VALUES
                  (5711, "Life Healthcare Pty Ltd", 1800-060-168, "orders@lifehealthcare.com.au", "Level 2/327 Cambridge St, Wembley WA 6014", "Monday - Friday from 8:30 AM – 5:30 PM"),
                  (4775, "Medtronic Australasia Pty Ltd", 08-6389-5600, "australia.diabetes@medtronic.com", "Medtronic Australasia Pty Ltd, Lvl 3/1060 Hay St, West Perth WA 6005", "Monday - Friday from 8:30 AM – 5:30 PM"),
                  (1761, "Abacus dx Pty Ltd", 1800-222-287, "orders@abacusdx.com", "34 Corporate Drive, Cannon Hill, QLD, 4170", "Monday - Friday from 8:30 AM - 5:00pm");
             """)
conn.commit()
conn.close()  # closes my  connection when done


