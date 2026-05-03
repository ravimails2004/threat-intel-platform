# Repository Structure

```text

threat-intel-platform/
│
├── apps/                          # All deployable workloads
│   ├── ingestion-service/
│   ├── feature-service/
│   ├── inference-service/
│   ├── alert-manager/
│   └── soar-executor/
│
├── streaming/
│   ├── flink-jobs/
│   └── kafka-connect/
│
├── ml/
│   ├── training/
│   ├── serving/                  # Triton / TorchServe configs
│   ├── registry/                 # Model metadata
│   └── feature-store/
│
├── platform/
│   ├── auth/                     # OIDC / IAM integration
│   ├── config/                   # centralized config (env/consul)
│   └── common-lib/
│
├── infra/
│   ├── terraform/
│   │   ├── modules/
│   │   │   ├── eks/
│   │   │   ├── kafka-msk/
│   │   │   ├── flink/
│   │   │   └── gpu-nodegroup/
│   │   └── envs/{dev,staging,prod}
│   │
│   └── policies/                 # OPA / Sentinel
│
├── k8s/
│   ├── base/
│   ├── overlays/{dev,staging,prod}   # Kustomize
│   ├── helm/
│   └── argocd/                   # GitOps
│
├── observability/
│   ├── metrics/                  # Prometheus rules
│   ├── logs/                     # OpenSearch configs
│   ├── tracing/                  # Jaeger/Tempo
│   └── dashboards/               # Grafana JSON
│
├── security/
│   ├── rbac/
│   ├── network-policies/
│   ├── secrets/                  # External Secrets
│   └── compliance/               # RBI / PCI controls mapping
│
├── data-contracts/
│   ├── schemas/
│   └── registry/                 # schema registry config
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── chaos/
│
├── scripts/
│   ├── bootstrap.sh
│   └── load-test.sh
│
└── .github/workflows/

```
