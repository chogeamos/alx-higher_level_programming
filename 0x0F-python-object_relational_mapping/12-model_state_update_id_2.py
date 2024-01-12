#!/usr/bin/python3
""" Updates the name of the State object with the specified ID in the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create a database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create the tables in the database
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and update the name of the State object with the specified ID
    new_instance = session.query(State).filter_by(id=2).first()
    new_instance.name = 'New Mexico'

    # Commit the changes to the database
    session.commit()

