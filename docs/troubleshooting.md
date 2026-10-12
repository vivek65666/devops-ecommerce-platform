# 🧪 Production Troubleshooting Runbook

## 503 Service Unavailable

```bash
kubectl get pods -n ecommerce
kubectl describe pod <pod> -n ecommerce
kubectl get svc -n ecommerce
kubectl get endpoints -n ecommerce
kubectl logs <pod> -n ecommerce
```

If endpoints are empty:

```bash
kubectl get pods -n ecommerce --show-labels
kubectl get svc <service> -n ecommerce -o yaml
```

## CrashLoopBackOff

```bash
kubectl logs <pod> -n ecommerce --previous
kubectl describe pod <pod> -n ecommerce
kubectl get events -n ecommerce --sort-by=.lastTimestamp
```

Common causes: bad configuration, app exceptions, missing dependencies, database failures, wrong startup command, memory pressure.

## ImagePullBackOff

Inspect image/tag, ECR access, node IAM and registry connectivity.

## Rollback

```bash
kubectl rollout history deployment/<app> -n ecommerce
kubectl rollout undo deployment/<app> -n ecommerce
kubectl rollout status deployment/<app> -n ecommerce
```

## OOMKilled

```bash
kubectl describe pod <pod> -n ecommerce
kubectl top pod -n ecommerce
kubectl top node
```
