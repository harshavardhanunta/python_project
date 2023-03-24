''' Main File'''
import os
import time
from employee import *

def main():

    while True:
        choice = welcome_page()
        if choice == 1:
            os.system("cls")
            print("***************** REGISTER EMPLOYEE DETAILS ******************************\n\n")
            name = input("Enter Employee Name: ")
            age = get_emp_age()
            ph_num = input("Enter Employee Phone Number: ")
            address = get_emp_address()
            designation = input("Enter Employee Designation : ")
            sal = get_emp_salary_input ("Enter Employee Salary: ")
            emp_id = get_empid()
            emp_data = [name, age, ph_num, address, designation, sal]
            employee_database[emp_id] = emp_data
            os.system("cls")
            print("\n****************Verify Employee Details***************\n")
            display_emp_details(emp_id)
            time.sleep(5)

        elif choice == 2:
            os.system("cls")
            print("********************* Removing the Employee Details ****************\n")
            emp_id = int(input("Enter Employee Id: "))
            res = remove_employee_data(emp_id)
            if res:
                print("Employee Data sucessfully deleted ..")
                time.sleep(3)
            else:
                print("No data found from the employee id ", emp_id)
                time.sleep(3)

        elif choice == 3:
            os.system("cls")
            print("****************** Employee Details ********************")
            emp_id = int(input("Enter Employee Id: "))
            display_emp_details(emp_id)
            time.sleep(5)

        elif choice == 4:
            os.system("cls")
            print(" \n\n ***************** Closing the Employee Application .....")
            time.sleep(2)
            break

        else:
            print("\n ********** Choose Above options only ....")
            time.sleep(2)

if __name__ == "__main__":
    main()
