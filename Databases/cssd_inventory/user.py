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

CREATE ROLE IF NOT EXISTS 'Sterile Services Manager';
               GRANT SELECT, UPDATE, INSERT ON cssd_inventory.* TO 'Sterile Services Manager';
               GRANT SELECT, UPDATE, INSERT ON cssd_users.* TO 'Sterile Services Manager';
CREATE USER '19878'@'localhost' IDENTIFIED BY 'Mdwb@Shi1984';
               GRANT 'Sterile Services Manager' TO '19878'@'localhost';
               SET DEFAULT ROLE 'Sterile Services Manager' FOR '19878'@'localhost';
               FLUSH PRIVILEGES;
""")
    

cursor.close()
conn.close()  # closes my connection when done




