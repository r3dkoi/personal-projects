import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='Fu3c0c0Sk3l3d1rge',  # my XAMPP root password
    database='cssd_users'  # must match the name you created in phpMyAdmin 
) 
#Table for users
#Don't forget to add foreign key to RoleID to reference RoleID in roles table
#Creating user accounts for privileges
#Assigning roles to users

cursor = conn.cursor() 

cursor.execute("""

CREATE ROLE IF NOT EXISTS 'Inventory Administrator';
               GRANT SELECT, UPDATE, INSERT, CREATE, ALTER, DROP, CREATE ROUTINE ON cssd_inventory.* TO 'Inventory Administrator';
CREATE USER '49201'@'localhost' IDENTIFIED BY 'IoaVW,wa52p';
               GRANT 'Inventory Administrator' TO '49201'@'localhost';
               SET DEFAULT ROLE 'Inventory Administrator' FOR '49201'@'localhost';
               FLUSH PRIVILEGES;
""")
    

cursor.close()
conn.close()  # closes my connection when done




