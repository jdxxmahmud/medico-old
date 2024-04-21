from sqlalchemy import Column, String, Integer, DateTime, BigInteger, event
from sqlalchemy.sql import func
from db.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(BigInteger, primary_key=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    contact_no = Column(String, nullable=False)
    email = Column(String, nullable=False)
    
    gender = Column(String, nullable=False)

    date_of_birth_ts = Column(BigInteger, nullable=False)  # Timestamp format
    
    address = Column(String, nullable=False)

    house_no = Column(String)
    road = Column(String)
    post_code = Column(String)
    town = Column(String)
    
    created_at_ts = Column(BigInteger, 
                        default=func.current_timestamp())
    