from flask import Flask, jsonify
import time
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Checkout API is running"

@app.route("/health")
def health():
    return jsonify(status="healthy")

@app.route("/checkout")
def checkout():
    delay = int(os.getenv("CHECKOUT_DELAY_MS", "100"))

    time.sleep(delay / 1000)

    return jsonify(
        status="success",
        message="Checkout completed"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
