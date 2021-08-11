#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
import models
from models.amenity import Amenity
from models.review import Review

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)
    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)
    max_guest = Column(Integer,
                       nullable=False,
                       default=0)
    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)
    latitude = Column(Float, nullable=True,
                      default=0)
    longitude = Column(Float, nullable=True,
                       default=0)
    amenity_ids = []

    if models.STORAGE_TYPE == 'db':
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete, delete-orphan")
    else:
        @property
        def reviews(self):
            inst_reviews = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    inst_reviews.append(review)
            return inst_reviews

        @property
        def amenities(self):
            """
            return amenity_id
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, amenity):
            """
            update amenity list
            """
            if type(amenity).__name__ == 'Amenity':
                self.amenity_ids.append(amenity.id)
