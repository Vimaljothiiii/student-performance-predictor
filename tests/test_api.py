import sys
import os

sys.path.append(os.path.abspath("backend"))

from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_prediction():
    client = app.test_client()

    response = client.post("/predict", json={
        "study_hours": 6,
        "attendance": 80,
        "previous_score": 65,
        "assignment_score": 70
    })

    assert response.status_code == 200

    data = response.get_json()

    assert "prediction" in data