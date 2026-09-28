import mysql.connector

#print('mysqlconnector installed successfully')
myconn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@",
    database="company_management"

)
mycursor = myconn.cursor()
