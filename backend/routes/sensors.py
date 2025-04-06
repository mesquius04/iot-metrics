from fastapi import APIRouter
from models import Sensor, Measurement
from db import measurements_collection
from bson import ObjectId
from fastapi.responses import JSONResponse

router = APIRouter()

def convert_objectid_to_str(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj

def serialize_document(document):
    return {key: convert_objectid_to_str(value) for key, value in document.items()}

@router.get("/{sensor_id}")
async def get_sensor_data(sensor_id: str):

    sensor_data = measurements_collection.find_one({"sensorId": sensor_id})
    
    if not sensor_data:
        return JSONResponse(status_code=404, content={"message": "not_found"})
    
    serialized_data = serialize_document(sensor_data)
    
    return serialized_data

router = APIRouter()

@router.post("/")
async def create_sensor_data(sensor: Sensor):

    sensor_data = {
        "sensorId": sensor.sensorId,
        "type": sensor.type,
        "location": sensor.location,
        "measurements": [{"timestamp": m.timestamp, "value": m.value, "type": m.type} for m in sensor.measurements],
    }
    result = measurements_collection.insert_one(sensor_data)
    return {"message": "data_inserted", "id": str(result.inserted_id)}

@router.get("/{sensor_id}/log")
async def get_sensor_log(sensor_id: str):

    sensor_data = measurements_collection.find({"sensorId": sensor_id})

    if not sensor_data:
        return JSONResponse(status_code=404, content={"message": "not_found"})
    
    serialized_data = [serialize_document(data) for data in sensor_data]

    return {"sensorId": sensor_id, "data": serialized_data}

@router.get("/{sensor_id}")
async def get_sensor_data(sensor_id: str):
    sensor_data = measurements_collection.find({"sensorId": sensor_id})
    
    if not sensor_data:
        return JSONResponse(status_code=404, content={"message": "not_found"})

    serialized_measurements = []

    for data in sensor_data:
        measurements = data.get("measurements", [])
        
        for measurement in measurements:
            serialized_measurements.append({
                "timestamp": measurement.get("timestamp"),
                "value": measurement.get("value"),
                "type": measurement.get("type"),
            })

    return {"sensorId": sensor_id, "measurements": serialized_measurements}
