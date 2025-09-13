import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestPhotoAPI:
    def test_photo_create_sesion(self):
        data = {
            "id_usuario": 1,
            "fecha": "2025-09-20",
            "ubicacion": "Parque Central",
            "tipo_sesion": "Boda",
            "duracion_horas": 3,
            "precio": 500000,
            "estado": "Confirmada"
        }
        response = client.post("/photo/sesiones/", json=data)
        assert response.status_code == 201
        assert response.json()["tipo_sesion"] == "Boda"

    def test_photo_get_sesion_not_found(self):
        response = client.get("/photo/sesiones/9999")
        assert response.status_code == 404
        assert "Sesión no encontrada" in response.json()["detail"]

    def test_photo_precio_invalido(self):
        data = {
            "id_usuario": 1,
            "fecha": "2025-09-21",
            "ubicacion": "Estudio Central",
            "tipo_sesion": "Retrato",
            "duracion_horas": 2,
            "precio": -100,
            "estado": "Pendiente"
        }
        response = client.post("/photo/sesiones/", json=data)
        assert response.status_code == 422

    def test_photo_duracion_invalida(self):
        data = {
            "id_usuario": 1,
            "fecha": "2025-09-22",
            "ubicacion": "Playa Blanca",
            "tipo_sesion": "15 años",
            "duracion_horas": 0,
            "precio": 300000,
            "estado": "Pendiente"
        }
        response = client.post("/photo/sesiones/", json=data)
        assert response.status_code == 422
