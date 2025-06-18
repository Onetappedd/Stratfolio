import os
import sys
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import app

client = TestClient(app)

def test_generate_endpoint():
    response = client.post("/generate", json={"risk_level": "Moderate", "amount": 1000, "use_api": False})
    assert response.status_code == 200
    data = response.json()
    assert "stocks" in data and "bonds" in data and "cash" in data

def test_generate_invalid_risk():
    response = client.post("/generate", json={"risk_level": "Bad", "amount": 1000, "use_api": False})
    assert response.status_code == 400
