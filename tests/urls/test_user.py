def test_create_user(test_app_with_db):
    response = test_app_with_db.post(
        "/users/",
        json={
            "name": "Flavien",
            "email": "deadpool@example.com",
            "password": "chimichangas4life",
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert "id" in data


def test_create_existing_user(test_app_with_db):
    response = test_app_with_db.post(
        "/users/",
        json={
            "name": "Flavien",
            "email": "deadpool@example.com",
            "password": "chimichangas4life",
        },
    )

    response = test_app_with_db.post(
        "/users/",
        json={
            "name": "Flavien",
            "email": "deadpool@example.com",
            "password": "chimichangas4life",
        },
    )

    assert response.status_code == 409
