#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
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

    records = session.query(State).filter(State.name.like('%a%')).all()

    for row in records:
        session.delete(row)
    session.commit()
