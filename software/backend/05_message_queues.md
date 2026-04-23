---
tags:
  - software
  - backend
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T15:20:41
recent_editor: CLAUDE
---

↑ [Backend Overview](./00_backend_overview.md)

# Message Queues

## What It Is

A buffer between services. The producer writes a message to the queue without waiting for the consumer to process it. The consumer reads from the queue at its own pace. This decouples the two services in time.

## Analogy

A post box. You drop letters in (produce) and walk away — you don't wait for the recipient to read them. The post office (queue) holds the letters. The recipient (consumer) picks them up when ready. Neither party needs to be available at the same time.

## How It Works

```
Producer → [Queue] → Consumer
  (API)               (Worker)
```

**Synchronous (HTTP):** producer waits for consumer to respond. If consumer is slow or down, producer is blocked.

**Async (queue):** producer writes and moves on. Consumer processes independently. If consumer is down, messages accumulate and are processed when it recovers.

**Key concepts:**

| Concept | Meaning |
|---------|---------|
| **Producer** | Service that sends messages |
| **Consumer** | Service that reads and processes messages |
| **Topic / Queue** | Named channel messages flow through |
| **Acknowledgement** | Consumer confirms it processed the message |
| **Dead letter queue** | Where messages go after repeated failure |

**Common tools:**

| Tool | Best for |
|------|---------|
| **Kafka** | High-throughput event streaming, replay, audit logs |
| **Amazon SQS** | Simple AWS-native queue, managed, easy to set up |
| **RabbitMQ** | Complex routing, lower throughput |
| **Redis Pub/Sub** | Lightweight, ephemeral (no persistence) |

## Example

User uploads a video → API writes `{ userId, videoPath }` to a queue → returns 200 immediately → transcoding worker picks up the message → processes video in the background → notifies user when done.

Without a queue: the API waits for transcoding to finish (minutes), request times out.

## Why It Matters

Message queues enable async processing, smooth out traffic spikes, and decouple services so a slow consumer doesn't block the producer. Essential for any background task: email sending, video processing, AI inference jobs.

---
↑ [Backend Overview](./00_backend_overview.md)

**Related:** [Microservices](./04_microservices.md), [Rate Limiting](./06_rate_limiting.md)
**Tags:** #software #backend
