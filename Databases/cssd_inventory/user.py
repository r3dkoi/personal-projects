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
cursor.execute("""CREATE TABLE `users` (
               `UserID` INT PRIMARY KEY AUTO_INCREMENT,
               `EmployeeID` INT NOT NULL,
               `RoleID` INT NOT NULL, 
               `Password` TEXT NOT NULL,
               `FullName` VARCHAR(50) NOT NULL,
               `Department` VARCHAR(50) NOT NULL,
               `LastLogin` DATETIME NOT NULL,
               `AccountStatus` TEXT NOT NULL
               )""")
conn.commit()
conn.close()  # closes my  connection when done


