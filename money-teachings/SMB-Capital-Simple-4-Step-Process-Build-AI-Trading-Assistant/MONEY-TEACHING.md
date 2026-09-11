# The Simple 4-Step Process To Build Your Own AI Trading Assistant With Claude (for Beginners)

## Overview

This Money Teaching walks through SMB Capital's simple 4-step framework for building a personal AI trading assistant using Claude, even with no coding experience. It covers how to plan your workflow, generate custom trading tools, personalize them to your style, and automate your daily routine. The goal is to remove time-consuming preparation and execution bottlenecks (e.g., building watchlists, writing scripts, reviewing trades) so you can focus on trading.

## When to Follow These Money Teachings

- When you want to build a personal AI trading assistant without extensive coding experience
- When working with Claude to generate custom trading tools like alerts, dashboards, or trade journals
- When the user asks about automating pre-market research, trade review, or order logic with AI

## Steps

### Step 1: Plan Mode

Before you start building, define exactly what you want your AI assistant to do. Write down your trading process, identify the specific bottlenecks that slow you down (e.g., data gathering, analysis, journaling), and specify the outputs you need. Be detailed about your requirements, including inputs, rules, and desired formats. The clearer your plan, the better Claude can build the right tool.

### Step 2: Build Mode (Let AI Do the Work)

Take your plan and feed it into Claude. Describe what you want in simple, direct language—Claude will write the code, build the scripts, and create the tools for you. You do not need to be a programmer. Provide explicit rules, logic, constraints, and formatting requirements, and Claude handles the implementation.

### Step 3: Personalization (Make It Yours)

Once Claude produces the initial version, refine it. Adjust prompts, modify logic, and tailor outputs to match your specific trading style (e.g., day trading, swing trading, scalping) and personal trading playbook (e.g., your written entry/exit rules, risk parameters). Iterate by requesting changes until the tool fits your workflow. This step transforms a generic solution into a personalized trading assistant.

### Step 4: Automate Your Daily Routine

Set up schedules, integrate the assistant with your existing tools (e.g., TradingView, broker platform, Google Sheets, Discord), and let it handle repetitive tasks automatically. This includes pre-market research briefings, trade journaling, performance analysis, and alert monitoring. Automation lets you focus on execution while AI handles the grunt work.

## Examples

### Example 1: Custom TradingView Alert

Use Claude to build a Pine Script v5 indicator and alert that triggers when price breaks above the 30-minute opening range high with volume at least 1.5x the opening range average, price above VWAP, and within the first 2 hours of the session. Include visual requirements like horizontal lines and background color changes.

### Example 2: Pre-Market Game Plan Automation

Feed Claude a watchlist with overnight news and pre-market data, and ask it to analyze each stock for catalyst strength (e.g., earnings, FDA decisions, macro events), price action (e.g., trend direction, support/resistance tests), key levels (e.g., prior day high/low, VWAP, moving averages), setup potential (e.g., matching your predefined entry criteria), and priority ranking (e.g., rank 1-5 by setup clarity and catalyst quality). The output is a clean table and market context summary you can review before the open.

### Example 3: Custom Trade Journal and Performance Analysis

Ask Claude to build a Python script that imports broker CSV data and analyzes performance by setup type (e.g., opening range breakout, VWAP reclaim, moving average bounce), time of day (e.g., first 30 minutes, midday, last hour), and day of week. The script should calculate win rates, average wins and losses, expectancy, and flag time periods where win rate falls below your personal baseline threshold (e.g., below 40% win rate over 20+ trades).

### Example 4: AI Trade Autopsy

After a trade, paste the setup details (ticker, date, setup type), entry and exit rules (planned vs. actual prices, stop loss, target), and your actual behavior (e.g., moved stop early, added to a loser, exited early) into Claude and ask it to evaluate whether you followed your written plan, which specific behavioral patterns you exhibited (e.g., FOMO entry, revenge trading, premature exit), and which rules or behaviors to prioritize improving in your next 5 trades.

## Best Practices

- ✅ Define clear objectives, explicit rules, and structured inputs before asking Claude to build anything
- ✅ Follow the prompt pattern: clear objective, explicit rules, structured inputs, defined output format, and constraints
- ✅ Keep a human in the loop—never let AI size positions or place trades unsupervised
- ✅ Build a verification step into every workflow and keep your own rules in charge
- ✅ Use AI to codify process over prediction; ask Claude to help write your rulebook, not to predict the market

## Keep In Mind

- AI is not here to replace your thinking. It is here to remove time-consuming bottlenecks in preparation (e.g., building watchlists, scanning for setups), review (e.g., analyzing trade performance, journaling), execution (e.g., order entry, position sizing), and infrastructure building (e.g., coding dashboards, backtesting scripts).
- The better you describe what you want, the better the AI can build it.
- Consistency comes from repeatable rules, not market forecasts.

## Security & Safety Notes

- Never let Claude size positions or place trades unsupervised.
- AI can state a wrong answer with the same confidence it states a right one—always verify outputs before acting on them.
- Do not paste sensitive account credentials or proprietary strategy details into public AI interfaces.

## Common Pitfalls

- **Problem:** Asking Claude "will this stock go up?" instead of using it to codify your process.
  **Solution:** Reframe prompts around building repeatable rules, dashboards, and review tools rather than seeking predictions.
- **Problem:** Skipping the Plan Mode and jumping straight to building vague or undefined tools.
  **Solution:** Spend time in Step 1 writing down exactly what the tool should do, what data it needs, and what output format you expect.
- **Problem:** Letting the AI run trades or manage risk without human oversight.
  **Solution:** Keep execution and position sizing under your direct control. Use AI only for preparation, analysis, and infrastructure.
