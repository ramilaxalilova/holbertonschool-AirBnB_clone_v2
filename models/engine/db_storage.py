#!/usr/bin/python3
"""this module defines a class to manage db storage"""
from sqlalchemy import create_engine, MetaData
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


sql = 'mysql+mysqldb://{}:{}@{}:3306/{}'
user = getenv('HBNB_MYSQL_USER')
pwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')


class DBStorage:
    """manages storage in db"""
    __engine = None
    __session = None

    def __init__(self):
        """creates new engine instances"""
        self.__engine = create_engine(sql.format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine, checkfirst=True)

    def all(self, cls=None):
        """queries db for objects"""
        dictonary = {}
        if cls:
            cls_list = [cls]
        else:
            cls_list = [User, State, City, Amenity, Place, Review]

        for c in cls_list:
            dictonary.update({
                "{}.{}".format(c.__name__, obj.id): obj
                for obj in self.__session.query(c).all()
                })
        return dictonary

    def new(self, obj):
        """adds the object to the current database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables n current database session in the database"""
        self.__session = Base.metadata.create_all(self.__engine)
        sess_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)

        Session = scoped_session(sess_maker)
        self.__session = Session()

    def close(self):
        """ closes sessio """
        self.__session.close()

    def close(self):
        """ call close on private session. """
        self.__session.remove()
