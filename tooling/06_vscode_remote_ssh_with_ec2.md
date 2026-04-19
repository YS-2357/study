---
tags:
  - tooling
  - aws
  - computing
created_at: 2026-04-13T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_tooling_overview.md)

# VS Code Remote SSH with EC2

## What It Is

Using **VS Code Remote - SSH** with **Amazon EC2 (Elastic Compute Cloud)** means VS Code connects to an EC2 instance over SSH, installs **VS Code Server** there, and runs commands plus most workspace extensions on the remote machine instead of your laptop, as described in the [VS Code Remote - SSH documentation](https://code.visualstudio.com/docs/remote/ssh). The main overhead is that your editor becomes a remote session: file operations, terminals, language servers, debugging, and extension work now depend on network quality, remote machine sizing, and EC2 operations.

## Analogy

It is like driving a car with a remote steering link. You still hold the wheel locally, but the engine, transmission, and road contact are somewhere else, so latency, fuel cost, and maintenance all matter more than they do in a local setup.

## How It Works

### The biggest overhead categories

| Overhead | Why it exists | What you feel |
|---------|---------------|---------------|
| **Network latency** | VS Code keeps the UI local, but the remote server, terminal, debugger, and most extensions run on the EC2 host over SSH according to the [VS Code docs](https://code.visualstudio.com/docs/remote/ssh). | Slower file search, IntelliSense, terminal response, debug attach, and save/build loops when the network is slow or far away |
| **Remote compute cost** | EC2 On-Demand instances are billed while `running`, with per-second billing and a 60-second minimum, per the [Amazon EC2 On-Demand pricing docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html). | You pay for the remote machine even if you are mainly "just editing" |
| **Remote storage cost** | If you stop an EBS-backed instance, compute charges stop, but attached EBS storage still costs money, as documented in [How EC2 instance stop and start works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-stop-start-works.html). | Cheap to pause compute, but not free to keep the environment around |
| **Bootstrap and extension overhead** | Remote - SSH requires a working SSH client locally, an SSH server remotely, and installs VS Code Server on the host; most extensions are installed on the SSH host, per the [VS Code docs](https://code.visualstudio.com/docs/remote/ssh). | First-time setup, extra installs, occasional extension mismatch, remote dependency setup |
| **Security and ops overhead** | SSH access requires you to manage keys, SSH reachability, and security-group rules; AWS documents security groups as the instance firewall in the [EC2 security group docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html). | More setup work than local editing and more chance of access mistakes |

### What is usually the main overhead in practice

For most people, the **main practical overhead is latency**. VS Code is usable because the UI stays local, but the actual development work executes on the remote host. That means every "developer feedback loop" depends on SSH round-trips and remote machine responsiveness, not just on your laptop.

If the EC2 instance is in the same region as your database or internal services, that tradeoff can still be worth it because your app-to-app traffic may become much faster than running locally. But from a pure editor experience standpoint, network delay is the first thing you notice.

### What costs more than people expect

The second big overhead is usually **keeping the environment alive**:

1. The EC2 instance costs money while running, per the [On-Demand pricing model](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html).
2. If you stop it, compute charges stop, but EBS storage persists and is still billed, per the [EC2 stop/start behavior docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-stop-start-works.html).
3. Starting again is not instant operationally because you may need to wait for boot, package services, SSH readiness, and your dev stack to come back.

### What operational overhead comes with SSH

VS Code Remote - SSH needs an SSH client on your machine and a running SSH server on the remote host, as listed in the [VS Code requirements](https://code.visualstudio.com/docs/remote/ssh). On AWS, that usually means:

1. Launch EC2.
2. Allow SSH access with a security group rule, which AWS documents in its [security group guidance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-security-group.html).
3. Restrict port 22 to your IP rather than opening it broadly; AWS explicitly warns to authorize only the addresses that need access in the [security-group update docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/changing-security-group.html), and AWS Security Hub flags unrestricted SSH ingress in [EC2.13](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-13).
4. Manage SSH keys, usernames, host changes, and remote packages.

### A useful conclusion

If your question is "what is the one main overhead?", the answer is:

- **Main technical overhead:** network latency in the edit-build-debug loop
- **Main money overhead:** paying for a running EC2 environment and persistent EBS storage
- **Main admin overhead:** securing and maintaining SSH access

## Example

Suppose you use VS Code Remote - SSH to connect from Seoul to a `t3.small` EC2 instance in another region.

- Typing stays local, so the editor window itself feels normal.
- Running `npm install`, `pytest`, `git grep`, or a language server happens on the EC2 host through VS Code Server, per the [VS Code Remote - SSH model](https://code.visualstudio.com/docs/remote/ssh).
- If the network is slow, autocomplete and terminal output feel delayed.
- If you leave the instance running all day, you keep paying EC2 compute charges under the [On-Demand model](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html).
- If you stop the instance at night, compute charges stop but your EBS volume still costs money, per the [EC2 stop/start docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-stop-start-works.html).

In that setup, the editor is not the expensive part. The overhead comes from distance, remote machine runtime, and SSH operations.

## Why It Matters

If you organize the tradeoff clearly, you can decide whether VS Code over SSH is the right tool:

- Use it when you need the code to live near AWS resources, large datasets, or internal VPC-only systems.
- Avoid it when you mainly want a fast local editing loop and do not need remote proximity.
- If SSH exposure is the main concern, consider **AWS Systems Manager Session Manager**, which AWS says can provide secure access "without the need to open inbound ports, maintain bastion hosts, or manage SSH keys" in the [Session Manager docs](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html).

> **Tip:** If you use EC2 only as a remote dev box, put the instance in the closest practical region to you, stop it when idle, keep the security group tight, and treat latency as the first thing to optimize.

---
↑ [Overview](./00_tooling_overview.md)

**Related:** [Obsidian + GitHub as a Second Brain](05_obsidian_github_second_brain.md)
**Tags:** #tooling #aws #computing
