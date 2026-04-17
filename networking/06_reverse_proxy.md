---
tags:
  - networking
created_at: 2026-04-14
updated_at: 2026-04-17
---
# Reverse Proxy

## What It Is

A reverse proxy is a server that sits in front of one or more backend servers and forwards client requests to them. From the client's perspective, it looks like a single server — the backends are hidden.

```
Client → Reverse Proxy → Backend Server A
                       → Backend Server B
                       → Backend Server C
```

Contrast with a **forward proxy**: a forward proxy acts on behalf of the *client* (e.g., to anonymize or filter outbound traffic). A reverse proxy acts on behalf of the *server*.

For HTTP fundamentals used by reverse proxies, see [HTTP](05_http.md). For load balancing as a specific reverse proxy use case, see [ELB](../aws/101/aws_services/16_elastic_load_balancing.md).

## Analogy

A hotel front desk. Guests (clients) always talk to the front desk (reverse proxy). The front desk routes requests to housekeeping, room service, or concierge (backends). Guests never call those departments directly.

## How It Works

1. Client sends a request to the reverse proxy's IP/domain.
2. The proxy inspects the request (URL path, hostname, headers).
3. It forwards the request to the appropriate backend.
4. The backend responds to the proxy, which returns the response to the client.

The client only ever sees the proxy's address — backend IPs remain internal.

### Core Capabilities

| Capability | What It Does | Example |
|-----------|-------------|---------|
| **Load balancing** | Distribute requests across backends | Round-robin across 3 app servers |
| **TLS termination** | Decrypt HTTPS once at the proxy; backends use plain HTTP internally | Nginx handles TLS, forwards to `localhost:3000` |
| **Caching** | Store responses and serve them without hitting backends | Cache static assets for 24 hours |
| **Compression** | Gzip responses before sending to client | Reduce JSON payload size |
| **Path routing** | Route `/api/*` to one service, `/static/*` to another | Microservices behind one domain |
| **Rate limiting** | Reject or throttle excess requests | Max 100 req/s per IP |
| **Authentication** | Verify identity before forwarding | OAuth token check at the proxy |
| **IP whitelisting / blocking** | Allow or deny by IP at the edge | Block known bad IPs before they reach your app |

### When to Use a Reverse Proxy

- You have **multiple backend services** and want a single entry point.
- You want to **offload TLS** from application code.
- You need **caching** close to users without changing app logic.
- You need **rate limiting or auth** applied uniformly across services.
- You want to **hide backend topology** (IPs, ports, server count).
- You need **zero-downtime deploys** by shifting traffic gradually.

### Common Tools

| Tool | Typical Use |
|------|------------|
| **Nginx** | High-performance reverse proxy and static file server |
| **HAProxy** | TCP/HTTP load balancing, fine-grained health checks |
| **Caddy** | Automatic TLS, simple config, good for small deployments |
| **Traefik** | Docker/Kubernetes-native, auto-discovers services |
| **AWS ALB** | Managed reverse proxy + load balancer on AWS |
| **AWS CloudFront** | CDN with reverse proxy behavior at edge locations |
| **AWS API Gateway** | Managed reverse proxy for serverless and REST APIs |

## Example

Single domain, two microservices using Nginx:

```nginx
server {
    listen 443 ssl;
    server_name api.example.com;

    location /users/ {
        proxy_pass http://user-service:8080;
    }

    location /orders/ {
        proxy_pass http://order-service:8081;
    }
}
```

The client calls `https://api.example.com/users/1`. Nginx terminates TLS, matches `/users/`, and forwards to `user-service:8080` — the client never knows the internal port or host.

## Why It Matters

Almost every production web system uses a reverse proxy. On AWS, [ALB](../aws/101/aws_services/16_elastic_load_balancing.md) is a managed reverse proxy for EC2 and containers; [CloudFront](../aws/101/aws_services/21_amazon_cloudfront.md) is a reverse proxy at the CDN edge; [API Gateway](../aws/101/aws_services/07_aws_lambda.md) is a reverse proxy for Lambda. Understanding what a reverse proxy does explains *why* these services exist and which one to pick.

---
← Previous: [HTTP](05_http.md) | [Overview](00_overview.md) | Next: →
