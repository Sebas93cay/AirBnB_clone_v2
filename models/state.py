#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if models.STORAGE_TYPE == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete, delelete-orphan")
    else:
        @property
        def cities(self):
            from models import storage
            all_cities = storage.all(City)
            FS_cities = []
            for city in all_cities:
                if city.state_id == self.id:
                    FS_cities.append(city)
            return FS_cities
