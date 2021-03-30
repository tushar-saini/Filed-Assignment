from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# Test index page
def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to the Audio book API."

# Testing create test
def test_create():
    response = client.put(
        "/create/song/",
        json={"id": 101, "name": "test", "duration": 5, "uploadtime": "2020/04/19"}
    )
    assert response.status_code == 200

# Testing duplicate entry
def test_duplicate():
    response = client.put(
        "/create/song/",
        json={"id": 101, "name": "test", "duration": 5, "uploadtime": "2020/04/19"}
    )
    assert response.status_code == 400
    assert response.json() == {"detail" : "Duplicate Error"}

# Testing get api
def test_get():
    response = client.put("/get/song?id=101")
    assert response.status_code == 200

# Testing delete api
def test_delete():
    response = client.put("/delete/song?id=101")
    assert response.status_code == 200
    assert response.json() == {"response" : "Delete successful!"}
