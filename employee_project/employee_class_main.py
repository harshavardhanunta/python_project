import os
import time
from employee_class import *
def main():
    employee_obj = Employeeinfo("", "", '', '', '', '')
    while True:
        choice = welcome_page()
        if choice == 1:
            os.system("cls")
            print("***************** REGISTER EMPLOYEE DETAILS ******************************\n\n")
            name = employee_obj.get_employee_name(input("Enter Employee Name:"))
            age = employee_obj.get_emp_age(input("Enter Employee age:"))
            phone_number = employee_obj.get_emp_phone_number(input("Enter Employee Phone Number:"))
            address = employee_obj.get_emp_address(input("Enter Employee Adderss:"))
            designation = employee_obj.get_emp_designation(input("Enter the designation:") )
            salary = employee_obj.get_emp_salary(input("Enter Employee Salary:"))
            emp_id = get_empid()
            emp_obj = Employeeinfo(name, age, phone_number, address, designation, salary)
            employee_database[emp_id] = emp_obj
            os.system("cls")
            print("\n****************Verify Employee Details***************\n")
            emp_obj.display_emp_details(emp_id)
            time.sleep(5)
        elif choice == 2:
            os.system("cls")
            print("********************* Removing the Employee Details ****************\n")
            emp_id = int(input("Enter Employee Id: "))
            #employee_obj = Employee_info(" ", " ", " ", " ", " ", " ")
            res = employee_obj.remove_employee_data(emp_id)
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
            employee_obj.display_emp_details(emp_id)
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
