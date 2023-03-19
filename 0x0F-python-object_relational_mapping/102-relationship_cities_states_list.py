#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the DB
"""

if __name__ == '__main__':
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = Session(bind=engine)

    # result = session.query()
    result = session.query(State).join(City).order_by(City.id).all()

    for state in result:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
