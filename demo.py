import psycopg2

def create_table():
    connection = psycopg2.connect(
                dbname="studentdb",
                user="postgres",
                password="root1234",
                host="localhost",
                port="5432"
                )

    cur = connection.cursor()
    cur.execute("CREATE TABLE students(student_id SERIAL PRIMARY KEY, name TEXT, address TEXT, age INTEGER, phno TEXT);")
    print("Student table created.")
    connection.commit()
    connection.close()

def insert_data():
    # code to accept data from user
    name = input("Enter student name: ")
    address = input("Enter student address: ")
    age = int(input("Enter student age: "))
    phno = input("Enter student phno: ")
    connection = psycopg2.connect(
                dbname="studentdb",
                user="postgres",
                password="root1234",
                host="localhost",
                port="5432"
                )

    cur = connection.cursor()
    cur.execute("INSERT INTO students(name, address, age, phno) VALUES (%s, %s, %s, %s)", (name, address, age, phno))
    print("Data added into students table.")
    connection.commit()
    connection.close()

def update_data():
    student_id = int(input("Enter student id to be updated: "))
    name = input("Enter student name: ")
    address = input("Enter student address: ")
    age = int(input("Enter student age: "))
    phno = input("Enter student phno: ")
    connection = psycopg2.connect(
                dbname="studentdb",
                user="postgres",
                password="root1234",
                host="localhost",
                port="5432"
                )
    cur = connection.cursor()
    cur.execute("INSERT INTO students(name, address, age, phno) VALUES (%s, %s, %s, %s)", (name, address, age, phno))














