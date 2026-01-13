# Scripts

This folder contains Python scripts designed for use on NumWorks calculators.

## Contents

Each script in this folder is a standalone educational tool targeting a specific topic within AP Calculus AB. Scripts are designed to be uploaded individually to a NumWorks calculator and run independently.

## NumWorks Python Constraints

The NumWorks calculator runs a limited MicroPython environment with the following constraints:

- **No external libraries**: Only built-in Python functionality and NumWorks-provided modules (`math`, `kandinsky`, `ion`, etc.) are available.
- **Limited memory**: Scripts must be memory-efficient. Large data structures and recursive algorithms may cause issues.
- **No file I/O**: Scripts cannot read from or write to files.
- **Screen limitations**: The display is 320x240 pixels. Visual output must be designed accordingly.
- **No floating-point precision guarantees**: Standard floating-point limitations apply.

## Educational Design

Each script is designed with education as the primary goal:

- Scripts explain what they are computing and why.
- Intermediate steps and reasoning are shown where pedagogically valuable.
- Output is structured to reinforce conceptual understanding.

Scripts in this folder are not black-box calculators. They are learning tools.
