#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model_state import Base, State


def fetch_first(username, password, db_name):
    """Print the State with the lowest id, or Nothing if the table is empty."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name), pool_pre_ping=True)
    session = Session(engine)
    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    fetch_first(sys.argv[1], sys.argv[2], sys.argv[3])
