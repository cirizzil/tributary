import requests as requests

data = {
    "engine_temperature": 0.3,
}

response = requests.post("http://localhost:8000/record", json=data)
print(response.content)
