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
-- Set the encryption key
SET @encryption_key = SUBSTRING(SHA2(' T4p0(0kL*da/', 512), 1, 32);

-- Re-encrypt one EmployeeID  at a time with known values
UPDATE users 
SET EmployeeID = AES_ENCRYPT('314127', @encryption_key)
WHERE UserID = 1;  -- Choose a specific user ID

-- Test decryption on this row
SELECT 
    UserID, 
    CAST(AES_DECRYPT(EmployeeID, @encryption_key) AS CHAR CHARACTER SET utf8mb4) AS decrypted_password
FROM users
WHERE UserID = 1;
""")
    

cursor.close()
conn.close()  # closes my connection when done




