# 🏗️ Architecture Deep Dive

## Request path

```text
User → React → Ingress/LB → API Gateway → Business Service → PostgreSQL/Redis
```

## Delivery path

```text
GitHub → GitHub Actions → Test → SonarQube → Trivy → Docker → ECR → Argo CD → EKS
```

## Observability

```text
Application → Metrics → Prometheus → Grafana
Application → Logs → Loki → Grafana
```

Payment operations are intentionally simulated for education and must not be used for real financial transactions.
