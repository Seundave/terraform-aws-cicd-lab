from app.main import app


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_products():
    client = app.test_client()

    response = client.get("/api/v1/products")

    assert response.status_code == 200
    assert len(response.json["products"]) > 0


def test_users():
    client = app.test_client()

    response = client.get("/api/v1/users")

    assert response.status_code == 200
    assert len(response.json["users"]) > 0


def test_orders():
    client = app.test_client()

    response = client.get("/api/v1/orders")

    assert response.status_code == 200
    assert len(response.json["orders"]) > 0