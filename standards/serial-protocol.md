---
title: Serial Communication Protocol
description: A basic serial protocol for communication between devices.
---

# Standards
Data is transmitted at a rate of one bit per tick. A serial packet consists of a single start bit followed immediately by the data. Packets may be sent right after another with no delay in between packets. Each packet has a data width of 8 bits.

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
