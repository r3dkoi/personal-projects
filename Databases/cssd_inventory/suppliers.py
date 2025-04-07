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

#Updating Phone Numbers
updates = [
    ('1800-060-168', 5711),
    ('08-6389-5600', 4775),
    ('1800-222-287', 1761)
]
for phone_number, supplier_id in updates:
    cursor.execute("""
               UPDATE `suppliers`
               SET `Contact_Number` = %s
               WHERE `SupplierID` = %s;
               """, (phone_number, supplier_id))
conn.commit()
conn.close()  # closes my  connection when done


