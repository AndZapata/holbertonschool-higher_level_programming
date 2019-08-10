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

    string = "SELECT id, name FROM states \
    WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(argv[4])
    cur.execute(string)
    for string in cur:
        print(string)
    cur.close()
