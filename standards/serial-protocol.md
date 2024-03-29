---
title: Serial Communication Protocol
description: A basic serial protocol for transmitting data between two devices.
---

# Standards
## Overview
A serial standard used for transmitting data over a single wire. The standard does not specify a bit width.

## Design
Data is sent at a rate of one bit per tick. A serial packet consists of a single start bit followed immediately by the data. Packets may be sent right after another with no delay in between packets.

### Packet example
```
+-+--------+
|1|00101101|
+-+--------+
 ^ ^^^^^^^^
 | \-------Data
 Start bit

+-+--------+-+--------+-- - -
|1|00101101|1|01001100|. . .
+-+--------+-+--------+-- - -
 ^ ^^^^^^^^ ^ ^^^^^^^^
 | |        | \-------Data
 | |        Start bit
 | |
 | \-------Data
 Start bit
```
