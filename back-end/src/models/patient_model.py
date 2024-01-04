from sqlalchemy import Column, String, INTEGER

from db.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    address = Column(String)
