import mysql.connector 

# Connect to the MySQL server (assuming default XAMPP settings) 
conn = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
    database='talentforge_db'  # must match the name you created in phpMyAdmin 
) 

cursor = conn.cursor() 

# Inserting data test - corrected version
cursor.execute("""
              INSERT INTO `talentforge employee records`(`ID`, `Employee ID`, `FirstName`, `LastName`, `Email`, `Company`, `Mobile Number`, `Account No.`, `BSB No.`, `Tax File No.`, `Pay Day`)
VALUES (5, 6666, "Jack", "Napier", "hahaha@hotmail.com", "TheJoker", "0492982879", "788732550", "143689", "76299362", "Friday");
               """)
conn.commit()
conn.close()  # Always close your connection when done
