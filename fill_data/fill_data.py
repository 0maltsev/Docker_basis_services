import mysql.connector
import csv


connection = mysql.connector.connect(user='root', password='root12', host='db', port='3306', database='db')
cursor = connection.cursor()

csv_data = csv.reader(open('/data/data.csv'))

cursor.execute("CREATE TABLE people(name VARCHAR(50) NOT NULL, age INT NOT NULL)")

header = next(csv_data)

for row in csv_data:
        cursor.execute("INSERT INTO people (name, age) VALUES (%s, %s)", row)

connection.commit()

cursor.execute("SELECT * FROM people")

result = cursor.fetchall()

for row in result:
    print(row)

connection.close()
