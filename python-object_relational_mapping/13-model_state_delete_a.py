#!/usr/bin/python3
"""Deletes all State objects containing the letter a from hbtn_0e_6_usa."""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model_state import Base, State


def delete_a(username, password, db_name):
    """Delete every State whose name contains the letter a."""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name), pool_pre_ping=True)
    session = Session(engine)
    session.query(State).filter(State.name.like("%a%")).delete(
        synchronize_session=False)
    session.commit()
    session.close()


if __name__ == "__main__":
    delete_a(sys.argv[1], sys.argv[2], sys.argv[3])
