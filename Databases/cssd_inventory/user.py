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
               ALTER TABLE `users`
               ADD FOREIGN KEY (`RoleID`) REFERENCES `roles`(`RoleID`)
               """)
conn.commit()
conn.close()  # closes my  connection when done


