# build a schema using pydantic
from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str
    date_of_birth: str
    address: str

    class Config:
        orm_mode = True


class PatientIn(PatientBase):
    pass

class PatientOut(PatientBase):
    id: str

        