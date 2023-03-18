#!/usr/bin/python3

if __name__ == '__main__':
	import sys
	import MySQLdb
	args = sys.argv
	# db = MySQLdb.connect(host='localhost', user=args[1], passwd=args[2], db=args[3])
	# cur = db.cursor()

	query = "SELECT * FROM table_name WHERE column_name = %s"

	rows = cur.fetchall()
    for row in rows:
        print(row)




