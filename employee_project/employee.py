'''Employee Project'''

import os
import re
emp_id = 0
employee_database = dict()

def get_emp_age():
    while True:
        age = int(input('Enger age : '))
        if age>=18 and age<=60:
            return age
        print('Invalid age entered, please re-enter age, Suggestion: Enter number format and Age in between 18 and 60 only')

def get_emp_address():
    data_limit_reg = re.compile(r'[a-zA-Z0-9,-/ ]*$')
    while True:
        address = input("Enter Employee Address : ")
        if (data_limit_reg.match(address)) and len(address) <= 150:
            return address
        else:
            print('Address not valid please enter the address again, Suggestion: use only ", - / " as operators or no. of caracters not morethan 150')


def get_empid():
    """ @param: None
        @desc: Return the employee Id
        @returns: int
    """
    global emp_id
    emp_id = emp_id + 1
    return emp_id


def remove_employee_data(employee_id):
    """ @param: int
        @desc: Remove/Delete data from data base
        @returns: bool
    """
    for emp_id in employee_database:
        if emp_id == employee_id:
            del employee_database[emp_id]
            return True
    return False


def get_employee_data(employee_id):
    """ @param: int
        @desc: Check the Employee id from the database and get the data from database
        @returns: list()
    """
    emp_data = list()
    for emp_id in employee_database:
        if emp_id == employee_id:
            emp_data = employee_database[emp_id]
            return emp_data
    return emp_data


def display_emp_details(employee_id):
    """ @param: int
        @desc: Display the employee details
        @returns: None
    """
    emp_data = get_employee_data(employee_id)
    if emp_data:
        print(" Employee Id : ", employee_id)
        print(" Employee Name: ", emp_data[0])
        print(" Employee Age: ", emp_data[1])
        print(" Employee Phone Number: ", emp_data[2])
        print(" Employee Address: ", emp_data[3])
        print(" Employee Designation: ", emp_data[4])
        print(" Employee Salary: ", emp_data[5])
    else:
        print("No Data Found ...")


def welcome_page():
    """ @param: None
        @desc: Display the home page
        @returns: int
    """
    os.system("cls")
    print("\n\n*******************************************************************")
    print("****************** WELCOME TO EMPLYEE SERVICES ********************")
    print("*******************************************************************\n")
    print(" Add Employee Details Enter number           : 1")
    print(" Remove/Delete Employee Details Enter number : 2")
    print(" Display Employee Details Enter number       : 3")
    print(" Exit the Apllication Enter number           : 4")
    choice = int(input("\nEnter your choice : "))
    return choice


def get_emp_salary_input(msg = "Enter employee salary:"):
    """ @param: string
        @desc: Receive the input from the user and validating the data
        @returns: int
    """
    try:
        sal = int(input(msg))
    except ValueError:
        print("Invalid input, enter a valid input ex: 20000")
        sal = get_emp_salary_input(msg)
    return sal
