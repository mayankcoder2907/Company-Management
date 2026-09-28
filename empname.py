from db import myconn,mycursor
def add_employee():
    name=input("Enter employees name: ")
    age=int(input("Enter employee age: "))
    gender=input("Enter employee gender: ")
    phnumber=int(input("Enter employee phone number: "))
    deptid=int(input("Enter employee department: "))
    insertquery = "INSERT INTO employee(empid,empname,age,gender,phnumber,dept_id) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (name,age,gender,phnumber,deptid)
    mycursor.execute(insertquery,values)
    myconn.commit()
    print("Employee data added successfully")
def view_employee():
    mycursor.execute("SELECT * FROM employee")
    for row in mycursor.fetchall():
        print(row)
def delete_employee():
    empid=int(input("Enter employee id: "))
    mycursor.execute("DELETE FROM employee WHERE empid=%s"%(empid))
    myconn.commit()
    print("Employee data deleted successfully")
