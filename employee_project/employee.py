'''Employee Project'''

import os
import re
emp_id = 0
employee_database = dict()


def get_emp_address():
    data_limit_reg = re.compile(r'[a-zA-Z0-9,-/ ]*$')
    while True:
        address = input("Enter Employee Address : ")
        if (data_limit_reg.match(address)):
            return address
        else:
            print('Address not valid please enter the address again, Suggestion: use only ", - / " as operators')


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


def get_employee_name():
    """ @param: string
        @desc: This Method receives the input from the user and validating the name .
        @returns: string
    """
    while True:
        min_length_name = 3
        max_length_name = 15
        employee_name = input("Enter the  Employee Name:")
        length_name = len(employee_name)
        if employee_name.isalpha() == True or ' ' in employee_name:
            if (min_length_name < length_name and max_length_name > length_name):
                 return employee_name
            else:
                print("Enter the minmum 3 chacters and maximun 15 characters :")
        else:
            print("Invalid name entered , Please provide the valid name:")