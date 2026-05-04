import os

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def setup_otel():
    # Read from environment (standard OTEL way)
    service_name = os.getenv("OTEL_SERVICE_NAME", "unknown-service")

    # Optional: parse additional resource attributes
    resource_attributes = {
        "service.name": service_name
    }

    # Support OTEL_RESOURCE_ATTRIBUTES like: key1=val1,key2=val2
    extra_attrs = os.getenv("OTEL_RESOURCE_ATTRIBUTES")
    if extra_attrs:
        for item in extra_attrs.split(","):
            if "=" in item:
                k, v = item.split("=", 1)
                resource_attributes[k.strip()] = v.strip()

    resource = Resource.create(resource_attributes)

    # Create provider with resource
    provider = TracerProvider(resource=resource)

    # OTLP HTTP exporter (4318)
    exporter = OTLPSpanExporter(
        endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://otel-collector:4318/v1/traces")
    )

    processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(processor)

    trace.set_tracer_provider(provider)

    return trace.get_tracer(service_name)
