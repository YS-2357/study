# Header and Payload

## Why This Matters

When studying networking, you will often hear the words `header` and `payload`.

They are very important because network data is usually not sent as one raw block.

Each layer adds its own information around the data it receives.

## Basic Meaning

- `header`: control information added by a layer
- `payload`: the actual content being carried by that layer

A simple way to think about it:

- header = instructions and metadata
- payload = the thing you want to deliver

## Why Layers Add Headers

Each layer has its own job.

To do that job, it needs to attach some information.

For example:
- Layer 4 needs ports and transport control information
- Layer 3 needs source and destination IP addresses
- Layer 2 needs local network addressing information

That added information is usually placed in the header.

## Layer 4 Example

At Layer 4, the protocol might be Transmission Control Protocol (TCP).

The Layer 4 header can include things such as:
- source port
- destination port
- sequence number
- acknowledgment information
- control flags

The Layer 4 payload is the data coming from higher layers, such as:
- Hypertext Transfer Protocol (HTTP) request data
- Domain Name System (DNS) message data
- application data in general

So:
- Layer 4 header = transport control information
- Layer 4 payload = application-side data being carried

## Layer-by-Layer Wrapping

One of the most important ideas in networking is that each lower layer wraps the data from the upper layer.

That means:
- the upper layer's whole data unit becomes the payload of the lower layer
- the lower layer adds its own header

This happens step by step.

### Example: opening a web page

1. Layer 7 creates an HTTP request
2. Layer 4 adds a TCP header
3. Layer 3 adds an Internet Protocol (IP) header
4. Layer 2 adds a frame header
5. Layer 1 sends the bits physically

So you can picture it like this:

```text
Layer 4 = [TCP header][HTTP data]
Layer 3 = [IP header][TCP header][HTTP data]
Layer 2 = [Frame header][IP header][TCP header][HTTP data]
```

## Header and Payload Are Not Only Layer 4

These terms are strongly related to Layer 4, but they are not limited to Layer 4.

They are used at multiple layers, especially:
- Layer 2
- Layer 3
- Layer 4

That is why header and payload are better understood as part of encapsulation, not as a concept belonging to only one layer.

## Easy Intuition

Think of sending a package inside another package.

- the inside content is the payload
- the label and delivery instructions are the header

Then another delivery stage may put that whole package inside a bigger one with a new label.

That is similar to how networking layers wrap data.

## What to Remember

- header = metadata and delivery/control information
- payload = the content being carried
- each lower layer wraps the upper layer's data
- Layer 4 uses headers heavily, but header/payload is a multi-layer idea
