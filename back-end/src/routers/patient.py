from fastapi import APIRouter, HTTPException
from schemas.patient_schema import PatientBase, PatientIn, PatientOut


router = APIRouter(
    prefix="/patient",
    tags=["patient"],
    responses={404: {"description": "Not found"}},
)


fake_patient_db = {"1": {"id": 1,
                       "name": "Morgan"}, 
                   "2": {"id": 2,
                       "name": "Freeman"}}


@router.get("/")
async def read_items():
    return fake_patient_db


@router.get("/{patient_id}")
async def read_item(patient_id: str):
    if patient_id not in fake_patient_db:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"patient": fake_patient_db[patient_id]["name"], "patient_id": patient_id}


@router.put(
    "/{patient_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_patient(patient_id: str, patient: PatientIn):
    if patient_id != "1":
        raise HTTPException(
            status_code=403, detail="You can only update the item: 1"
        )
    return patient