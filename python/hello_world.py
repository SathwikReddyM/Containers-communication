import mysql.connector
connection = mysql.connector.connect(user='root', password='password', host='mysql', port="3306", database='db')
cursor = connection.cursor()
cursor.execute('Select * FROM students')
students = cursor.fetchall()
print(students)
    
