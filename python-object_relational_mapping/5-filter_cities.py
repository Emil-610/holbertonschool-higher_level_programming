#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa."""
import sys

import MySQLdb


def filter_cities(username, password, db_name, state_name):
    """Print the cities of state_name on one line, separated by commas."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s ORDER BY cities.id ASC",
                (state_name,))
    print(", ".join(row[0] for row in cur.fetchall()))
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
