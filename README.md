# Threat Intelligence Platform (GPU-based)

## Overview
Real-time AI-driven threat detection system using:
- Kafka (streaming)
- Flink (processing)
- GPU inference (PyTorch)
- Kubernetes (deployment)

## Quick Start

```bash
docker-compose up

## Services
- ingestion-service → produces events
- flink-job → processes events
- inference-service → GPU scoring
- alert-manager → triggers alerts

---

# 🐳 4. Local Dev Setup (docker-compose.yaml)

```yaml
version: '3.8'

services:
  zookeeper:
    image: confluentinc/cp-zookeeper
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181

  kafka:
    image: confluentinc/cp-kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092

  ingestion:
    build: ./services/ingestion-service

  inference:
    build: ./services/inference-service
