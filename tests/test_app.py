from app.app import app


def test_home_page():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    data = res.get_json()
    assert data["app"] == "ACEest Fitness & Gym Manager"
    assert "version" in data


def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "UP"


def test_get_and_add_routine():
    client = app.test_client()
    res_get = client.get("/routines")
    assert res_get.status_code == 200

    res_post = client.post("/routines", json={"name": "HIIT Session", "category": "Cardio"})
    assert res_post.status_code == 201
    assert res_post.get_json()["routine"]["name"] == "HIIT Session"

    res_bad = client.post("/routines", json={})
    assert res_bad.status_code == 400
