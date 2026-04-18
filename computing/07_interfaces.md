---
tags:
  - computing
  - networking
created_at: 2026-03-31T00:00:00
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_overview.md)

# Interfaces

## What It Is

An interface is how you interact with a system. It defines the method of access without requiring you to know the internal implementation.

## Analogy

A remote control: you use the TV through buttons without understanding the internal circuitry. You still need to know what each button does — that's the interface.

## How It Works

### Types of Interfaces

| Type | What it is | Example |
|------|-----------|---------|
| **API** | Rules for programs to talk to each other | REST API, AWS SDK |
| **CLI** | Text-based interaction | `aws s3 ls`, `kubectl get pods` |
| **GUI** | Visual interaction | AWS Console, web browsers |
| **Network Interface** | Connection point for network communication | ENI (Elastic Network Interface) |

### API

An API defines what operations are available and how to call them. You don't see the internal code — you call the API and handle the response.

API styles (see [HTTP](../networking/05_http.md) for REST details):

| Style | Format | Use case |
|-------|--------|----------|
| REST | JSON over HTTP | Most web APIs |
| GraphQL | JSON over HTTP | Frontend flexibility |
| gRPC | Protocol Buffers over HTTP/2 | Microservice-to-microservice |

### ENI (Elastic Network Interface)

A virtual network card in AWS. Each [EC2](../aws/05_amazon_ec2.md) instance has at least one ENI.

An ENI has: private IP, optional public IP, MAC address, [security groups](../aws/14_security_group.md), and source/destination check flag.

An instance can have multiple ENIs for separating management and data traffic or multi-homed setups across subnets.

### Programming Interface

In software, an interface is a contract: if you implement the interface, you must provide the required methods. The caller doesn't care which implementation is used.

## Example

You run `aws s3 ls` in the terminal. The CLI (interface) translates your command into an API call to the S3 [endpoint](08_endpoints.md) (`s3.us-east-1.amazonaws.com`). The same operation through the GUI: open the AWS Console and click through the S3 bucket list.

Another example: you SSH into a Linux server and run `vim config.yaml`. The terminal is still the interface to the machine, but the editor becomes a second interface you use to edit the file inside that terminal session. See [Vim and Neovim](../tooling/02_vim_and_neovim.md) for the editor-specific details.

## Why It Matters

Interface = how you interact. [Endpoint](08_endpoints.md) = where you reach the system. Understanding this distinction clarifies AWS documentation and terminal workflows: the terminal can host multiple interfaces at once, such as a shell for running commands and an editor for changing files.

---
← Previous: [Caching](06_caching.md) | [Overview](./00_overview.md) | Next: [Endpoints](08_endpoints.md) →
