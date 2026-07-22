# import mysql.connector

# connection = None
# cursor = None

# try:
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="minnie",
#         database="d15"
#     )

#     if connection.is_connected():
#         print("Connected Successfully")

#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM employees where emp_id=2;")

#     for row in cursor.fetchall():
#         print(row)

# except mysql.connector.Error as e:
#     print("Database error:", e)
#     print("Check your MySQL username, password, database name, and server status.")
# finally:
#     if cursor:
#         cursor.close()
#     if connection and connection.is_connected():
#         connection.close()
#         print("Connection closed")


# import mysql.connector

# conn = None
# cursor = None

# try:
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="minnie",
#         database="d15"
#     )

#     if conn.is_connected():
#         print("connected successfully")

#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM student;")

#     for row in cursor.fetchall():
#         print(row)

# except mysql.connector.Error as e:
#     print("Database error:", e)

# finally:
#     if cursor is not None:
#         cursor.close()
#     if conn is not None and conn.is_connected():
#         conn.close()




# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="minnie",
#     database="d15"
# )

# cursor = conn.cursor()

# sql = "INSERT INTO emp(emp_id,emp_name,email,salary,dept_name,gender,join_date,emp_experience) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# values = (101, "Hemanth", "hemanth@example.com", 50000, "IT", "Male", "2023-01-01", 2 )

# cursor.execute(sql, values)
# conn.commit()

# print("Record inserted successfully")

# cursor.close()
# conn.close()







import mysql.connector

# --- Database Connection ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="minnie",   # change to your MySQL password
    database="d15"       # change to your database name
)
cursor = conn.cursor()

# --- User Login ---
# def login():
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
#     result = cursor.fetchone()

#     if result:
#         print(f"\n✅ Welcome, {username}! You are logged in.\n")
#         menu()
#     else:
#         print("❌ Invalid login. Try again.")

# --- CRUD Operations ---
def create():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    cursor.execute("INSERT INTO student (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    print("✅ Record created successfully.")

def read():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    print("\n📋 Student Records:")
    for row in rows:
        print(row)

def update():
    sid = int(input("Enter student ID to update: "))
    new_age = int(input("Enter new age: "))
    cursor.execute("UPDATE student SET age=%s WHERE id=%s", (new_age, sid))
    conn.commit()
    print("✅ Record updated successfully.")

def delete():
    sid = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM student WHERE id=%s", (sid,))
    conn.commit()
    print("✅ Record deleted successfully.")

# --- Menu ---
def menu():
    while True:
        print("\nChoose an operation:")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            read()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

# --- Run Program ---
# login()

# Close connection when done
cursor.close()
conn.close()
