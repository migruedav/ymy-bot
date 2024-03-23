# fastapi exameple app

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "METC"}
