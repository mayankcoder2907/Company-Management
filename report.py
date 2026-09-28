from db import myconn,mycursor
def department_report():
    query="select department.dept_name,employee.empname from employee join department on employee.emp_id=department.emp_id"

    mycursor.execute(query)
    for row in mycursor.fetchall():
        print(row)
def salary_report():
    query="select employee.empname,salary.amount,salary.monthname from employee join salary on employee.emp_id=salary.emp_id"
    mycursor.execute(query)
    for row in mycursor.fetchall():
        print(row)

