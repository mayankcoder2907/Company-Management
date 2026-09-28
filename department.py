from db import myconn,mycursor
def add_department():
    department=input("Enter department name: ")
    mycursor.execute("INSERT INTO department VALUES (%s)",(department))
    myconn.commit()
    print("Department added successfully")
def view_departments():
    mycursor.execute("SELECT * FROM department")
    for row in mycursor.fetchall():
        print(row)

