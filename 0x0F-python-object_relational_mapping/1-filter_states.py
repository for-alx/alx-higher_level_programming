#!/usr/bin/python3
"""
Lists all states from database hbtn_0e_0_usa that start with 'N'
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE CONVERT(`name` USING Latin1) \
                 COLLATE Latin1_General_CS LIKE 'N%';")
    states = cur.fetchall()

    for state in states:
        print(state)