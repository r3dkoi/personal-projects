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
cursor.execute("""
               
               """)
conn.commit()
conn.close()  # closes my  connection when done


