import paho.mqtt.client as mqtt
import json
import time
import random

broker = "test.mosquitto.org"
topic = "iot/sensor/temp"

client = mqtt.Client("SimSensor")
client.connect(broker, 1883)

for _ in range(5):  # simulate 5 readings
    temp = round(random.uniform(20.0, 35.0), 2)
    payload = json.dumps({"device_id": "sensor1", "temperature": temp})
    client.publish(topic, payload)
    print(f"[PUBLISH] {payload}")
    time.sleep(3)
