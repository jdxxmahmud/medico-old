from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.patient_schema import *
from models import patient_model

from db.database import engine, get_db
from services.patient_service import *

patient_model.Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/patients",
    tags=["patients"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_all_patient(db: Session = Depends(get_db)):
    patients = get_patients(db)
    return patients


@router.post("/add-patient", response_model=PatientOut)
def create_patient(patient: PatientIn, db: Session = Depends(get_db)):
    db_patient = get_patient_by_email(db, patient.email)

    if db_patient:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return add_patient(db=db, patient=patient)

@router.delete("/delete-patient", response_model=PatientOut)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    return delete_patient_by_id(db, patient_id)

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