#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    s = Session()
    q = s.query(City).order_by(asc(City.id)).all()
    for i in q:
        print("{}: {} -> {}".format(i.id, i.name, i.state.name))

    s.close()
