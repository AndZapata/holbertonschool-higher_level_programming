#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from sqlalchemy import Column, Integer, String
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    s = Session()
    q = s.query(State).filter(State.name.like(
        '%a%')).order_by(asc(State.id)).all()
    for string in q:
        print("{}: {}".format(string.id, string.name))
    s.close()
