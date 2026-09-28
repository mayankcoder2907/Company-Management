from db import myconn,mycursor
def add_salary():
    empid=int(input("Enter employee id: "))
    amount=float(input("Enter employee salary: "))
    monthname=input("Enter month name: ")
    mycursor.execute("INSERT INTO Salary (empid,amount,monthname) VALUES (%s,%s,%s)",(empid,amount,monthname))
    myconn.commit()
    print("Salary added successfully")