#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

db = MySQLdb.connect(
    host='localhost',
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    port=3306
)

cursor = db.cursor()


query = f"SELECT id, name FROM states WHERE name = '{argv[4]}' ORDER BY id ASC"

cursor.execute(query)

result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
db.close()
