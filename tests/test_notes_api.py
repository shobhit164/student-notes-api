def test_health_check(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_create_and_fetch_note(client):
    create_response = client.post(
        "/api/notes",
        json={
            "title": "Midterm Revision",
            "content": "Review CI/CD concepts and GitHub Actions.",
            "course": "CSD-4503",
        },
    )

    assert create_response.status_code == 201
    note = create_response.get_json()
    assert note["title"] == "Midterm Revision"

    get_response = client.get(f"/api/notes/{note['id']}")
    assert get_response.status_code == 200
    assert get_response.get_json()["course"] == "CSD-4503"


def test_list_notes_returns_created_notes(client):
    client.post(
        "/api/notes",
        json={
            "title": "Sprint 1",
            "content": "Create Flask CRUD routes.",
            "course": "DevOps",
        },
    )

    response = client.get("/api/notes")
    payload = response.get_json()

    assert response.status_code == 200
    assert len(payload) == 1
    assert payload[0]["title"] == "Sprint 1"


def test_update_note(client):
    create_response = client.post(
        "/api/notes",
        json={
            "title": "Old Title",
            "content": "Old content",
            "course": "Course A",
        },
    )
    note_id = create_response.get_json()["id"]

    update_response = client.put(
        f"/api/notes/{note_id}",
        json={
            "title": "Updated Title",
            "content": "Updated content",
            "course": "Course B",
        },
    )

    assert update_response.status_code == 200
    assert update_response.get_json()["title"] == "Updated Title"


def test_delete_note(client):
    create_response = client.post(
        "/api/notes",
        json={
            "title": "Delete Me",
            "content": "Temporary note",
            "course": "Course C",
        },
    )
    note_id = create_response.get_json()["id"]

    delete_response = client.delete(f"/api/notes/{note_id}")
    assert delete_response.status_code == 200

    get_response = client.get(f"/api/notes/{note_id}")
    assert get_response.status_code == 404


def test_create_note_validates_missing_fields(client):
    response = client.post(
        "/api/notes",
        json={"title": "Incomplete"},
    )

    assert response.status_code == 400
    assert "Missing required fields" in response.get_json()["error"]

