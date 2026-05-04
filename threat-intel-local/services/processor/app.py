from kafka import KafkaConsumer, KafkaProducer
import json, requests

# OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

span_processor = BatchSpanProcessor(
    OTLPSpanExporter(endpoint="http://otel-collector:4318/v1/traces")
)
trace.get_tracer_provider().add_span_processor(span_processor)

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
    with tracer.start_as_current_span("process_event") as span:
        event = msg.value

        features = [
            len(event["user_id"]),
            1 if event["status"] == "failed" else 0
        ]

        span.set_attribute("user_id", event["user_id"])

        r = requests.post("http://inference:8000/infer", json={"features": features})
        event["risk_score"] = r.json()["risk_score"]

        producer.send("scored-events", event)
