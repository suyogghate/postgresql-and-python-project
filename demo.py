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
    connection = psycopg2.connect(
            dbname="studentdb",
            user="postgres",
            password="root1234",
            host="localhost",
            port="5432"
            )
    cur = connection.cursor()
    fields = {
        "1":("name", "Enter new name: "),
        "2":("address", "Enter new address: "),
        "3":("age", "Enter new age: "),
        "4":("phno", "Enter new number: ")
    }

    print("Which field would you like to update: ")
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    field_choice = input("Enter the number of the field you want to update: ")

    if field_choice in fields:
        field_name, prompt = fields[field_choice]
        new_value = input(prompt)
        sql = f"UPDATE students SET {field_name}=%s WHERE student_id=%s"
        cur.execute(sql, (new_value, student_id))
        print(f"{field_name} is updated successfully.")
    else:
        print("Invalid choice")

   
    
    connection.commit()
    connection.close()

def delete_data():
    student_id = input("Enter the ID of the student to be deleted: ")
    connection = psycopg2.connect(
            dbname="studentdb",
            user="postgres",
            password="root1234",
            host="localhost",
            port="5432"
            )
    cur = connection.cursor()

    cur.execute("SELECT * FROM students WHERE student_id=%s", (student_id,))
    student = cur.fetchone()

    if student:
        print(f"Student to be deleted: ID {student[0]}, Name:{student[1]}, Address:{student[2]}, Age: {student[3]}, Phno:{student[4]}")
        choice = input("Are you sure you want to delete the student details (Yes/No): ")
        if choice.lower() == "yes":
            cur.execute("DELETE FROM students WHERE student_id=%s", (student_id,))
            print("Student record deleted")
        else:
            print("Deletion cancelled.")
    else:
        print("Student not found")

    connection.commit()
    connection.close()

delete_data()












