#!/usr/bin/python3
''' lists all states from the database hbtn_0e_0_usa '''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    co_db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = co_db.cursor()

    cur.execute("SELECT id, name FROM states \
    WHERE name = %s ORDER BY id ASC", (argv[4],))
    for string in cur:
        print("{}".format(string))
    cur.close()
