from kafka import KafkaProducer
import json, time, uuid

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    event = {
        "event_id": str(uuid.uuid4()),
        "user_id": "user123",
        "ip": "1.2.3.4",
        "action": "login",
        "status": "failed"
    }
    producer.send("raw-events", event)
    print("Sent:", event)
    time.sleep(1)
