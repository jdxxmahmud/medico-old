from sqlalchemy.orm import Session

from models.patient_model import Patient


def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Patient).offset(skip).limit(limit).all()