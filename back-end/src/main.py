from fastapi import FastAPI

from routers import patient, doctor

app = FastAPI()


app.include_router(patient.router)
app.include_router(doctor.router)



@app.get("/")
async def root():
    return {"message": "Hello Medico!"}