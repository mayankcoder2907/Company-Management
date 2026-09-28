from empname import *
from department import *
from empname import add_employee
from project import *
from salary import *
from report import *
while True:
     print("1.Add Employees")
     print("2.View Employees")
     print("3. Delete Employees")
     print("4. Add Department")
     print("5. View Department")
     print("6. Add Project")
     print("7. Add Salary")
     print("8. Department report")
     print("9.Salary Report")
     print("10.Exit")
     choice=int(input("Enter your choice:"))
     if choice==1:
        add_employee()
     elif choice==2:
        view_employee()
     elif choice==3:
        delete_employee()
     elif choice==4:
         add_department()
     elif choice==5:
         view_departments()
     elif choice==6:
         add_project()
     elif choice==7:
         add_salary()
     elif choice==8:
         department_report()
     elif choice==9:
         salary_report()
     elif choice==10:
         print("Exit")
         break
     else:
         print("Enter a valid choice")


