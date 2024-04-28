from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class patientportal(Base):
    __tablename__ = 'patientportal'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    dob = Column(Integer)
    gender = Column(String)
    phonenumber = Column(Integer)
    emailaddress = Column(String)
    emergencycontact = Column(Integer)
    address = Column(String)


