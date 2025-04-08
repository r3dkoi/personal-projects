import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 
#Table for user roles


cursor = conn.cursor() 
cursor.execute("""CREATE TABLE `roles`(
               `RoleID` INT(11) PRIMARY KEY AUTO_INCREMENT,
               `RoleName` VARCHAR(50) NOT NULL,
               `Description` TEXT NOT NULL,
               `ActiveStatus` BOOLEAN NOT NULL DEFAULT 1
               )""")
conn.commit()
conn.close()  # closes my  connection when done


