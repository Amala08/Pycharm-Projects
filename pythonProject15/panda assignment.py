import pandas
#Read the csv file via pandas

employee_details = pandas.read_csv("employee.csv")

#Get the maximum salary via pandas series
# highest_salary = employee_details["salary"].max()
# print("MAXIMUM SALARY")
# print("***************")
# print(f"The highest salary from the given employee data is {highest_salary}")
# print("############################################################")

#Convert dataframe to list

emp_list = employee_details.values.tolist()

#Insert the emp_list to sqlite database

import sqlite3
#create a connetion
connection = sqlite3.connect("employee.db")

#create a cursor
cursor = connection.cursor()

#create Table

cursor.execute("""CREATE TABLE employee_details(
    firstname text,
    lastname text,
    email text,
    profession text,
    age INTEGER,
    salary Real
)
""")
#creating the entire details for the list

cursor.executemany("INSERT INTO employee_details VALUES (?, ?, ?, ?, ?, ?)",emp_list)

#commit the table

connection.commit()

#close the table

connection.close()

#Get full detail of employee whose age is above 50

# cursor.execute("SELECT * FROM employee_details WHERE age = 50")
# age_list = cursor.fetchall()
# for element in age_list:
#     print(element)
# print("########################################################################################")
#
# #Get only first name,last name and salary of the employee whose salary is above 5000
#
# cursor.execute("SELECT firstname,lastname,salary FROM employee_details WHERE salary > 5000.00")
# salary_list = cursor.fetchall()
# for element in salary_list:
#     print(element)
# print("########################################################################################")
#
# #Get employee full detail whose name starts with A
#
# cursor.execute("SELECT * FROM employee_details WHERE firstname LIKE 'A%'")
# employee_list = cursor.fetchall()
# for element in employee_list:
#     print(element)

#Update the employee age to 23 where the age is less than 18

cursor.execute("""UPDATE employee_details 
SET age=23
WHERE age<18""")

connection.commit()

update_list = cursor.fetchall()
print(update_list)



