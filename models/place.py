#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from os import getenv


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
      
        @property
        def reviews(self):
          """ Returns list of reviews.id """
          
          var = models.storage.all()
          lista = []
          result = []
          for key in var:
              review = key.replace('.', ' ')
              review = shlex.split(review)
              if (review[0] == 'Review'):
                  lista.append(var[key])
          for elem in lista:
              if (elem.place_id == self.id):
                  result.append(elem)
          return (result)
              
          @property
          def amenities(self):
              """ Returns list of amenity ids """
              return self.amenity_ids
  
          @amenities.setter
          def amenities(self, obj=None):
              """ Appends amenity ids to the attribute """
              if type(obj) is Amenity and obj.id not in self.amenity_ids:
                  self.amenity_ids.append(obj.id)
