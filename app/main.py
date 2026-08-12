from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/api/v1/products")
def products():
    return jsonify(
        {
            "products": [
                {"id": 1, "name": "Laptop"},
                {"id": 2, "name": "Phone"},
            ]
        }
    ), 200


@app.get("/api/v1/users")
def users():
    return jsonify(
        {
            "users": [
                {"id": 1, "name": "David"},
            ]
        }
    ), 200


@app.get("/api/v1/orders")
def orders():
    return jsonify(
        {
            "orders": [
                {"id": 1, "status": "completed"},
            ]
        }
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
