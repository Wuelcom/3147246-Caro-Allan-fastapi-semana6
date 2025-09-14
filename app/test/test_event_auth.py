def test_register_event_user(client):
    data = {
        "username": "organizador_test",
        "password": "password123",
        "role": "organizador_evento"
    }
    response = client.post("/auth/register", json=data)
    assert response.status_code == 201

def test_login_event_user(client):
    register_data = {
        "username": "admin_event",
        "password": "admin123",
        "role": "admin_evento"
    }
    client.post("/auth/register", json=register_data)

    login_data = {
        "username": "admin_event",
        "password": "admin123"
    }
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_only_admin_can_delete_event(client):
    # Aquí deberías crear un token de admin_evento
    # y verificar que solo con ese se pueda eliminar
    pass
