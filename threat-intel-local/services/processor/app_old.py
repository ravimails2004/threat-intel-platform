from kafka import KafkaConsumer, KafkaProducer
import json, requests

consumer = KafkaConsumer(
    "raw-events",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda m: json.loads(m.decode())
)

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode()
)

for msg in consumer:
    event = msg.value

    features = [
        len(event["user_id"]),
        1 if event["status"] == "failed" else 0
    ]

    r = requests.post("http://inference:8000/infer", json={"features": features})
    event["risk_score"] = r.json()["risk_score"]

    producer.send("scored-events", event)
    print("Processed:", event)
