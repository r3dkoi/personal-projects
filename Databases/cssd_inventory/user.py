import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 
#Table for users
#Don't forget to add foreign key to RoleID to reference RoleID in roles table

cursor = conn.cursor() 
cursor.execute("""
               INSERT INTO `users`(`EmployeeID`, `RoleID`, `Password`, `FullName`, `Department`, `LastLogin`, `AccountStatus`)
               VALUES
               (314127, 3, "HorsePurpleHatRunBay", "Simon Sandler", "CSSD", "26-10-24 02:00:00", "Inactive"),
               (19878, 1, "Mdwb@Shi1984", "Nick Maui", "CSSD", "26-10-24 02:00:00", "Active"),
               (99102, 1, "Children+Xmas=Excitement", "Susie Wellbram", "CSSD", "25-01-25 03:00:05", "Active"),
               (49201, 4, "IoaVW,wa52p", "Adam Sakier", "Supply Stores", "25-00-25 01:00:05", "Active")
               """)
conn.commit()
conn.close()  # closes my  connection when done


