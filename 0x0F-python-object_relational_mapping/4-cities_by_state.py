#!/usr/bin/python3
''' Script that lists all states from the database '''
import MySQLdb
from sys import argv


def main():
    '''Creating connection to the db '''
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    ''' Creating a cursor '''
    cur = db.cursor()

    ''' Executing the query to list all the states '''
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                INNER JOIN states\
                on cities.state_id = states.id\
                ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    ''' close all cursor and database '''
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
