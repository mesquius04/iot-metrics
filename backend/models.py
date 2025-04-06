from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Measurement(BaseModel):
    timestamp: datetime
    value: float
    type: str

class Sensor(BaseModel):
    sensorId: str
    type: str
    location: Optional[dict] = None
    measurements: List[Measurement]

    class Config:
        orm_mode = True
