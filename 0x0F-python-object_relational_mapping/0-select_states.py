#!/usr/bin/python3
''' lists all states from the database hbtn_0e_0_usa '''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    co_db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        database=argv[3],
        port=3306)
    cur = co_db.cursor()

    string = "SELECT id, name FROM states ORDER BY id ASC"
    cur.execute(string)
    for string in cur:
        print(string)
    cur.close()
