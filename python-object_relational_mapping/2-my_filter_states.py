#!/usr/bin/python3
"""Displays all states matching the name given as an argument."""
import sys

import MySQLdb


def my_filter_states(username, password, db_name, state_name):
    """Print the states whose name matches state_name, ordered by id."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = BINARY '{}' "
                "ORDER BY id ASC".format(state_name))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    my_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
