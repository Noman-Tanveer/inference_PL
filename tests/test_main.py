
# Unit tests and integration tests
import requests
from fastapi.testclient import TestClient
from app.main import app

# Create a FastAPI test client
client = TestClient(app)

def test_read_main():
    # Send a GET request to the default API route
    response = client.get("/")
    # Assert the response status code (200 OK)
    assert response.status_code == 200
    # Assert the response content
    assert response.json() == {"Hello": "World"}

def test_read_items():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": None}

    response = client.get("/items/2?q=foo")
    assert response.status_code == 200
    assert response.json() == {"item_id": 2, "q": "foo"}

    response = client.get("/items/3?q=bar")
    assert response.status_code == 200
    assert response.json() == {"item_id": 3, "q": "bar"}

def test_detect_image():
    # Load an image as bytes (you can read an image file using open() in binary mode)
    with open("resources/maxresdefault.jpg", "rb") as image_file:
        image_bytes = image_file.read()
    # Send a POST request to the process-image endpoint
    response = client.get("/detect/", files={"image_bytes": ("resources/maxresdefault.jpg", image_bytes)})
    # Check the response
    assert response.status_code == 200
