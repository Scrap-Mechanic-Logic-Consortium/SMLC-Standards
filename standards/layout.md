---
title: Layout
description: Standardizes logic component form-factor and IO gate markings
---

# Layout
This is the main logic component layout standard for the SMLC. If you make a component (re-usable logic creation like an adder or some RAM) and want to use a standard way of communicating how to use it, this standard is for you. This standard is general and applicable to all logic components, and other more specific standards can be built on top of it.

## New global terminology
These are new terms that are used in this standard that should be made global, which will happen in a separate proposal in the terminology repo.
- A **component** is a Scrap Mechanic creation intended to be re-used inside of other logic creations.

## Terminology
- An **interface** is a set of logic gates that form an input or output of a creation (and components, which are creations)
- An **internal** gate is the opposite of an interface gate, so these are gates that are NOT supposed to be connected to external circuitry.
- A **flatpack** formfactor means that the component is one block tall, and thus entirely flat.

## General shape
(This section assumes that you don't rotate the component after having loaded it on the lift, so down stays down)
All interface gates of your creation should be on the sides of your creation. No vertical column of blocks will have both interface gates and internal gates that should not get external connections. From a side view, this might look like this:
```
# = interface gate
G = internal gate

  GG G
#GGG GG 
#GGGGGG#
```

## Interface markings
To make interfaces clearly visible, and ideally, make their function easy to read with just a glance at a component's documentation, here are some standards for marking interface gates:
- Paint your input gates in one of the left 4 hues of the paint tool, excluding the gray tones. The 4 hues on the right (excluding orange) should be for outputs.
  - input = yellow, lime, green, cyan or blue
  - output = violet, magenta, red or orange
  - the 8 grayscale and orange colors should NOT be used for interface gates.
- If an interface is a binary number, the logic gates should be oriented such that the logic symbols point towards the Most significant bit.
Anything that is NOT an interface gate can be painted and oriented however you want, as long as it still complies with what is described in the general shape section.

### Example color schemes:
A memory bank:
- yellow = address in
- green = data in
- lime = write
- blue = read enable
- violet = data output
- black = internal gates

A counter:
- green = increment
- blue = decrement
- violet = binary output
- internal gates are a messy mix of all the other colors not used as interface colors. (Allowed, not reccomended)
You can paint the internal gates if you want to use the colors to describe how the component works internally.
