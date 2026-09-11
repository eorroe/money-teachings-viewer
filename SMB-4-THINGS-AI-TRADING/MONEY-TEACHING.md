# SMB-4-THINGS-AI-TRADING

## Overview

A trader from SMB Capital shares four critical mistakes made while building an AI trading assistant with Claude Code. The lessons focus on treating Claude as an inference layer rather than just a code generator, organizing work across separate sessions, maintaining architecture documents, and teaching the AI your trading methodology. These teachings help traders build efficient, reliable AI-assisted trading systems.

## When to Follow These Money Teachings

- When building an AI trading assistant or any AI-powered trading tool
- When using Claude Code for trading automation and analysis
- When seeking to improve workflow efficiency and decision-making in trading

## Steps

### Step 1: Define Your Use Cases and Expected ROI

Before writing any code, identify the specific problems you want to solve and verify that building an AI assistant will actually move the needle. The speaker identified two core goals: automating a manual trade log review process and synthesizing daily emails, analyst reports, and market filters into a concise morning report. Ask yourself what would make the time investment worthwhile.

### Step 2: Treat Claude Code as an Inference Layer, Not Just a Code Factory

Most people use Claude Code only to write code. This is only one dimension of its value. Instead, wire Claude's reasoning into your product as a live feature. The speaker's trading operating system uses Claude API calls to read the market, break down research, and review performance live. Design an inference architecture where the app reasons over data rather than simply regurgitating it.

### Step 3: Use Separate Chat Threads for Each Inference Layer

Do not run the entire project inside one Claude Code session. The longer a session runs, the more context degrades and contradictions accumulate. Open separate chat threads, one per inference layer. For example, the speaker uses dedicated chats for the morning report synthesis, the daily trade log, and the performance review layer. Each chat has a single, focused task.

### Step 4: Build an Architecture Document per Layer as Your Single Source of Truth

Within each dedicated chat, work with Claude to draft an architecture document that captures everything about that layer. The speaker's morning report architecture has five sections: A) system purpose, B) how the system thinks, C) what the system produces, D) how it renders and runs, and E) phase two roadmap. This document is the single source of truth that prevents contradictions and lost progress.

### Step 5: Close the Loop Between Architecture and Code After Every Change

When you update the architecture document, send the updated version to Claude Code with a prompt asking it to implement the changes and report back what it changed. Then feed that report back to the chat side to verify alignment. The architecture and the code base should mirror each other by the end of each prompt cycle. This prevents artifacts from earlier vibed code from causing confusion later.

### Step 6: Teach Your Assistant Who You Are via a Settings Tab

Never assume the AI understands your trading process, risk tolerance, or methodology. Build a settings tab that holds your playbooks, grade table, catalyst methodology, theme ontology, review process, and any other context that shapes how you think about trades. Feed this into the app's reasoning live so that depending on the task, the AI references the relevant pieces. The more specific boundaries you provide, the more the AI can leverage its inference instead of hallucinating.

### Step 7: Lead with the Definition of Success, Not Step-by-Step Instructions

When prompting, start with the finished product you want rather than a list of steps. Define what success looks like. The optimal prompting strategy has evolved toward leading with the outcome, which is also easier for humans to articulate.

## Examples

### Example 1: Morning Report Synthesis

The speaker receives hundreds of emails, analyst reports, earnings analysis, and market filters daily. Rather than manually scanning everything, he built a morning report layer that reads all emails and synthesizes them into sections: environment, themes, catalysts, insights, and watch list. Each section has a distinct question, lens, selection criteria, and synthesis. For instance, the catalyst section asks "what names are most in play?" and uses a bottom-up lens focused on individual company catalysts rather than just the most emailed mega cap name. This prevents the AI from overweighting Nvidia just because every email mentions it.

### Example 2: Automated Trade Log Review

The speaker had an existing Google Sheets trade log that surfaced process gaps such as incorrect grading, failure to size based on grade, or losing money on good ideas. The problem was it was entirely manual and took too long. He used Claude to recreate the trade log as an interactive tool that asks him questions after each trade, pushes him to be more specific, and surfaces tendencies and patterns. The daily log inference layer acts like a manager, while the performance layer acts like a CEO, generating weekly and monthly reviews of trading patterns.

## Best Practices

- ✅ Start by defining success and ROI before touching any code
- ✅ Use separate Claude Chat sessions to design each inference layer before coding
- ✅ Maintain a per-layer architecture document as your single source of truth
- ✅ Build a settings tab that stores your playbooks, theme definitions, and risk parameters
- ✅ Close the loop by asking Claude Code to report back changes after every implementation
- ✅ Give the AI specific boundaries and definitions to reduce hallucination
- ✅ Lead prompts with the desired outcome rather than step-by-step instructions

## Keep In Mind

- The better your data quality and boundaries, the better the AI output
- You must own your intellectual property; maintain the architecture documents yourself
- Claude Code's context degrades over long sessions; start fresh for new layers
- The AI cannot read your mind; you must explicitly teach it your process and definitions
- Simple UI tweaks can stay in Claude Code, but structural changes must go through the architecture first
- The goal is efficiency and accuracy, not just building more features

## Security & Safety Notes

- Always verify AI-generated trade recommendations against your own analysis
- Include source citations in every section of reports so you can trace data back to origin
- Start with small, contained tasks before trusting the AI with complex decisions
- Treat the AI as an assistant, not a replacement for trading judgment
- Audit the structure of outputs, not just the data; errors often appear in section placement

## Common Pitfalls

- **Problem:** Using Claude Code only as a code factory and never leveraging its inference capabilities
  **Solution:** Design an inference architecture that wires Claude's reasoning directly into your app as a live feature, not just a backend code generator.
- **Problem:** Running the entire project in one Claude Code session, leading to context degradation and contradictions
  **Solution:** Use separate chat threads dedicated to each inference layer (morning report, daily log, performance).
- **Problem:** Vibe coding without architecture documents, causing contradictions, artifacts, and lost progress
  **Solution:** Maintain a per-layer architecture document as the single source of truth and update it before sending changes to Claude Code.
- **Problem:** Expecting the AI to understand your trading process without explicitly teaching it
  **Solution:** Build a settings tab containing your playbooks, theme definitions, risk tolerance, catalyst methodology, and review process so the AI references the right context for each task.
