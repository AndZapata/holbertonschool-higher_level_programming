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

    cur.execute("SELECT cities.name FROM cities \
    WHERE cities.state_id = (SELECT states.id FROM states \
    WHERE states.name = %s) ORDER BY cities.id ASC", (argv[4],))
    list_1 = []
    for string in cur:
        list_1 += string
    print(', '.join(list_1))
    cur.close()
