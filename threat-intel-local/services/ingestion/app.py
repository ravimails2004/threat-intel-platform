from kafka import KafkaProducer
import json, time, uuid

from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry import trace

from otel import setup_otel

tracer = setup_otel()
propagator = TraceContextTextMapPropagator()

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode()
)

def produce_event():
    with tracer.start_as_current_span("produce_event") as span:
        event = {
            "event_id": str(uuid.uuid4()),
            "user_id": "user1",
            "status": "failed"
        }

        span.set_attribute("event_id", event["event_id"])
        span.set_attribute("user_id", event["user_id"])

        # Inject trace context into Kafka headers
        headers = {}
        propagator.inject(headers)

        producer.send(
            "raw-events",
            value=event,
            headers=[(k, v.encode()) for k, v in headers.items()]
        )

        print("Produced:", event)


while True:
    produce_event()
    time.sleep(1)
