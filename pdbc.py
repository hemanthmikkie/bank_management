import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="minnie",
    database="pratice"
)
cursor = conn.cursor()
# cursor.execute("SELECT * FROM employees")
# rows = cursor.fetchall()
# print(rows)
# rows = cursor.fetchone()
# print(rows)
# rows = cursor.fetchmany(3)
# print(rows)
# cursor.execute("INSERT INTO employees VALUES (155, 'chadini', 'Female', 28, 'HR', 'HR Executive', 42000.00, 3, 'sneha@gmail.com', '9876543210', '2022-03-15', 'Mumbai', 'Active');")
# conn.commit()
# user=input("enter id : ")
# cursor.execute(f"select * from employees where employee_id={user};")
# rows = cursor.fetchall()
# print(rows)
# cursor.execute(f"delete from employees where employee_id=%s;", (140,))
# conn.commit()
# cursor.execute("SELECT * FROM employees")
# rows = cursor.fetchall()
# print(rows)
# cursor.execute("UPDATE employees SET emp_name='sneha' WHERE emp_id=155;")
# conn.commit()
# cursor.execute("SELECT * FROM employees")
# rows = cursor.fetchall()
# print(rows)

cursor.execute("SELECT * FROM employees where city='hyderabad';")
rows = cursor.fetchall()
print(rows)



