from sqlalchemy.orm import Session
from fastapi import HTTPException


from models.patient_model import Patient
from schemas.patient_schema import *


def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Patient).offset(skip).limit(limit).all()


def get_patient_by_email(db: Session, email: str):
    return db.query(Patient).filter(Patient.email == email).first()


def get_patient_by_id(patient_id: int, db: Session):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


def add_patient(db: Session, patient: PatientIn):
    with db:
        db_patient = get_patient_by_email(db, patient.email)
        if db_patient:
            raise HTTPException(status_code=400, detail="Email already registered")
    
        db_patient = Patient(
                        name=patient.name,
                        email=patient.email,
                        address=patient.address
                            )
        db.add(db_patient)
        db.commit()
        db.refresh(db_patient)

    return db_patient


def edit_patient(patient_id: int, updated_patient: PatientIn, db: Session):
    with db:
        db_patient = db.get(Patient, patient_id)

        patient_data = updated_patient.model_dump(exclude_unset=True)

        for key, value in patient_data.items():
            setattr(db_patient, key, value)

        db.add(db_patient)
        db.commit()
        db.refresh(db_patient)
        return db_patient




def delete_patient_by_id(db: Session, patient_id: int):
    with db:
        patient = get_patient_by_id(db, patient_id)
        db.delete(patient)
        db.commit()

        return patient