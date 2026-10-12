# 🚀 Deployment Runbook

## Local

```bash
docker compose -f docker/docker-compose.yml up --build
```

## Terraform

```bash
cd terraform
terraform init
terraform fmt -recursive
terraform validate
terraform plan
```

Review all costs, IAM permissions, networking and security before `terraform apply`.

## Helm

```bash
helm lint helm/ecommerce
helm upgrade --install ecommerce helm/ecommerce -n ecommerce --create-namespace
```

## GitOps

Update `argocd/application.yaml` with your repository/ECR values and apply it after installing Argo CD.
