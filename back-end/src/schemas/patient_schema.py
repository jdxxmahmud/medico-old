# build a schema using pydantic
from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str
    email: str
    address: str
    

    class Config:
        from_attributes = True


class PatientIn(PatientBase):
    pass

class PatientOut(PatientBase):
    pass

class PatientDB(PatientBase):
    id: int

        