#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = Session(bind=engine)

    result = session.query(State).order_by(State.id).first()

    if (not result):
        print("Nothing")
    else:
        print("{}: {}".format(result.id, result.name))
