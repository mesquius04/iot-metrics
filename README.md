# IoT-Metrics

This demo demonstrates how **MongoDB** and **FastAPI** can be used to efficiently process different types of data coming from several different IoT sensors.

## Why MongoDB?

Data comming from real-world sensors (often used for *Predictive Maintenance*) usually varies a lot. The easiest way I have found to illustrate this is by considering a project that uses sensors from four different generations. Some of them might include more or less metadata, relationships, alerts, and other elements that we might want to store.

MongoDB allows us to avoid being 'stuck' in a very rigid schema.

Horizontal scalability, sharding, reliability, and compatibility with other Big Data tools, such as Kafka, Spark, or TensorFlow, were also considered in the choice.

## How to run the DEMO?

### Requirements

- Docker
- Python
- curl
- `requests` pip module

### Step 0

Clone this repo on your local machine using:

> git clone https://github.com/mesquius04/iot-metrics.git

### Step 1

Start the Docker containers (MongoDB and FastAPI/backend) with:

> docker compose up

### Step 2

You are done! Now have fun testing the endpoints. You will find all of them in: **http://localhost:8000/docs**

## Example

Now consider we have a sensor with ID *temp-001*. We can post a metric by using:

```bash
curl -X 'POST'   'http://localhost:8000/data/'   -H 'Content-Type: application/json'   -d '{
  "sensorId": "temp-001",
  "type": "temperature",
  "measurements": [
    { "timestamp": "2025-04-06T08:00:00Z", "value": 42.5, "type": "temperature" },
    { "timestamp": "2025-04-06T08:05:00Z", "value": 32.8, "type": "temperature" }
  ]
}'
```

You can see all the metrics from a sensor with:

```bash
curl -X 'GET'   'http://localhost:8000/data/temp-001'   -H 'accept: application/json'
```

If you worry about your sensor, you can use:

```bash
curl -X 'GET'   'http://localhost:8000/data/temp-001/log'   -H 'accept: application/json'
```

To access the complete logs for every post.

Finally, you can use `./client/sensor.py` to automate posting from your local device.

```bash
cd client

python3 simulator.py
Insert the sensor ID: sensor_1
¿How many data? 8
¿How many requests? 3
¿How many seconds between them? 2
```

*Project inspired in Apache Kafka.*