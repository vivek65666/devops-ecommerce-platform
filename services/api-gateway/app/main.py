import os
import httpx
from fastapi import FastAPI, HTTPException, Request
from prometheus_fastapi_instrumentator import Instrumentator
app=FastAPI(title="E-Commerce API Gateway", version="1.0.0", redirect_slashes=False)
Instrumentator().instrument(app).expose(app)
SERVICES={
 "users":os.getenv("USER_SERVICE_URL","http://user-service:8001"),
 "products":os.getenv("PRODUCT_SERVICE_URL","http://product-service:8002"),
 "cart":os.getenv("CART_SERVICE_URL","http://cart-service:8003"),
 "orders":os.getenv("ORDER_SERVICE_URL","http://order-service:8004"),
 "payments":os.getenv("PAYMENT_SERVICE_URL","http://payment-service:8005"),
 "notifications":os.getenv("NOTIFICATION_SERVICE_URL","http://notification-service:8006")}
@app.get("/health")
def health(): return {"status":"ok","service":"api-gateway"}
@app.get("/ready")
def ready(): return {"ready":True}
@app.get("/api/v1/services")
def services(): return {"services":SERVICES}
@app.api_route("/api/v1/{service}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
@app.api_route("/api/v1/{service}/{path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def proxy(service: str, path: str = "", request: Request = None):
    base = SERVICES.get(service)
    if not base:
        raise HTTPException(404, "Unknown service")
    
    # Build target URL depending on whether a sub-path exists
    if path:
        target = f"{base}/api/v1/{service}/{path}"
    else:
        target = f"{base}/api/v1/{service}"
        
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.request(
                request.method,
                target,
                content=await request.body(),
                headers={"content-type": request.headers.get("content-type", "application/json")}
            )
    except httpx.RequestError as e:
        raise HTTPException(502, f"Upstream unavailable: {e}")
        
    return r.json() if r.content else {"status": r.status_code}
