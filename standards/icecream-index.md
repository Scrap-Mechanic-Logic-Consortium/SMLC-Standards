---
title: Icecream Index
description: A way to categorize logic creations based on the quantity and type of mods used.
---

# Icecream Index

The Icecream Index is a way to categorize logic creations based on the types of logic mods used.

- **Vanilla** = No mods are used.
    - **Spawnable vanilla** = BP editing, self wires, glitch welds, and non-vanilla colors are allowed. Creations that are too big to spawn on the lift in vanilla, do not qualify for this category.
        - **Strict/Glitchless Vanilla** = Absolutely no mods, BP edits, glitches, self-wires, or non-vanilla colors are allowed in this category.
- **Modded** = Requires *any* mods to spawn/use
    - **Light modded** = Uses only mods that exclusively implement boolean logic alternatives (limited to the boolean operators AND, OR, XOR, NAND, NOR, XNOR, IMPLY, NIMPLY, NOT). Mods that internally optimize the logic are allowed. ie. it does not matter what the mod does internally as long as the outcome of the circuit is the same.
        - **Theoretical vanilla** = Uses mods that implement boolean logic gates to reduce gate count or lag without a per tick performance gain. One-block boolean memory blocks are allowed as an exception as long as they could be replaced by vanilla logic with the same behavior.
        - **Accelerated vanilla** = Identical to theoretical, but a logic speedup mod is required for it to work at all because it needs to keep up with SM physics, and/or it needs to be faster than the rest of the vanilla logic system. (think self-driving cars, rolling-window screens, ect…)
    - **Auxiliary modded** = Uses mods for physics-based improvements, decoration, etc.. (ex. modded pistons)
    - **Alternative logic modded** = Uses mods that implement mathematical function blocks / computers.
        - **Mathematical** = Uses modded gates and blocks that are not intrinsically turing-complete (ie. modpack-esque blocks).
        - **Block Computer** = Uses modded parts that are intrinsically turing-complete (ie. can run any program that a computer can run in a block).
