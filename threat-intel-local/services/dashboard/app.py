from flask import Flask, jsonify
from kafka import KafkaConsumer
import json, threading

app = Flask(__name__)
alerts = []

def consume():
    consumer = KafkaConsumer(
        "scored-events",
        bootstrap_servers="kafka:9092",
        value_deserializer=lambda m: json.loads(m.decode())
    )

    for msg in consumer:
        event = msg.value
        if event["risk_score"] > 0.8:
            alerts.append(event)

threading.Thread(target=consume, daemon=True).start()

@app.route("/alerts")
def get_alerts():
    return jsonify(alerts)

app.run(host="0.0.0.0", port=5000)
