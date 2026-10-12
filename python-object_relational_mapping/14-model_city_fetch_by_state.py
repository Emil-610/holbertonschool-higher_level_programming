#!/usr/bin/python3
"""Prints all City objects with their State from hbtn_0e_14_usa."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model_city import City
from model_state import Base, State


def fetch_by_state(username, password, db_name):
    """Print each city as '<state name>: (<city id>) <city name>'."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name), pool_pre_ping=True)
    session = Session(engine)
    rows = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for state, city in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()


if __name__ == "__main__":
    fetch_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
