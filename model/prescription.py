from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class prescription(Base):
    __tablename__ = 'prescription'

    id = Column(Integer, primary_key=True)
    #patientid = Column(Integer,foreign_key = True)
    dob = Column(Integer)
    gender = Column(String)
    phonenumber = Column(Integer)
    allergies = Column(String)


