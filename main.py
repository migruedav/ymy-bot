# fastapi exameple app

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "METDC"}


@app.get("/ada")
async def root():
    return {"message": "EBR"}
