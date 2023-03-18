#!/usr/bin/python3
"""
List all cities of a state
"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
        JOIN states \
        ON cities.state_id = states.id \
        WHERE states.name=%s ORDER BY cities.id", (args[4], ))

    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
