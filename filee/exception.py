# try:
#     # Code that may cause an exception
# except ExceptionType:
#     # Code to handle the exception
# else:
#     # Executes if no exception occurs
# finally:
#     # Executes whether an exception occurs or nots


#exception handling in Python is a mechanism that allows you to gracefully handle errors and exceptional situations that may arise during the execution of your code. It helps prevent your program from crashing and allows you to provide meaningful feedback or take corrective actions when an error occurs.
# num=10
# r=num/2
# print(r)



# try:
#     num=10
#     r=num/0
#     print(r)
# except ZeroDivisionError:
#     print("division by zero is not allowed")
# else:
#     print("succesfully executed")

# finally:
#     print("this is finally block")




# age=-5
# if age<0:
#     raise ValueError("Age cannot be negative")




try:
    file=open("minniee.txt","r")
    content=file.read()
except FileNotFoundError:
    print("file not found")
