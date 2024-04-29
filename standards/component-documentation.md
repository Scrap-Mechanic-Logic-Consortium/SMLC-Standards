---
title: Component Documentation
description: This standard defines how components should be documented in their blueprint description.
---

# Component Documentation

## Overview

This standard defines how components should be documented in their blueprint description. The goal is to provide a consistent and informative format that works for all components. By following this standard, it will be easier for users to understand how to use a component, because the formatting and terminology is consistent with other components.

## Terminology

- :bearing: **Component**: A logic creation intended to be used inside of other larger logic creaitons. Examples include ALUs, registers, and memory units.
- :bearing: **Interface**: A set of logic gates that function as input and/or output gates.
- :bearing: **Flag**: An interface with a single gate, which sends or recieves a continuous on or off signal.
- :bearing: **Trigger**: An interface with a single gate, which sends or recieves a pulsed signal.
- :bearing: **Bus**: An interface with multiple gates, which sends or recieves for example a binary number or another form of a multi-bit signal.
- :bearing: **Trigger bus**: Same as a normal bus, but is also a trigger, where if any of the bits is on, the trigger is considered to be active. It is not possible to send a 0 through a trigger bus, as it would not activate the trigger. This is NOT a bus with a seperate trigger interface. That's just a normal bus and a trigger.

## Blueprint Description
### Short non-technical description
The blueprint description should start with a short non-technical description of the component. This should be no longer than a paragraph. This description should explain what the component does, and why it is useful. Avoid immedietly diving into technical details, because thats for a later section.

### Interface decleration
Next, we describe what inputs and outputs the component has. This should be done using the following format:
`<interface gate color> <interface type (flag, bus, etc)> <input/output> : <short but descriptive name>`
(see examples below)

### Detailed description
After the interface decleration, we should provide a more detailed description of the component. This should include how the component works, and how it should be used. This section should be written in a more technical style, and should be more detailed than the short non-technical description. Here you can use the names of the interfaces you declared earlier.

Examples of stuff to discuss are:
- How to use the component
- What conventions you used for LSB marking, signed binary number formats, etc
- With what delay your component responds to inputs
- What the limist of the component are, and what happens if you exceed them
- Things that might cause undefined or buggy behavior
- Wether or not it is okay to "merge delete" the input and output interfaces to reduce the delay of the component

### Contact information, licence and credits
Finally, the blueprint description should include contact information for the creator of the component. (probably you) Preferrebly, this should include a Discord username, but something like an email or a statement that you want messages via steam is also fine.
Here you can also give other people permission to use your component, and if and how you want to be credited for it.
Of course if you used someone elses creation or idea in your component, you should credit them here, even if you got permission from them.

## Example
```
This is a 4-bit adder. It takes two 4-bit numbers as input, and outputs the sum of those numbers. This is useful for adding two numbers together in a computer.

blue bus input : A
red bus input : B
cyan flag input : Carry in
green bus output : Sum
yellow flag output : Carry out

Add two 4-bit two's complement numbers together. The carry in is added to the least significant bit of the first number. The sum is output as a 4-bit two's complement number, and the carry out is the carry out of the most significant bit, acting like a 5th output bit. The carry in is optional, and can be left unconnected if not needed.

This is a carry lookahead adder, and it has a delay of 6 ticks. It is balanced, so streaming in numbers at a high rate should not cause any issues. The input gates are just plain and-gates with no other inputs, do merge deleting them is fine. The output gates are XOR gates with no looped back outputs, so they can be merge deleted as well, as long as they are merger with other XOR gates.

This was made by CodeMaker_4, you can contact me via Discord on @codemaker_4. You can use this component in your creations, but please credit me if you do by mentioning my name and the name of this component in the description of your creation. This is my own work, based on the relevant wikipedia article.
```