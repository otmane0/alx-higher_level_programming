#!/usr/bin/python3
"""Order by id"""

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


    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query, (argv[4],))

    result = cursor.fetchall()
    for one in result:
        if one[1] == argv[4]:
            print(one)

    cursor.close()
    db.close()
