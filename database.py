import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor, conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='1234567')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error!', 'Connection Failed')
        return
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data(Id VARCHAR(20), Name VARCHAR(50), Phone VARCHAR(20), Role VARCHAR(30), Gender VARCHAR(20), Salary Decimal(10,2))')
    
def insert(id, name, phone, roll, gender, salary):
    mycursor.execute('INSERT into data VALUES (%s, %s, %s, %s, %s, %s)', (id, name, phone, roll, gender, salary) )
    conn.commit()

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE Id = %s', id)
    result = mycursor.fetchone()
    # print(result)        it will print (1,) if id exists in row 1 in the table output 
    return result[0] > 0

def fetch_employees():
    mycursor.execute('SELECT * FROM data')
    result = mycursor.fetchall()
    return result

connect_database()