from sqlalchemy import Column, String

from db.database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, )
    date_of_birth = Column(String)
    address = Column(String)
