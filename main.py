# fastapi exameple app

from fastapi import FastAPI
from api.bot import bot
from api.prueba import prueba

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "METC"}


@app.get("/bot")
async def root():
    data = bot()
    return {"message": data}


@app.get("/prueba")
async def root():
    data = prueba()
    return {"message": data}
