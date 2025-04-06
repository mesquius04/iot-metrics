import random
import time
import json
import requests
from datetime import datetime, timedelta

# Randomized type between:
measurement_types = ["temperature", "humidity", "pressure", "light", "sound"]

def generate_data(sensor_id, num_data_points):
    base_time = datetime.utcnow()
    data = []
    
    for i in range(num_data_points):
        measurement_type = random.choice(measurement_types)
        
        timestamp = (base_time + timedelta(minutes=5 * i)).isoformat() + "Z"
        value = round(random.uniform(10.0, 50.0), 2)

        data_point = {
            "timestamp": timestamp,
            "value": value,
            "type": measurement_type
        }
        data.append(data_point)
    
    return {
        "sensorId": sensor_id,
        "type": "multi",
        "measurements": data
    }

def send_data(sensor_id, num_data_points, num_requets_points, interval_seconds):
    url = 'http://localhost:8000/data/'  # Default route

    data = generate_data(sensor_id, num_data_points)

    json_data = json.dumps(data)

    for i in range(num_requets_points):

        response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json_data)
        
        if response.status_code == 200:
            print(f"Datos enviados correctamente: {json_data}")
        else:
            print(f"Error al enviar datos: {response.status_code}")
            
        time.sleep(interval_seconds)

def main():
    sensor_id = input("Insert the sensor ID: ")
    num_data_points = int(input("¿How many data? "))
    num_requets_points = int(input("¿How many requests? "))
    interval_seconds = int(input("¿How many seconds between them? "))
    
    send_data(sensor_id, num_data_points, num_requets_points, interval_seconds)

if __name__ == "__main__":
    main()
