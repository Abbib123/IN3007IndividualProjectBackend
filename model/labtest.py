from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class labtest(Base):
    __tablename__ = 'labtest'

    id = Column(Integer, primary_key=True)
    #medicalprofid = Column(Integer,foreign_key = True)
    name = Column(String)
    dob = Column(Integer)
    testordered = Column(String)
    status = Column(String)
    testresult = Column(String)
    


