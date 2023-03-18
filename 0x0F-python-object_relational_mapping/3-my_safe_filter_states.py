#!/usr/bin/python3
"""
Lists all values in the states tables of a database where name
matches the argument in a safe way
"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()
    qury = ""
    cur.execute("SELECT * FROM states WHERE name=%s;", (sys.argv[4], ))

    rows = cur.fetchall()
    for row in rows:
        print(row)
