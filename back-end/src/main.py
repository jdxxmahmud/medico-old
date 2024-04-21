from fastapi import FastAPI

from db.database import recreate_database
from routers import patient, doctor

app = FastAPI()


app.include_router(patient.router)
# app.include_router(doctor.router)


@app.on_event("startup")
def startup_event():
    recreate_database()

@app.get("/")
async def root():
    return {"message": "Hello Medico!"}


