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
    state_name = argv[4]
    ''' Creating a cursor '''
    cur = db.cursor()

    ''' Executing the query to list all the states '''
    cur.execute("SELECT cities.name\
                FROM cities\
                INNER JOIN states\
                on cities.state_id = states.id\
                WHERE states.name = %(state_name)s\
                ORDER BY cities.id ASC",
                {'state_name': state_name})
    rows = cur.fetchall()
    list = []
    for row in rows:
        for col in row:
            list.append(col)
    print(', '.join(list))

    ''' close all cursor and database '''
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
