from sqlalchemy.orm import Session

from models.doctor_model import Doctor


def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Doctor).offset(skip).limit(limit).all()