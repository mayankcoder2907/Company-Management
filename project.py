from db import myconn,mycursor
def add_project():
   project_name=input("Enter project name: ")
   department=input("Enter department name: ")
   mycursor.execute("INSERT INTO department(project_name,dept_id) VALUES(%s,%s),(project_name,dept_id)")
   myconn.commit()
   print("Project added successfully")
