---
title: Buffered Intercomponent Communication
description: This standard defines how components should communicate with each other using a buffer.
---

# Intercomponent Communication

## Overview

This standard outlines the principles and mechanisms for buffered communication between components. There are two components defined:
- The sending port
    - 16 bit output
    - 1 bit PP (Pushing Packet)
    - 1 bit RST (Reset)
- The receiving port
    - 16 bit input
    - 1 bit RTR (Ready to Receive)
    - 1 bit RST (Reset)

## Buffers

Buffers provide a temporary storage area for data in transit between components. Implementations include:
- Circular buffers: Allow for multiple requests/packets, optimizing storage efficiency.
- Single-packet buffers: Ideal for simpler communication scenarios.
- Devices processing data are assumed to be a buffer in and of themselves.

## Handshaking

- RTR (Ready to Receive): Indicates the receiving port can accept a new data packet.
- PP (Pushing Packet): Confirms the sending port is actively transmitting a data packet. Valid data is present on the output line during this phase.

- RTR = 1: The sending port may transmit a data packet. This signal, along with PP, may be brief (a single tick).
- RTR = 0: The receiver must ignore data and PP; the receiver is not prepared.
- Receiver's Responsibility: Processing should only begin when RTR is set to 1.
- Mid-transmission Readiness: If the receiver becomes ready during a transmission, it should momentarily pulse RTR to 1 and begin processing immediately.

## Buffer Management
- Buffered Receivers: Maintain RTR at 1 while the buffer has ample space (10+ free packets). If space drops below 10 packets, pulse RTR x times per 10 ticks (x = number of free packets) to alert the sender.
- Non-Buffered Receivers: Pulse RTR once every 10 ticks to simulate a single-packet buffer.

### Unsafe Communication
If the sender does not awknowledge the receiver's readiness (aka performs an unsafe push), the state of the communication may be damaged. In this case, the sender can send a reset signal through the RST line to reset the communication. Upon resetting, the receiver should clear its buffer and reset its state. Further actions can be taken by the receiver or higher level protocols which is up to implementation.

**Notes:**
- The 10-tick interval accounts for potential transmission and processing delays.
- The 16-bit data packet width was chosen for compatibility with the most common data width of modern logic computers.