import pymysql
connection = pymysql.connect(
            host="Your_host_name",
            user="Your_user_name",
            password="Your_password",
            database='Your_database name'

)
cur = connection.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    grade VARCHAR(50) NOT NULL
)
"""
cur.execute(create_table_query)
connection.commit()
get_student_id=int(input("enter the id"))
get_first_name=(input("enter the first_name"))
get_last_name=(input("enter the last_name"))
get_age=int(input("enter the age"))
get_grade=float(input("enter the grade"))
sql = "INSERT INTO student (student_id,first_name, last_name, age, grade) VALUES (%s,%s,%s,%s,%s)"

cur.execute(sql,(get_student_id,get_first_name,get_last_name,get_age,get_grade))
connection.commit()
connection.close()
update_query = "UPDATE student SET grade = 97 WHERE first_name = 'alice' "
cur.execute(update_query)
connection.commit()
delete_query = "DELETE FROM student WHERE last_name = 'smith'"
cur.execute(delete_query)
connection.commit()


select_query = "SELECT * FROM student"
cur.execute(select_query)
student_records = cur.fetchall()
for record in student_records:
    print(record)
connection.close()