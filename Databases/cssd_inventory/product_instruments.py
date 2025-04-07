import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 
cursor = conn.cursor() 



#Don't forget to add the foreign keys to the inventory table once the Product and Location tables are created
# FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
# FOREIGN KEY (LocationID) REFERENCES Locations(LocationID)
# FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) in instruments inventory table

#Updating Supplier ID in product_instruments table
updates = [
    (1761, 236314),
    (4775, 307331),
    (5711, 482038),
    (5711, 485285)
]

for supplier_id, product_id in updates:
    cursor.execute("""
               UPDATE `instrument inventory`
               SET `SupplierID` = %s
               WHERE `ProductID` = %s;
               """, (supplier_id, product_id))
conn.commit()
conn.close()  # closes my  connection when done


