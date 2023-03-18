#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import MySQLdb
    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states \
                ON cities.state_id = states.id ORDER BY cities.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
