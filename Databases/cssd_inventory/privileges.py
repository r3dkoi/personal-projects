import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='cssd_inventory'  # must match the name you created in phpMyAdmin 
) 

#Adding privileges to roles

cursor = conn.cursor() 

cursor.execute()
conn.commit()

cursor.close()
conn.close()  # closes my connection when done


