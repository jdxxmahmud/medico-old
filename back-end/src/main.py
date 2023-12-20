from fastapi import FastAPI

from routers import patient

app = FastAPI()


app.include_router(patient.router)



@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}