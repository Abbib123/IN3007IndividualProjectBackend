from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


#This class is optional,reconsider if this class is needed for future implementation
Base = declarative_base()

class sysadpanel(Base):
    __tablename__ = 'sysadpanel'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    dob = Column(Integer)
    gender = Column(String)
    phonenumber = Column(Integer)
    emailaddress = Column(String)
    address = Column(String)
    role = Column(String)
    accesslevel = Column(String)

