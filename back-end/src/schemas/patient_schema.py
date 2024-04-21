# build a schema using pydantic
from pydantic import BaseModel, EmailStr


class PatientBase(BaseModel):

    first_name: str
    last_name: str

    contact_no: str
    email: EmailStr

    gender: str 

    date_of_birth_ts: int# Timestamp format

    address: str
    house_no: str
    road: str
    post_code: str
    town: str

    created_at_ts: int  = None# Timestamp format

    
    class Config:
        from_attributes = True


class PatientIn(PatientBase):
    pass

class PatientOut(PatientBase):
    pass

class PatientDB(PatientBase):
    id: int = None




