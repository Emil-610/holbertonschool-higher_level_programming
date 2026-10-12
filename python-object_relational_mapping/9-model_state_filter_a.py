#!/usr/bin/python3
"""Lists all State objects containing the letter a from hbtn_0e_6_usa."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model_state import Base, State


def filter_a(username, password, db_name):
    """Print every State whose name contains an a, ordered by id."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name), pool_pre_ping=True)
    session = Session(engine)
    states = session.query(State).filter(State.name.like("%a%")).order_by(
        State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    filter_a(sys.argv[1], sys.argv[2], sys.argv[3])
