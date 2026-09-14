# SMB AI Trading Assistant

## Overview

This Money Teaching walks you through building a personal AI trading assistant using Claude Code, demonstrated by SMB Capital traders Tim and Garrett. It teaches a repeatable four-step workflow that traders who do not know HyperText Markup Language (HTML) and who have not used coding or agentic AI tools can follow to create a customized HTML trading dashboard. The dashboard tracks trades, identifies recurring mistakes, displays performance patterns, and automates daily journaling routines.

## When to Follow These Money Teachings

- When you want to build a personal trading dashboard without coding experience
- When you use TraderView or similar tools that track trade performance statistics, tag trades, and provide profit and loss (P&L) breakdowns and win-loss ratios, but want stats and tabs for the specific setups and patterns you track that those tools do not cover
- When you want to automate your end-of-day trade review and journaling routine
- When you want Claude to analyze your trade write-ups and flag recurring mistakes or tendencies
- When you are a retail trader looking for a structured, repeatable workflow to adopt AI tools

## Steps

### Step 1: Plan Mode — Brainstorm Your Dashboard Design

Open Claude Code and switch to Plan Mode by toggling off "Accept Edits." In Plan Mode, Claude does not modify any files—it only asks questions and helps you design a concrete implementation plan. Craft your first prompt to describe the dashboard you want. For example:

"I want to create a trading dashboard that I update every day with the trades I took and the best ops of the day. I want to model it after a template dashboard with three images of trading dashboards that I attached. I want to include tabs for tracking trades, best ops, and problem patterns. I want to use ask-user-question mode for every tab I want on the dashboard. Since we're in plan mode, ask me questions for every major decision. Do not decide anything yet. Batch three to four questions per round. After each batch, update the plan document."

Claude will then ask questions in batches of three or four. Answer each batch, and after each round Claude updates the plan document. Continue answering questions until Claude signals it has enough information. Typical questions include:

- What platform should the dashboard live on? (Choose: local HTML single-page app you open in a browser)
- Where should dashboard data live? (Choose: daily entries, notes, tags—human-readable format)
- How does data get into the dashboard each day? (Manual entry, auto-pull script, or defer)
- What is this dashboard for? (Select all that apply: historical review, coach accountability view)
- What are best ops? (Setups you saw and didn't take, setups you took, market-wide)
- What are patterns/trade tags? (Similar to TraderView tags, plus identified tendencies for grouping trades)
- What should the end-of-day routine ask? (Trade write-ups, best ops)

Once all questions are answered, Claude will generate a complete .md implementation plan document. Save that file.

### Step 2: Build Mode — Build the Skeleton

Start a new Claude Code session (or stay in the Plan Mode session from Step 1), make sure you are NOT in Plan Mode (toggle "Accept Edits" ON), and paste your saved .md implementation plan into the session. Tell Claude: "Here's my implementation plan for a trading dashboard that I'm trying to build. I want you to build the skeleton of this."

Claude will then build the full HTML dashboard skeleton. Once it finishes, you will get a link to open the dashboard in your browser. No further coding is required on your part during this step—Claude builds the HTML dashboard skeleton and provides you a browser link.

### Step 3: Personalize the Dashboard

Open the dashboard in your browser using the link Claude provided. Review what was built. Now go back to Claude Code (still in Build Mode / Accept Edits ON) and start making one-off, personalized changes. Examples of personalization include:

- Adding tabs you originally missed (e.g., a "Tendencies" tab)
- Modifying charts to show exact accuracy percentage and cumulative profit and loss (P&L) on the X axis instead of just letter grades (A+, A, A-, B)
- Incorporating your trading playbook rules, the specific conditions you look for before entering a trade (your "checks in favor"), and your execution rules into dedicated tabs
- Adding a performance coach layer that reviews trade write-ups and identifies recurring mistakes
- Adding a "strengths" or goals section
- Backfilling old trades so the dashboard shows historical data and graphs

Continue iterating in Build Mode until the dashboard matches your implementation plan and includes all tabs and stats you defined in Step 1.

### Step 4: Set Up a Routine (Make It Repeatable)

Once the dashboard is built and personalized, make the workflow repeatable by setting up a Claude Code Routine. Tell Claude you want a routine scheduled for after the regular U.S. equities market session ends (Eastern Time), at a specific time each day (e.g., 4:15 PM ET or 4:30 PM ET). Define what questions Claude should ask you during that routine to update the dashboard. For example, Claude can prompt you:

- "What trades did you take today?"
- "Do you want to add anything to the journal?"
- "What were the best ops of the day?"
- "What pattern does this trade fall under?"

Claude will then auto-populate the dashboard based on your answers. You can also set routines for before the regular U.S. equities market session opens (pre-market, before 9:30 AM ET) or for weekly review intervals. The key is that once the routine is set up, you only need to respond to Claude's prompts—Claude handles the prompting and the dashboard updates automatically.

## Examples

### Example 1: A Performance-Based Trading Dashboard With Coach Layer

Tim, co-host of the Trading Floor podcast (available on Spotify), built a dashboard that tracks every trade taken in 2026, splits results by grade (A+, A, A-, B), and shows cumulative P&L. He added a "Tendencies" page that displays recurring patterns like "no man's land sizing" (mentioned five times in trade write-ups) and "end-of-month B cap" (where he catches himself over-grading B trades). He also added a performance coach layer: every time he inputs a new trade write-up, Claude reviews his stats, tendencies, and journal entries, and produces a coach's note like, "Those were two no man's land sizing trades today—something we really want to keep an eye on."

### Example 2: A Dynamic Resource / Setup Grading Dashboard

Garrett, co-host of the Trading Floor podcast (available on Spotify), described building a dashboard focused on his specific plays: tracking catalysts, setups that are working vs. not working, and grading setups. He wants Claude to understand his checks in favor and variables for each play, then help him grade new setups by comparing them against his historical trade data. For example, if a breakout trend trade closes right at the breakout level, Claude could pull up all similar past setups and show: "You've taken 20 breakout trend trades in the past year. 70% closed above the level and worked. None closed below and worked. Consider lowering the grade or getting flat."

### Example 3: A Simple Daily Review Dashboard With Routine

A trader with no coding background can build a minimal dashboard in a single afternoon by following the four steps. They can set up a Claude Code Routine that triggers after the regular U.S. equities session closes (Eastern Time), asks for trades taken, best ops, and journal notes, then auto-updates an HTML dashboard file on their computer. No need to enter trade data separately into TraderView; you enter it directly into the dashboard via the Claude Code routine.

## Best Practices

- Start in Plan Mode and complete the full brainstorming process before switching to Build Mode—this reduces the amount of debugging and rework after switching modes
- Use ask-user-question mode during Plan Mode; batching 3–4 questions per round and updating the plan document after each batch keeps the process organized and reduces the number of typed tokens used in the session
- Attach template images (e.g., screenshots of TraderView pages you like) to your initial prompt so Claude has a visual reference for the end goal
- Save the .md plan file and use it as the input to a fresh Build Mode session—do not try to build and plan in the same session
- Be specific in your trade write-ups and journal entries—the more context you give Claude, the more accurately it can detect patterns in your trading behavior and include them in a coach's note
- Keep the dashboard focused on features that directly answer a question you have before or after taking a trade; remove features that do not inform a decision you actually make
- Set up a Claude Code Routine so the daily journaling process is automatic and consistent

## Keep In Mind

- The quality of what Claude can detect in your trading depends on the detail in your write-ups. Trade entries that include executions, allocation grades, accuracy assessments, mistakes, and reasoning give Claude more material to work with; entries with minimal detail limit what it can surface.
- Use Claude as an information organizer and pattern detector, not as a decision-maker for entries or exits. Write a clear instruction defining Claude's role so it summarizes past performance rather than instructing you to trade.
- You can continue personalizing the dashboard further over time. Step 3 is an ongoing process as you discover new ideas.
- The four-step workflow is reusable for building trading-related tools such as dashboards, resource pages, and setup graders—not just one type of dashboard. In your initial prompt, replace the trading-specific terms (for example, "trading dashboard," "trades," "P&L") with terms relevant to the tool you are building.

## Security & Safety Notes

- The dashboard is a local HTML file that opens in a browser. It lives on your machine and is not hosted online, so your trade data stays private.
- Do not share your Claude Code session or implementation plan file publicly if it contains private trading data, account details, or personal strategy information.
- Review any code Claude generates before using it, especially if you modify the dashboard to connect to external APIs or brokerages.
- Claude Code can manipulate files on your computer. Keep your trading data folder separate from system directories and outside other sensitive project folders.

## Common Pitfalls

- **Problem:** Jumping straight into Build Mode without a plan, leading to messy code and constant rework.
  **Solution:** Complete Step 1 (Plan Mode) first. Let Claude write the full .md plan, review it, and only then switch to Build Mode.
- **Problem:** Overloading the initial prompt with too many requirements at once, causing Claude to miss key details.
  **Solution:** Keep the first prompt focused. Use the structured ask-user-question flow in Plan Mode to add details incrementally.
- **Problem:** Building a dashboard full of charts and stats that do not inform entry or exit decisions.
  **Solution:** Focus each tab and stat on a specific question you need answered before or after taking a trade. Cut anything that does not improve your entry or exit decisions.
- **Problem:** Forgetting to backfill old trades, so the dashboard has no historical context for pattern detection.
  **Solution:** Enter your recent trades after building the skeleton so Claude has data to analyze.
- **Problem:** Letting Claude make entry or exit decisions instead of just providing information.
   **Solution:** Write a clear instruction framing Claude's role as a coach and organizer. Do not ask it to tell you whether to enter or exit a trade—ask it to summarize your past performance in similar setups.