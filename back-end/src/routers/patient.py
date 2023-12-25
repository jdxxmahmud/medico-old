from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.patient_schema import *
from models import patient_model

from db.database import SessionLocal, engine
from services.patient_service import get_patients

patient_model.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/patients",
    tags=["patients"],
    responses={404: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()



@router.get("/")
def get_all_patient(db: Session = Depends(get_db)):
    patients = get_patients(db)
    return patients


# @router.get("/{patient_id}")
# async def read_item(patient_id: str):
#     if patient_id not in fake_patient_db:
#         raise HTTPException(status_code=404, detail="Patient not found")
#     return {"patient": fake_patient_db[patient_id]["name"], "patient_id": patient_id}


# @router.put(
#     "/{patient_id}",
#     tags=["custom"],
#     responses={403: {"description": "Operation forbidden"}},
# )
# async def update_patient(patient_id: str, patient: PatientIn):
#     if patient_id != "1":
#         raise HTTPException(
#             status_code=403, detail="You can only update the item: 1"
#         )
#     return patient