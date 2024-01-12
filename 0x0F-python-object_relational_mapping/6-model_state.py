#!/usr/bin/python3
"""Establish a link between classes and database tables."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create a SQLAlchemy engine for MySQL database connection
    db_user, db_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{db_user}:{db_password}@localhost/{db_name}', pool_pre_ping=True)

    # Create tables defined in the model_state module
    Base.metadata.create_all(engine)

