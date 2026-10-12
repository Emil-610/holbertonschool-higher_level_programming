#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import sys

import MySQLdb


def list_states(username, password, db_name):
    """Print all rows of the states table, sorted by states.id ascending."""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
