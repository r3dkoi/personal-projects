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
#Creating user accounts for privileges
#Assigning roles to users

cursor = conn.cursor() 

cursor.execute(
    """
    GRANT 'Sterile Services Employee' TO '314127'@'localhost'

    """
)
conn.commit()

# Flush privileges always to ensure changes take effect
try:
    cursor.execute("FLUSH PRIVILEGES")
    conn.commit()
    print("Successfully flushed privileges")
except mysql.connector.Error as err:
    print(f"Error flushing privileges: {err}")

cursor.close()
conn.close()  # closes my connection when done




