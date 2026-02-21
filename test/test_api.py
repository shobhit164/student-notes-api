import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    res = client.get("/")
    assert res.status_code == 200


def test_create_note(client):
    res = client.post("/notes", json={
        "title": "Test Note",
        "content": "CI/CD test"
    })
    assert res.status_code == 201
    data = res.get_json()
    assert data["title"] == "Test Note"


def test_get_notes(client):
    # Create a note first
    client.post("/notes", json={"title": "A", "content": "B"})
    res = client.get("/notes")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_update_note(client):
    # Create a note first
    client.post("/notes", json={"title": "Old", "content": "Content"})
    res = client.put("/notes/1", json={"title": "Updated", "content": "New"})
    assert res.status_code == 200
    data = res.get_json()
    assert data["title"] == "Updated"


def test_delete_note(client):
    # Create a note first
    client.post("/notes", json={"title": "ToDelete", "content": "Delete me"})
    res = client.delete("/notes/1")
    assert res.status_code == 200
    data = res.get_json()
    assert data["message"] == "Deleted"