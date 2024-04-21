from sqlalchemy.orm import Session
from fastapi import HTTPException


from models.patient_model import Patient
from schemas.patient_schema import *


def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Patient).offset(skip).limit(limit).all()


def get_patient_by_id(patient_id: int, db: Session):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


def add_patient(patient: PatientIn, db: Session):
    with db:

        if get_patient_by_email(db, patient.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        
        db_patient = Patient()


        for attribute in vars(patient):
            setattr(db_patient, attribute, getattr(patient, attribute))

        db.add(db_patient) 
        try:   
            db.commit()
        
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=404, detail="Error occurred, please retry")


        '''update the new_patient instance with 
            any new data from the database, 
            such as auto-generated IDs or default values'''
        
        db.refresh(db_patient)

    return patient


def edit_patient(patient_id: int, updated_patient: PatientIn, db: Session):
    with db:   
        db_patient = db.get(Patient, patient_id)

        if not db_patient:
            raise HTTPException(status_code=404, detail="Error with the patient ID, please try again")

        for attribute in vars(updated_patient):
            setattr(db_patient, attribute, getattr(updated_patient, attribute))

        db.add(db_patient)
        db.commit()
        db.refresh(db_patient)

        return db_patient


def delete_patient_by_id(patient_id: int, db: Session):
    with db:
        patient = get_patient_by_id(patient_id, db)
        db.delete(patient)
        db.commit()

        return patient
    

#* Other Services
    
def get_patient_by_email(db: Session, email: str):
    return db.query(Patient).filter(Patient.email == email).first()

def get_patient_by_last_name(last_name: str, db: Session):
    return db.query(Patient).filter(Patient.last_name == last_name).all()

def get_patient_by_dob(dob: int, db: Session):
    return db.query(Patient).filter(Patient.date_of_birth_ts == dob)
