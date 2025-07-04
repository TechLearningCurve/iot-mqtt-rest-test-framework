import requests

API_URL = "https://mock-api.com/device/sensor1/last-reading" 

response = requests.get(API_URL)
data = response.json()

print(f"[VALIDATE] Got data from API: {data}")
assert "temperature" in data and 20 <= data["temperature"] <= 35
print("[VALIDATE] Data validation successful.")