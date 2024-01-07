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


@router.get("/{patient_id}")
async def read_item(patient_id: int, db: Session = Depends(get_db)):
    return get_patient_by_id(patient_id, db)


@router.post("/add-patient", response_model=PatientOut)
def create_patient(patient: PatientIn, db: Session = Depends(get_db)):
    return add_patient(db=db, patient=patient)

@router.delete("/delete-patient", response_model=PatientOut)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    return delete_patient_by_id(patient_id, db)


@router.put("/{patient_id}",)
def update_patient(patient_id: int, updated_patient: PatientIn, db = Depends(get_db)):

    return edit_patient(patient_id, updated_patient, db)