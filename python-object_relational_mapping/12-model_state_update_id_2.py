#!/usr/bin/python3
"""Changes the name of a State object in the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # On récupère l'état avec id = 2
    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
