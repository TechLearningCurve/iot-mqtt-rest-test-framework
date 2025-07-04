# iot-mqtt-rest-test-framework
# Mini IoT Test Framework

This is a simple IoT testing framework that simulates a device using MQTT, validates cloud data using REST API, and performs automated testing with Pytest.

## Features
- Simulate sensor data using MQTT (`mqtt_publisher.py`)
- Validate backend via REST API (`api_validator.py`)
- Automated pipeline test (`test_iot_pipeline.py`)
- Pytest + HTML reports

## Setup

```bash
git clone https://github.com/TechLearningCurve/iot-mqtt-rest-test-framework.git
cd iot-mqtt-rest-test-framework
pip install -r requirements.txt