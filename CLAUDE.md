# Claude Code Instructions

This file provides directives for Claude Code sessions working on this repository.

## Project Purpose

APCalc-NumWorks-Toolkit is an educational toolkit for AP Calculus AB students using NumWorks calculators. The purpose is to support genuine learning—not to enable cheating or shortcut-taking. Every script must reinforce conceptual understanding.

## Scope Constraints (v1)

- This version covers **AP Calculus AB only**.
- Do not introduce BC topics (series, polar, parametric beyond motion, advanced integration techniques) until explicitly authorized for a future version.
- Stay within the boundaries of the College Board AP Calculus AB curriculum.

## Script Requirements

Every script must:

1. **Explain calculus reasoning in its output.** Raw numerical answers are insufficient. Scripts must display steps, intermediate values, and conceptual explanations where appropriate.

2. **Be educational, not transactional.** The goal is to teach, not to compute silently.

## Prohibited Behaviors

- **NEVER add symbolic CAS (Computer Algebra System) behavior.** This toolkit operates numerically and pedagogically, not symbolically.
- Do not implement features that would be disallowed on AP exams.
- Do not add hidden functionality or undocumented capabilities.

## Technical Constraints

- **Prioritize NumWorks Python constraints.** The NumWorks calculator runs MicroPython with limited memory and no external libraries. All code must be compatible.
- **Prioritize efficiency within educational goals.** Efficiency means clarity and reliability, not clever shortcuts that obscure understanding.

## Architecture Decisions

Architecture and design decisions for this project are made by the human maintainer in collaboration with ChatGPT. Claude Code's role is implementation and refinement within established guidelines, not architectural redesign.

## Reference Documents

Always consult:

- `README.md` for project overview
- `CONTRIBUTING.md` for contribution standards
- `docs/design_philosophy.md` for pedagogical principles
- `docs/exam_policy.md` for ethical guidelines

Follow the Project Goals & Rules as defined in this repository. When in doubt, ask for clarification rather than making assumptions.
