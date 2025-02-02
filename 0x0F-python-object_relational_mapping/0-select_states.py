#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""

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


    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    result = cursor.fetchall()
    for x in result:
        print(x)


    cursor.close()
    db.close()