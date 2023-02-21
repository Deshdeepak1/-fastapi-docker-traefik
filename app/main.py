from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.db import User, database

app = FastAPI(title="FastAPI, Docker and Traefik")


@app.get("/")
async def read_root():
    return await User.objects.all()


@app.post("/file")
async def file():
    headers = {"Content-Disposition": 'attachment; filename="csv.gz"'}
    return FileResponse("csv.gz", headers=headers)


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
