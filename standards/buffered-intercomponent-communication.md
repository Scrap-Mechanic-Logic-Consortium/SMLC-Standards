---
title: Buffered Paralell Transmission Protocol
description: This standard defines how components should communicate with each other using a buffer.
---

# Buffered Paralell Transmission Protocol

## Overview

This standard outlines the principles and mechanisms for buffered data transmission from one component to another. There are two components defined:
- The data producer
    - 32 bit output
    - 1 bit PP (Pushing Packet)
    - 1 bit RST (Reset)
    - When it has data, it will send data to the consumer, unless the consumer is not ready to receive data.
- The data consumer
    - 32 bit input
    - 1 bit RTR (Ready to Receive)
    - 1 bit RST (Reset)
    - When it is ready to receive data, it will accept data from the producer and either store it in a buffer or process it immediately.

## Example use case:

A CPU producing data and sending it to a GPU for processing.
Sometimes, the CPU wants to send a burst of data to the GPU. But the GPU can't process the data that fast.
To prevent the CPU from being slown down, a buffer can be placed in between the CPU and the GPU.
This Buffered Paralell Transmission Protocol is then used for both the transfer from the CPU to the buffer, as from the buffer to the GPU.

## Buffers

Buffers provide a temporary storage area for data in transit between components. Implementations include:
- Circular buffers: Allow for multiple requests/packets, optimizing storage efficiency.
- Single-packet buffers: Ideal for simpler communication scenarios.
- Devices producing and consuming data are assumed to be a buffer in and of themselves.

## Handshaking

- RTR (Ready to Receive): Indicates the receiving port can accept a new data packet.
- PP (Pushing Packet): For each tick that this signal is turned on, it means that one packet is being pushed to the receiver. Sending multiple packets right after each other with no tick of pause in between is allowed and is called "streaming" data.

- RTR = 1: The sending port may transmit a data packet.
- RTR = 0: The receiver may ignore data and PP; the receiver is not prepared.
- RTR pulsing with duty cycle of n/10 ticks: The receiver is ready to receive at most n packets.

## Buffer Management
- Buffered Receivers: Maintain RTR at 1 while the buffer has ample space (10+ free packets). If space drops below 10 packets, send a PWM signal of n/10 ticks, where n is the number of free packets.
- Non-Buffered Receivers: Pulse RTR once every 10 ticks to simulate a single-packet buffer.

## Guarantees
- If the receiver is not ready to receive data, the sender must not push data, except when doing unsafe communication (see below).
- The order of the packets is meaningful and must be maintained. For example, a buffer should not reorder packets.
- If a packet is put into a buffer, it must come out of the buffer eventually, even if no packets come after it.

### Unsafe Communication
If the sender does not awknowledge the receiver's readiness (aka performs an unsafe push), the state of the communication may be damaged. In this case, the sender can send a reset signal through the RST line to reset the communication. Upon resetting, the receiver should clear its buffer and reset its state. Further actions can be taken by the receiver or higher level protocols which is up to implementation.

**Notes:**
- The 10-tick interval accounts for potential transmission and processing delays.
- The 32-bit data packet width was chosen for compatibility with a wide range of computers, devices, and usecases.
