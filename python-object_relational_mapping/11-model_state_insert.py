#!/usr/bin/python3
"""Adds the State Louisiana to the database hbtn_0e_6_usa."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model_state import Base, State


def insert_state(username, password, db_name):
    """Insert Louisiana and print its new id."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name), pool_pre_ping=True)
    session = Session(engine)
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()


if __name__ == "__main__":
    insert_state(sys.argv[1], sys.argv[2], sys.argv[3])
