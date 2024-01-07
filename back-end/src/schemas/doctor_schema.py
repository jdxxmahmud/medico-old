# build a schema using pydantic
from pydantic import BaseModel

class DoctorBase(BaseModel):
    name: str
    date_of_birth: str
    address: str

    # class Config:
    #     from_attributes = True


class DoctorIn(DoctorBase):
    pass

class DoctorOut(DoctorBase):
    pass

class DoctorDB(DoctorBase):
    id: str

        