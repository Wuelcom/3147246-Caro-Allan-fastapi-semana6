def test_create_event(client):
    data = {
        "nombre": "Concierto Bogotá",
        "fecha": "2025-10-15",
        "ubicacion": "Movistar Arena",
        "descripcion": "Concierto de rock",
        "capacidad": 5000
    }
    response = client.post("/event_eventos/", json=data)
    assert response.status_code == 201
    assert response.json()["nombre"] == "Concierto Bogotá"

def test_get_events(client):
    response = client.get("/event_eventos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
