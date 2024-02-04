import sqlite3

# Connect to the database
conn = sqlite3.connect('student.db')

# Create a cursor object for CRUD
cursor = conn.cursor()

# Create a table
table_info="""
Create table STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""

cursor.execute(table_info)
# Insert 5 Students data into the table
cursor.execute("INSERT INTO STUDENT VALUES('Amit','X','A',90);")
cursor.execute("INSERT INTO STUDENT VALUES('Rohit', 'XI', 'A', 100);")
cursor.execute("INSERT INTO STUDENT VALUES('Atul', 'XII', 'B', 86);")
cursor.execute("INSERT INTO STUDENT VALUES('Ankit', 'IX', 'C', 50);")
cursor.execute("INSERT INTO STUDENT VALUES('Hariom', 'X', 'B', 35);")

# Display all the data in the table
print("All the data in the table:")
data=cursor.execute("SELECT * FROM STUDENT;")

for row in data:
    print(row)
    
# Close the connection
conn.commit()
conn.close()
