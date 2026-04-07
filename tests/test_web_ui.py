def test_homepage_renders_dashboard(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Student Notes Dashboard" in response.data
    assert b"Create Note" in response.data


def test_ui_can_create_edit_and_delete_note(client):
    create_response = client.post(
        "/notes/create",
        data={
            "title": "Lecture Summary",
            "content": "Reviewed deployment automation.",
            "course": "CSD-4503",
        },
        follow_redirects=True,
    )
    assert create_response.status_code == 200
    assert b"Lecture Summary" in create_response.data

    update_response = client.post(
        "/notes/1/edit",
        data={
            "title": "Lecture Summary Updated",
            "content": "Reviewed CI, CD, and Azure deployment.",
            "course": "CSD-4503",
        },
        follow_redirects=True,
    )
    assert update_response.status_code == 200
    assert b"Lecture Summary Updated" in update_response.data

    delete_response = client.post("/notes/1/delete", follow_redirects=True)
    assert delete_response.status_code == 200
    assert b"Lecture Summary Updated" not in delete_response.data
