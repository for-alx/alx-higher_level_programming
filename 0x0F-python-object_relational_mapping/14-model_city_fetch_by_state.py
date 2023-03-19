#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = Session(bind=engine)

    result = session.query(City, State).\
        filter(State.id == City.state_id).\
        order_by(City.id).all()

    # Format(<state name>: (<city id>) <city name>)
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
