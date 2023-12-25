from fastapi import APIRouter, HTTPException
from schemas.doctor_schema import *
from models import doctor_model

from db.database import SessionLocal, engine
from services.doctor_service import get_doctors

router = APIRouter(
    prefix="/doctors",
    tags=["doctors"],
    responses={404: {"description": "Not found"}},
)

doctor_model.Base.metadata.create_all(bind=engine)



@router.get("/")
async def get_all_doctor():
    return get_doctors


# @router.get("/{doctor_id}")
# async def read_item(doctor_id: str):
#     if doctor_id not in fake_doctor_db:
#         raise HTTPException(status_code=404, detail="Doctor not found")
#     return {"doctor": fake_doctor_db[doctor_id]["name"], "doctor_id": doctor_id}


# @router.put(
#     "/{doctor_id}",
#     tags=["custom"],
#     responses={403: {"description": "Operation forbidden"}},
# )
# async def update_doctor(doctor_id: str, doctor: DoctorIn):
#     if doctor_id != "1":
#         raise HTTPException(
#             status_code=403, detail="You can only update the item: 1"
#         )
#     return doctor