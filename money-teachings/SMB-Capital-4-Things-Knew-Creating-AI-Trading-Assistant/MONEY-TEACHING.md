# SMB Capital: 4 Things I Wish I Knew Before Creating My AI Trading Assistant (With Claude Code)

## Overview

This Money Teaching documents four critical mistakes to avoid when building an AI-powered trading assistant with Claude Code. It is based on real-world experience from a retail trader who built a production trading dashboard using Claude Code. The content focuses on moving beyond basic improvised coding without formal documentation or architecture planning to designing an inference architecture where the language model actively processes data at runtime, rather than only generating code.

## When to Follow These Money Teachings

- When you want to build a trading assistant, research synthesizer, or any AI tool that must reason over data
- When you are using Claude Code or similar AI coding tools for a project beyond a standalone script
- When you need the AI to understand your personal trading process, playbooks, and methodology
- When you want to avoid costly rework from mixing architecture design with code implementation in the same session, hallucination, or contradictory instructions

## Steps

### Step 1: Build an Inference Architecture, Not Just a Code Factory

Do not treat Claude Code as a tool that only writes code when prompted. Instead, integrate Claude's reasoning capabilities directly into the application so it runs during normal operation. Define an "inference architecture" where the app uses the language model to synthesize emails, surface themes, break down catalysts, and review performance against your own methodology. The same AI that helps build the app should also operate inside the app as a reasoning engine. Design the application so the language model actively processes data and makes decisions at runtime, rather than only generating code during development.

### Step 2: Use Separate Chat Sessions for Each Inference Layer

Never run the entire project inside a single Claude Code session. As a single chat session accumulates more messages and context, the model's performance can degrade: it can become less consistent and accurate, earlier instructions and assumptions contradict later ones, and the session produces inconsistent or contradictory outputs. Create separate chat threads, with one dedicated to each inference layer of your trading assistant. For example, have one chat for the morning report synthesis, one for the daily trade log, and one for the performance review layer. Keep the Claude Code session for implementation only, and do all architecture and reasoning design in the dedicated chat threads.

### Step 3: Create a Per-Layer Architecture Document and Close the Loop

Coding without architecture documentation often leaves scattered notes, comments, and decisions that contradict each other and create confusion in the codebase. For each inference layer, create a written architecture document that serves as the single source of truth. The document should cover: A) system purpose, B) how the system thinks, C) what the system produces, D) how it is rendered and run, and E) phase two roadmap. Update the architecture document first with every refinement. Then prompt Claude Code with the updated architecture attached and ask it to report what in the codebase does not align with the architecture. Adjust both until they mirror each other. This practice is called "closing the loop."

### Step 4: Teach Your Assistant Who You Are via a Settings Tab

An AI that knows nothing about your process is likely to produce output that does not match your trading methodology or includes irrelevant themes and catalysts. Build a settings tab inside your trading assistant that injects your personal trading process into the app's reasoning engine during runtime. Include: your trading playbooks, performance grading table and risk parameters, catalyst methodology, review process, account definitions, explicit theme definitions with precise criteria, and theme database. The more specific boundaries you provide, the more Claude can leverage inference and synthesize accurately. Without this context, the assistant may hallucinate themes, misfile catalysts, and ignore your methodology.

## Examples

### Example 1: Morning Report Synthesis

Instead of asking Claude to "make a morning report," define an inference architecture with four sections: environment, themes, catalysts, and watch list. For the environment section, instruct Claude to answer: "What kind of day is this?" by describing market conditions and broader trading context. For the catalyst section, instruct Claude to answer: "What names are most in play?" by starting from individual company-specific catalysts rather than market-wide trends. Provide your seven-step catalyst breakdown and theme definitions in the settings tab. The result is a report that surfaces only the catalysts and themes that match your actual trading methodology.

### Example 2: Trade Log and Performance Review

Build an inference layer for the daily trade log that asks specific questions about each trade and asks follow-up questions to clarify vague entries. Build a second performance layer that aggregates patterns across weeks and months. The daily log layer reviews individual trades. The performance layer analyzes patterns across weeks and months. Feed both layers your review process and performance grading table from the settings tab so the AI understands execution gaps, sizing errors, and process inconsistencies the same way you do.

## Best Practices

- ✅ Design the inference architecture before writing any implementation code
- ✅ Keep one chat thread per inference layer and never mix architecture design with code implementation
- ✅ Maintain a written architecture document as the single source of truth
- ✅ Close the loop by comparing the codebase against the architecture after every change
- ✅ Store your playbooks, risk parameters, catalyst methodology, and theme definitions in a settings tab
- ✅ Lead prompts with the definition of success, not a list of steps
- ✅ Verify output against source data by checking the citations at the bottom of every report

## Keep In Mind

- The longer a single Claude Code session runs, the more context can degrade and contradictions can accumulate
- Vibe coding is fine for contained UI tweaks but risky when building inference layers because it leads to contradictions and unreconciled instructions
- If you give the AI no boundaries, it may invent themes and catalysts that do not match your process
- The architecture document should be updated first, then Claude Code should implement the changes
- Claude Code automatically reads the claude.md file at the start of every session; keep it aligned with your architecture

## Security & Safety Notes

- Do not expose raw API keys or credentials inside the architecture document or settings tab
- Treat the architecture document as proprietary knowledge that encodes your unique trading process
- Audit every report's source citations before acting on AI-synthesized output
- Start with non-real-money testing until you have verified the assistant's accuracy across enough sessions to verify consistency

## Common Pitfalls

- **Problem:** Using Claude Code only to write functions and never wiring its reasoning into the app
  **Solution:** Build an inference architecture where the large language model (LLM) reasons over your data dynamically inside the application

- **Problem:** Running all architecture discussion inside one Claude Code session, causing context degradation
  **Solution:** Use separate chat threads for each inference layer and keep Claude Code for implementation only

- **Problem:** Vibe coding without documentation, leading to contradictions and unreconciled instructions
  **Solution:** Write a per-layer architecture document and close the loop after every change

- **Problem:** Giving the AI no context about your trading process, causing generic or hallucinated output
  **Solution:** Populate a settings tab with your playbooks, risk parameters, catalyst methodology, and theme definitions
