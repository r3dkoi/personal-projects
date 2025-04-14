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

CREATE ROLE 'Sterile Services Employee';
               GRANT SELECT ON cssd_inventory.* TO 'Sterile Services Employee';
CREATE USER '314127'@'localhost' IDENTIFIED BY 'HorsePurpleHatRunBay';
               GRANT 'Sterile Services Employee' TO '314127'@'localhost';
               SET DEFAULT ROLE 'Sterile Services Employee' FOR '314127'@'localhost';
               FLUSH PRIVILEGES;
""")
    

cursor.close()
conn.close()  # closes my connection when done




