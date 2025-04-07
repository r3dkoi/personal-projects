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
             INSERT INTO `Instrument Inventory` (`ProductID`, `Name`, `Intended Purpose`, `Category`, `Cost`, `SKU`, `Sterilisation_Method`, `Class`, `ShelfLife`)
               VALUES 
                    (482038, "Gillies Dissecting Forcep", "Grasping delicate tissues with its narrow jaws providing comfortable access to deep tissues", "RMD", 34.10, 465469, "Steam", "I", "Used daily"),
                    (485285, "Disposable Gillies Dissecting Forceps", "Grasping delicate tissues with its narrow jaws providing comfortable access to deep tissues", "Single Use", 6.00, 883967, "N/A", "I", "N/A"),
                    (307331, "Pacing Leads", "Specialised conductors used in cardiac rhythm management devices to deliver electrical impulses from a pacemaker to the heart", "RMD", 597.93, 900654, "Hydrogen Peroxide", "III", "4 Years"),
                    (236314, "IVD Packs", "Combinations of products packaged together for specific diagnostic purposes", "IVD", 300.00, 945732, "None", "2", "4-6 Months");            
             """)
conn.commit()
conn.close()  # closes my  connection when done


