from fastapi import FastAPI
from routes import sensors

app = FastAPI()


app.include_router(sensors.router, prefix="/data", tags=["Sensors"])