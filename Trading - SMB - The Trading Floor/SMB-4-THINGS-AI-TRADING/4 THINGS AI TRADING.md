# SMB 4 THINGS AI TRADING

## Overview

Garrett from SMB Capital shares four critical mistakes made while building an AI trading assistant with Claude Code. The lessons focus on treating Claude Code as an inference layer rather than just a code generator, organizing work across separate sessions, maintaining architecture documents, and teaching Claude Code your trading methodology. These teachings help retail traders build AI-assisted trading systems that reduce time spent on manual trade log review and produce reports with consistent structure.

## When to Follow These Money Teachings

- When building an AI trading assistant or any AI-powered trading tool
- When using Claude Code for trading automation and analysis
- When seeking to streamline trading analysis workflows and reduce manual review steps in trading

## Steps

### Step 1: Define Your Use Cases and Expected ROI (Return on Investment)

Before writing any code, identify the specific problems you want to solve and verify that the time investment will produce a measurable improvement in your trading workflow outcomes. Garrett identified two core goals: automating a manual trade log review process and synthesizing hundreds of daily emails, analyst reports, and market filters into a morning report. Ask yourself what would make the time investment worthwhile.

### Step 2: Treat Claude Code as an Inference Layer, Not Just a Code Factory

Users can treat Claude Code only as a code generator. This is only one way to use it. Instead, wire Claude Code's synthesis capabilities into the trading assistant as an inference feature integrated into the app via Claude API calls. Garrett's trading assistant processes research and reviews trading performance through Claude API calls. Design an inference architecture where the app reasons over data rather than simply regurgitating it.

### Step 3: Use Separate Chat Threads for Each Inference Layer

Do not run the entire project inside one Claude Code session. In Garrett's experience, the longer a session runs, the more accumulated context the model must process through, which can reduce output quality as context accumulates. Open separate chat threads, one per inference layer. Garrett uses dedicated chats for each inference layer: the morning report synthesis, the daily trade log, and the performance review layer. Each chat has a single, focused task.

### Step 4: Build an Architecture Document per Layer as Your Single Source of Truth

Within each dedicated chat, work with Claude Code to draft an architecture document that captures all design decisions for that layer. Garrett's morning report architecture has five sections: A) system purpose, B) the system's inference framework, C) what the system produces, D) how it renders and runs, and E) phase two roadmap. This document captures all design decisions for that layer so that design decisions and implementation stay aligned, preventing contradictions and lost work.

### Step 5: Close the Loop Between Architecture and Code After Every Change

When you update the architecture document, send the updated version to Claude Code with a prompt asking it to implement the changes and report back what it changed. Then feed Claude Code's change report back to the dedicated chat thread to verify alignment. The architecture and the code base should be fully aligned after Claude Code implements each change. This prevents leftover inconsistencies and unresolved fragments from earlier prototyping work from creating confusion later.

### Step 6: Teach Your Assistant Who You Are via a Settings Tab

Do not assume Claude Code understands your trading process, risk tolerance, or methodology. Build a settings tab that holds your playbooks, grade table, catalyst methodology, theme ontology, and review process. Feed this into the assistant's analysis as part of the app so that depending on the task, Claude Code references the relevant settings. Providing specific boundaries enables Claude Code to leverage its inference and synthesis capabilities.

### Step 7: Lead with the Definition of Success, Not Step-by-Step Instructions

When prompting, start with the finished product you want rather than a list of steps. Define what success looks like. Based on his own experience, Garrett found that starting with the definition of success produces results that better match the intended output than leading with step-by-step instructions.

## Examples

### Example 1: Morning Report Synthesis

Garrett receives hundreds of emails daily, along with analyst reports, earnings analysis, and market filters. Rather than manually scanning everything, he built a morning report that reads all emails and synthesizes them into sections: environment, themes, catalysts, insights, and watch list. Each section has a distinct question, lens, selection criteria, and synthesis. For instance, the catalyst section asks "what names are most in play?" and uses a bottom-up lens focused on individual company catalysts rather than just the most emailed mega cap name. This prevents Claude Code from overweighting Nvidia just because 80 to 88 percent of emails mention it.

### Example 2: Automated Trade Log Review

Garrett had an existing Google Sheets trade log that surfaced process gaps such as incorrect grading, failure to size based on grade, or losing money on good ideas. The problem was it was entirely manual and time-consuming. He used Claude Code to recreate the trade log as an interactive tool that asks him questions after each trade, pushes him to be more specific, and surfaces tendencies and patterns. The daily log inference layer asks him questions after each trade, pushes him to be more specific, and surfaces tendencies and patterns, while the performance layer generates reviews of trading patterns across weekly and monthly intervals.

## Best Practices

- ✅ Start by defining success and ROI before touching any code
- ✅ Use separate Claude Chat sessions to design each inference layer before coding
- ✅ Maintain a per-layer architecture document as your single source of truth
- ✅ Build a settings tab that stores your playbooks, theme definitions, and risk parameters
- ✅ Close the loop by asking Claude Code to report back changes after every implementation
- ✅ Give Claude Code specific boundaries and definitions to reduce hallucination
- ✅ Lead prompts with the desired outcome rather than step-by-step instructions

## Keep In Mind

- More specific data and more specific boundaries improve the assistant's output accuracy.
- You must own your intellectual property; maintain the architecture documents yourself
- Claude Code's context degrades as sessions accumulate more context; start new chat threads for new inference layers
- Claude Code cannot infer unstated intent; you must explicitly teach it your process and definitions
- Cosmetic UI changes such as font size or color adjustments can be made directly in Claude Code, but any change to the report's structure, section layout, or data logic must first be reflected in the architecture document
- The objective is efficiency and accuracy, not just building more features

## Security & Safety Notes

- Always verify Claude Code-generated trade recommendations against your own analysis
- Include source references in each section of every report so you can identify which input produced each claim
- Start with contained tasks before expanding to broader analysis
- Treat Claude Code as an assistant, not a replacement for trading judgment
- Audit the structure of outputs as well as the data; Claude Code may place content in the wrong section

## Common Pitfalls

- **Problem:** Using Claude Code only as a code factory and never leveraging its inference capabilities
  **Solution:** Design an inference architecture that integrates Claude Code's synthesis capabilities into the trading assistant via Claude API calls, not just as a tool for writing code.
- **Problem:** Running the entire project in one Claude Code session, which in Garrett's experience leads to accumulated context that can reduce output quality and produce contradictions
  **Solution:** Use separate chat threads dedicated to each inference layer (morning report, daily log, performance).
- **Problem:** Building without architecture documents, causing contradictions, leftover inconsistent fragments in the codebase, and lost progress
  **Solution:** Maintain a per-layer architecture document as the authoritative reference for all design decisions and update it before sending changes to Claude Code.
- **Problem:** Expecting Claude Code to understand your trading process without explicitly teaching it
  **Solution:** Build a settings tab containing your playbooks, theme ontology, risk tolerance, catalyst methodology, and review process so Claude Code consults the applicable settings for each task type.
