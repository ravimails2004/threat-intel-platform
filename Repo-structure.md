threat-intel-platform/
├── README.md
├── docker-compose.yaml
│
├── infra/
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
│
├── k8s/
│   ├── namespace.yaml
│   ├── kafka.yaml
│   ├── inference-deployment.yaml
│   └── hpa.yaml
│
├── services/
│   ├── ingestion-service/
│   ├── inference-service/
│   └── alert-manager/
│
├── streaming/
│   └── flink-job/
│       └── job.py
│
├── ml/
│   ├── model.py
│   └── train.py
│
├── data-contracts/
│   └── event.json
│
├── observability/
│   └── prometheus.yaml
│
└── .github/
    └── workflows/
        └── ci.yaml
