#!/usr/bin/python3
"""
Lists all values in the states tables of a database where name
matches the argument
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur=cursor()
    cur.execute("SELECT * FROM states WHERE name={} ORDER BY id".format(args[4]))
    cur.fetchall()