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
    sess = Session()
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_city.state = new_state
    sess.add(new_state)
    sess.add(new_city)
    sess.commit()
    sess.close()
