
import datetime

from sqlalchemy import Boolean
from sqlalchemy import Column, Integer, String, Text, Date, Time, schema
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

import app.helpers
from app.models.base import Base
from app.models import db, File


# almost all the fields are completly empty since we can't be 100% sure imdb won't just fuck us over
class Movie(db.Model):
    __tablename__ = "movie"
    name = Column(String)
    imdb_id = Column(String)
    genre = Column(String, nullable=True)
    desc = Column(Text, nullable=True)
    release = Column(Date, nullable=True)
    runtime = Column(String, nullable=True)
    actors = Column(String, nullable=True)
    directors = Column(String, nullable=True)
    writer = Column(String, nullable=True)
    poster = Column(Text, nullable=True)  # can be an image in cache or a direct url to the website
    rate = Column(String, nullable=True)
    #raings = Column(Integer,nullable=True)
    files = relationship("File")
    viewed= Column(Boolean, default=False)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    pass