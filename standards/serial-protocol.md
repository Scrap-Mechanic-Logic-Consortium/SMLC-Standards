---
title: Serial Transmission Protocol
description: A basic serial protocol for communication between devices.
---

# Standard
This is a standard for data transmission over a single wire.

## Protocol
Data is transmitted at a rate of one bit per tick. A serial packet consists of a single start bit followed immediately by the data. The least significant bit of the data is sent first. Packets may be sent right after another with no delay in between packets. Each packet has a data width of 8 bits.

## Physical interface
The serial interface is a singular gate.

## Packet example
Bit flow is from left to right (left being the first bit transmitted).
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
