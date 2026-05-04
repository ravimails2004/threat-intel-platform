from kafka import KafkaConsumer
import json

from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry import trace

from otel import setup_otel

tracer = setup_otel()
propagator = TraceContextTextMapPropagator()

consumer = KafkaConsumer(
    "scored-events",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda m: json.loads(m.decode())
)

def extract_headers(kafka_headers):
    carrier = {}
    for k, v in kafka_headers:
        carrier[k] = v.decode()
    return carrier


for msg in consumer:
    carrier = extract_headers(msg.headers or [])
    context = propagator.extract(carrier)

    with tracer.start_as_current_span("alert_decision", context=context) as span:
        event = msg.value

        span.set_attribute("event_id", event.get("event_id"))
        span.set_attribute("risk_score", event.get("risk_score"))

        if event["risk_score"] > 0.8:
            span.set_attribute("decision", "ALERT")
            print("🚨 ALERT:", event)
        else:
            span.set_attribute("decision", "OK")
            print("OK:", event)
