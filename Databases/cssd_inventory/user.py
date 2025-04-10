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

cursor = conn.cursor() 

# List of users to create with their passwords
users = [
    ("99102", "Children+Xmas=Excitement")
]

# Execute CREATE USER statements one at a time
for username, password in users:
    try:
        create_user_sql = f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}'"
        cursor.execute(create_user_sql)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error creating user {username}: {err}")

cursor.close()
conn.close()  # closes my connection when done


