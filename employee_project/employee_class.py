
import os
import re
from Constants import *
emp_id = 0
employee_database = dict()


class EmployeeInfo():
    """
     EmployeeInfo class handled the all the employee related functionalities.
    """
    def __init__(self, name, age, phone_number, address, designation, salary):
        """
        Constructor For  Employee_info Class .

        Args:
            arg1 (str): The first argument name .
            arg2 (int): The second argument age.
            arg3 (int): The threed argument phone_number.
            arg4 (str): The fourth argument address.
            arg5 (str): The fourth argument designation.
            argr (int): The fourth argument salary.

        Return :
            None
        """
        self.emp_name = name
        self.emp_age = age
        self.emp_phone = phone_number
        self.emp_address = address
        self.emp_designation = designation
        self.emp_salary = salary

    def emp_details(self):
        """ @param: None
            @desc: Display The Employee Details
            @returns: None
        """
        print(" Employee Name: ", self.emp_name)
        print(" Employee Age: ", self.emp_age)
        print(" Employee Phone Number: ", self.emp_phone)
        print(" Employee Address: ", self.emp_address)
        print(" Employee Designation: ", self.emp_designation)
        print(" Employee Salary: ", self.emp_salary)


    def get_employee_name(self, employee_name):
        """ @param: str
            @desc: Get the input from the user and Verifying the user input is proper or not ,
            Return the Employee Name
            @returns: str
        """
        while True:
            length_name = len(employee_name)
            if employee_name.isalpha() == True or ' ' in employee_name:
                if (MIN_LENTH_NAME < length_name and MAX_LENTH_NAME > length_name):
                    return employee_name
                else:
                    print("Enter the minmum 3 chacters and maximun 15 characters")
            else:
                print("Invalid name entered , Please provide the valid name")
                employee_name = input("Enter Employee Name : ")

    def get_emp_age(self, age):
        """ @parm: str
            @desc: get the age of the employee from the database
            @return: int
        """
        while True:
            try:

                age = int(age)
                if age >= MAX_AGE and age <= MIN_AGE:
                    return age
                else:
                    print('Enter the valid age between 22 to 65')
            except ValueError:
                print('Enter the valid input:Ex-25')
                age = input("Enter Employee Age: ")


    def get_emp_phone_number(self, phone):
        """ @parm: str
            @desc: Get the input from the user and Verifying the user input is proper or not ,
            Return the Phone number
            @return: str
        """
        while True:
            if  len(phone) == 10 and phone.isdigit():
                return phone
            else:
                print('Enter the valid Phone Number:Ex-9988776655')
                phone = input("Enter Employee Phone Number: ")


    def get_emp_address(self, address):
        """ @parm: str
            @desc: add Employee Adderss to mployee Details
            @return: str
        """
        data_limit_reg = re.compile(ADDRESS_REG)
        while True:
            if (data_limit_reg.match(address)) and len(address) <= MIN_ADDRESS_LENGTH:
                return address
            else:
                print('Address not valid please enter the address again, Suggestion: use only ", - / " as operators or no. of caracters not morethan 150')
                address = input("Enter Employee Address : ")


    def get_emp_designation(self, designation):
        """ @parm: str
            @desc: Get the input from the user and Verifying the user input is proper or not ,
            Return the designation
            @return: str
        """
        while True:
            if designation in EMP_DESC:
                return designation
            else:
                print('Enter the valid Designation:',EMP_DESC)
                designation = input("Enter Employee Designation : ").strip()


    def get_emp_salary(self, salary):
        """ @parm: str
            @desc: Get the input from the user and Verifying the user input is proper or not ,
            Return the salary
            @return: int
        """
        while True:
            try:
                sal=int(salary)
                return sal
            except ValueError:
                print('Enter the valid ammount:Ex-20000')
                salary = input("Enter Employee Salary: ")


    def get_employee_data(self, employee_id):
        """ @param: int
            @desc: Check the Employee id from the database and get the data from database
            @returns: object
        """
        for emp_id in employee_database:
            if emp_id == employee_id:
                emp_data = employee_database[emp_id]
                return emp_data


    def display_emp_details(self, employee_id):
        """ @param: int
            @desc: Display the employee details
            @returns: None
        """
        emp_data = self.get_employee_data(employee_id)
        if emp_data:
            print(" Employee Id : ", employee_id)
            emp_data.emp_details()
        else:
            print("No Data Found ...")

    def remove_employee_data(self, employee_id):
        """ @param: int
            @desc: Remove/Delete data from data base
            @returns: bool
        """
        for emp_id in employee_database:
            if emp_id == employee_id:
                del employee_database[emp_id]
                return True
        return False

    def remove_employee_data(self, employee_id):
        """ @param: int
            @desc: Remove/Delete data from data base
            @returns: bool
        """
        for emp_id in employee_database:
            if emp_id == employee_id:
                emp_data  = self.get_employee_data(employee_id)
                #emp_data.emp_delete()
                return True
        return False


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


def get_empid():
    """ @param: None
        @desc: Return the employee Id
        @returns: int
    """
    global emp_id
    emp_id = emp_id + 1
    return emp_id
