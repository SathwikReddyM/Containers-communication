from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)
connection = mysql.connector.connect(user='root', password='password', host='mysql', port="3306", database='db')
cursor = connection.cursor()
cursor.execute('Select FirstName, Surname FROM students')
students = cursor.fetchall()
x = []
print(students)
@app.route('/',methods = ['get','post'])
def index():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        prompt,prompt1 = request.form['prompt'],request.form['prompt1']
        cursor = connection.cursor()
        statement = 'INSERT INTO db.students(FirstName, Surname) VALUES(%s,%s);'
        #statement = 'INSERT INTO db.students(FirstName, Surname) VALUES("sat", "red");'
        cursor.execute(statement,(prompt,prompt1))
        connection.commit()
        cursor.execute('Select FirstName, Surname FROM students')
        students = cursor.fetchall()
        x.append(students)
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)