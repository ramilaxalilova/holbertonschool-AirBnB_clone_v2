#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":

    class State(BaseModel, Base):
        """State class"""

        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="all, delete, delete-orphan"
        )

else:

    class State(BaseModel):
        """State class"""

        name = ""

        @property
        def cities(self):
            cities_list = []
            for city in cities:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list