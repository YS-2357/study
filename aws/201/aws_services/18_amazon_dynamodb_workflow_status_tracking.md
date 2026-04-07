# Amazon DynamoDB — Workflow Status Tracking

## What It Is

Amazon DynamoDB is often used as a status store for work items such as jobs, orders, uploads, or agent runs because it gives key-value lookups with single-digit millisecond performance and scales without server management, as described in the [AWS DynamoDB developer guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html). In practice, teams store a work item ID as the key and keep fields like `status`, `updated_at`, `worker_id`, and `result`.

See also: [Amazon DynamoDB (101)](../../101/aws_services/12_amazon_dynamodb.md) and [DynamoDB TTL and Session Store](14_amazon_dynamodb_ttl.md)

## Analogy

Think of DynamoDB like a warehouse tracking board where each box has one card. The card does not hold the full business process, but it does tell everyone whether that box is `pending`, `processing`, `done`, or `failed`, and who touched it last.

## How It Works

People use DynamoDB for workflow status because the access pattern is usually simple:

1. Write a new item with status `pending`.
2. A worker reads the item by its ID.
3. The worker updates the item to `processing`.
4. The worker finishes and updates the item to `done` or `failed`.

This fits DynamoDB well because workflow state is usually a direct key lookup or update, not a relational query with joins.

### Typical item shape

```json
{
  "job_id": "job_123",
  "status": "processing",
  "updated_at": "2026-04-07T10:15:00Z",
  "worker_id": "worker-a",
  "result_s3_key": null
}
```

### Why DynamoDB works well here

- Fast point reads and writes: a worker usually knows the exact `job_id`, so it can read or update that single item directly.
- Safe state transitions: DynamoDB supports condition expressions on `PutItem`, `UpdateItem`, and `DeleteItem`, so you can say "only move this job to `processing` if it is still `pending`" as documented in [Condition and filter expressions, operators, and functions in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html).
- Event hooks after status changes: DynamoDB Streams provides item-level change data capture in near real time, which is useful when a `done` item should trigger the next step, as described in [Change data capture for DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/streamsmain.html).
- Low operational overhead: you do not run database servers, patch them, or shard them yourself; DynamoDB is a managed service per the [AWS DynamoDB developer guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html).

### Common pattern: conditional claim

The important part is not just storing `status`, but updating it safely so two workers do not claim the same job at once.

```python
table.update_item(
    Key={"job_id": "job_123"},
    UpdateExpression="SET #s = :processing, worker_id = :worker, updated_at = :ts",
    ConditionExpression="#s = :pending",
    ExpressionAttributeNames={"#s": "status"},
    ExpressionAttributeValues={
        ":pending": "pending",
        ":processing": "processing",
        ":worker": "worker-a",
        ":ts": "2026-04-07T10:15:00Z",
    },
)
```

If the item is no longer `pending`, the update fails instead of silently letting two workers process the same job. That is exactly the kind of guard condition DynamoDB condition expressions are for in the [AWS docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html).

## Example

Imagine an image-processing pipeline:

- API writes `job_123` with `status = pending`
- Worker A tries to claim `job_123`
- DynamoDB conditionally changes it to `processing`
- Worker A finishes resizing the image and updates the item to `done`
- A DynamoDB Stream consumer notices the change and sends a notification

This is why people often pick DynamoDB for "pending / processing / done" tracking: the table is small, the lookup is by ID, the status update must be atomic, and later systems may need to react to item changes.

## Why It Matters

DynamoDB is a good fit when workflow state is mostly "look up one item by ID and change a few fields." It becomes especially attractive when you need atomic status transitions, very high write throughput, or stream-based reactions after updates.

It is not used because status values are special. It is used because many workflow systems are really just high-volume key-value state machines, and DynamoDB is strong at that shape of problem.

> **Tip:** If the workflow requires many joins, ad hoc reporting, or complex queries across many dimensions, DynamoDB may stop being a good fit. In that case, keep the hot workflow state in DynamoDB and move reporting or analytics elsewhere.

---
← Previous: [Amazon ECR](17_amazon_ecr.md) | [Overview](00_overview.md) | Next: [AWS 201 Services — Overview](00_overview.md) →
