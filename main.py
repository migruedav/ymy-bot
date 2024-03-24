# fastapi exameple app

from fastapi import FastAPI
from api.pru import pru
from api.loc import loc

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "METDC"}


@app.get("/ada")
async def root():
    return {"message": "EBR"}


@app.get("/pru")
async def root():
    return {"message": pru()}


@app.get("/loc")
async def root():
    return {"message": loc()}
