#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database
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

    result = session.query(State).filter(State.name.like('%a%'))\
                    .order_by(State.id).all()

    for row in result:
        print("{}: {}".format(row.id, row.name))
