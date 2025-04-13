import pymysql



conn = pymysql.connect(
     host = 'localhost',
     user = 'root',
     password='chavijain@0209',
     database='DB2'
 )

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(100),
               age INT)
               ''')


cursor.execute("INSERT INTO users(name,age)VALUES('Alice',30)")
cursor.execute("INSERT INTO users(name,age)VALUES('Bob',40)")

conn.commit()

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()