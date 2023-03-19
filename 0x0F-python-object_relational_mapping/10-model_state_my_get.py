#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the db
"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    arg = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = Session(bind=engine)

    state_name = sys.argv[4]
    result = session.query(State).filter(State.name == state_name).first()

    if (not result):
        print("Not found")
    else:
        print(result.id)
