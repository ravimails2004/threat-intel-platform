from fastapi import FastAPI, Request
import random

from opentelemetry import trace
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

from otel import setup_otel

app = FastAPI()

tracer = setup_otel("inference-service")
propagator = TraceContextTextMapPropagator()


@app.post("/infer")
async def infer(request: Request):
    # Extract trace context from incoming request headers
    context = propagator.extract(dict(request.headers))

    with tracer.start_as_current_span("infer_request", context=context) as span:
        body = await request.json()

        features = body.get("features", [])

        score = 0.5 + random.random() * 0.5

        span.set_attribute("features_length", len(features))
        span.set_attribute("risk_score", score)

        return {"risk_score": round(score, 2)}
