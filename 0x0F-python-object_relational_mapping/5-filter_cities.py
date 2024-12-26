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


    query = 'SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states \
                ON cities.state_id = states.id \
                ORDER BY cities.id ASC'



    cursor.execute(query)

    result = cursor.fetchall()
    string = ""
    for row in result:
        if row[1] == argv[4]:
            string += ', '+row[0]

    cursor.close()
    db.close()
