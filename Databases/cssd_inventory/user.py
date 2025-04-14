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
SET @encryption_key = SUBSTRING(SHA2('T4p0(0kL*da/', 512), 1, 32);
UPDATE users SET EmployeeID = AES_ENCRYPT(EmployeeID, @encryption_key);
               
""")
    

cursor.close()
conn.close()  # closes my connection when done




