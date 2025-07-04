import requests
import subprocess
import time

def test_iot_pipeline():
    # Run MQTT Publisher
    subprocess.run(["python", "mqtt_publisher.py"])
    time.sleep(5)  # Give time for backend processing

    # Validate via REST API
    response = requests.get("https://mock-api.com/device/sensor1/last-reading")
    data = response.json()

    assert "temperature" in data
    assert 20 <= data["temperature"] <= 35
    print(f"[PASS] Temperature is {data['temperature']}")
