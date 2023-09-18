# Performing-MYSQL-Task-using-Python
IF YOU WANT TO CREATE DATABASE TOO USING PYTHON YOU JUST NEED TO PERFORM THIS STEP:>

create_db_query = "CREATE DATABASE IF NOT EXISTS students"   ( HERE students is the database name)
cur.execute(create_db_query)
connection.commit()

If you are creating database then you need to remove database from the connection otherwise it will show you error:
connection = pymysql.connect(
            host="Your_host_name",
            user="Your_user_name",
            password="Your_password"

)
Once you have created the database then you need to add database name in the connection to use your selected database.
You can also use any database which is present in your MYSQL.
Query should be like this:>
connection = pymysql.connect(
            host="Your_host_name",
            user="Your_user_name",
            password="Your_password"
            database="Your_database_name"

)
Another thing you would encounter as a fresher:
if you have perform query that is:>

connection.close()


You just need to run connection query again for example:
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
connection.close()
After this you need to run the connection query.
Thank You!!

