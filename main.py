# fastapi exameple app

from fastapi import FastAPI
from api.bot import bot

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "METDC"}


@app.get("/bot")
async def root():
    data = bot()
    return {"message": data}
