#!/usr/bin/python3
'''DBStorage'''
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}"
            .format(user, password, host, database),
            pool_pre_ping=True,
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query on the current database session'''

        if cls is None:
        objects = self.__session.query(State).all()
            objects.extended(self.__session.query(User).all())
            objects.extended(self.__session.query(City).all())
            objects.extended(self.__session.query(Place).all())
            objects.extended(self.__session.query(Review).all())
            objects.extended(self.__session.query(Amenity).all())
            else:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}"
                .format(type(obj).__name__, obj.id): obj for obj in objs}
