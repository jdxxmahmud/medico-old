from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    id  = Column(String, primary_key=True, index=True)
    name = Column(String)
    # date_of_birth = Column(Integer)
    # address = Column(String)
    # post_office = Column(String)
    # time_created = Column(DateTime(timezone=True), server_default=func.now())
    # time_updated = Column(DateTime(timezone=True), onupdate=func.now())




