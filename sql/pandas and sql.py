import pandas
import sqlite3

employee_details = pandas.read_csv("employee.csv")
highest_salary = employee_details["salary"].max()  # Get the maximum salary via pandas series
print(f"The highest salary from the given employee data  via pandas is {highest_salary}")
emp_list = employee_details.values.tolist()  # Convert dataframe to list
connection = sqlite3.connect("employee.db")  # create a connection
cursor = connection.cursor()  # create a cursor
# cursor.execute("""CREATE TABLE employee_details(
#     firstname text,
#     lastname text,
#     email text,
#     profession text,
#     age INTEGER,
#     salary Real
# )""") #create Table
# cursor.executemany("INSERT INTO employee_details VALUES (?, ?, ?, ?, ?, ?)",emp_list)#insert emp_list to db
cursor.execute("SELECT MAX(salary) FROM employee_details")
print(f"The highest salary from the given employee data  via sqlite is {cursor.fetchall()}")
cursor.execute("SELECT MAX(salary), * FROM employee_details")
print(f"Max salary entire row :{cursor.fetchall()}")
action = input(
    "Choose the word for output age for age > 50,salary for sal > 5000,name for FN starts with A,update--age update: ")
if action == "age":
    cursor.execute("SELECT * FROM employee_details WHERE age > 50")  # Get full detail of employee whose age is above 50
elif action == "salary":
    cursor.execute("SELECT firstname,lastname,salary FROM employee_details WHERE salary > 5000.00")
elif action == "name":
    cursor.execute("SELECT * FROM employee_details WHERE firstname LIKE 'A%'")
elif action == "update":
    cursor.execute("UPDATE employee_details SET age=23 WHERE age<18")
    cursor.execute("SELECT * FROM employee_details")
output = cursor.fetchall()
for element in output:
    print(element)
connection.commit()#commit the table
connection.close()#close the table