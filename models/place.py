#!/usr/bin/python3
""" Class Place that inherits from base model"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ Class Place that inherits from base model """
    city_id = ""  # string - City.id
    user_id = ""  # string - User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # list of string: list of Amenity.id

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(self, *args, **kwargs)
