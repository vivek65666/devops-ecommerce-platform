# 🎯 Project-Based DevOps Interview Questions

1. **Why EKS?** Managed Kubernetes control plane with AWS integrations while teams manage workloads and delivery.
2. **Why ECR?** AWS-native container registry with IAM integration and image scanning.
3. **Helm vs YAML?** Helm provides templating, packaging and reusable releases.
4. **GitHub Actions vs Argo CD?** Actions handles CI; Argo CD handles GitOps delivery/reconciliation.
5. **Pod Running but 503?** Check readiness, selectors, endpoints, targetPort, listener and ingress.
6. **CrashLoopBackOff?** Repeated startup failure; inspect previous logs, events and configuration.
7. **ImagePullBackOff?** Bad image/tag, registry access or IAM/network issue.
8. **SonarQube vs Trivy?** Code quality/static analysis vs vulnerability/config/container scanning.
9. **Prometheus vs Loki?** Metrics vs logs.
10. **Why OIDC?** Avoid long-lived AWS credentials in GitHub.
11. **Rollback?** `kubectl rollout undo deployment/<app> -n ecommerce`.
12. **Terraform benefit?** Version-controlled declarative infrastructure.
13. **Production secrets?** Use AWS Secrets Manager/SSM plus a secure Kubernetes integration.
14. **What hardening is needed?** HPA, TLS, policies, backups, DR, alerts, SLOs, managed data services and least-privilege IAM.
