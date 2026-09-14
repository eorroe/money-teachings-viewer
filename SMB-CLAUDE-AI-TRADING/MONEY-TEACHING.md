# How To Build Your Own Claude AI Trading Assistant

## Overview

This Money Teaching guides traders through building an AI trading assistant using Claude Code (CLI) or Claude.ai web interface, even with no formal coding background. The approach focuses on operational efficiency (reducing the time spent on repetitive data gathering and formatting tasks) rather than prediction, helping traders automate manual daily processes like pre-market research, trade tracking, and market scanning. Justin Speiro, a trader at SMB Capital, demonstrates how he built an AI-powered pre-market research dashboard in 18–22 hours that now saves him approximately 60 minutes each morning.

## When to Follow These Money Teachings

- When you want to automate a repetitive daily trading workflow such as email research, trade tracking, or market scanning
 - When you have little or no coding experience but want to build trading tools
 - When you're spending at least one hour per trading day on manual research and want to free up time for actual trading
 - When you want to create dashboards tailored to your specific trading setups, rules, and blacklisted tickers
 - When you need to process data for stocks with at least 100,000 shares of average daily volume efficiently

## Steps

### Step 1: Identify a Daily Manual Process to Automate

Look at your current daily workflow and find a repetitive task you do manually. Examples include scanning research emails, tracking trades, reviewing economic calendars, or monitoring pre-market scanners. Justin started by identifying that he was spending his morning going through roughly 100 research emails. The key is to pick something you already do consistently, so you know exactly what the end result should look like.

### Step 2: Open Claude Code (CLI) or Claude.ai web interface and Describe Your Goal

Launch Claude Code and simply describe what you want to build in plain language. This is called "vibe coding." For example, say: "I want to build a dashboard that tracks my trades. I want to be able to upload my trade data at the end of the day and then see my win rate, win-loss ratio, average losing trade, average winning trade, and any other statistics you specify." The more specific and articulate you are about what you want, the better the output. If you struggle to express exactly what you need, use another LLM like ChatGPT to help refine your description, then copy and paste that into the Claude interface you are using.

### Step 3: Use Plan Mode to Brainstorm Before Building

Before Claude starts coding, switch to plan mode where you brainstorm and create a project brief. Ask Claude to think through the approach, what data you need, how the output should be structured, and what the workflow looks like. Iterate on the brief until it accurately captures what you want to accomplish. Only once you are satisfied with the plan should you switch to build mode.

### Step 4: Iterate and Fix Issues as They Arise

You will encounter problems where Claude does something incorrectly or produces output that does not match your expectations. When this happens, go back and correct it directly. Tell Claude specifically what is wrong and how to fix it. Justin notes that his pre-market research report is now on its third major iteration because he iterated on it daily. Treat debugging as part of the process. Justin finds the iteration process enjoyable rather than frustrating. Ask the Claude interface you are using "why did you do that?" to understand its reasoning, and ask "if you were me, how would you be doing this differently?" to get improvement ideas.

### Step 5: Teach the AI About Your Trading Business and System

Generic AI output is only as good as the data and context you give it. To make your assistant truly tailored to your trading playbook, rules, and blacklisted tickers, feed it information about how you trade. Share your playbook, your trade confirmation criteria, your blacklisted tickers, your position sizing preferences, and examples of past good trades. Justin spent approximately four to five hours going line by line through his trading analysis script to teach Claude every parameter and why each line exists. The more the AI knows about your specific style, the more valuable its output becomes.

### Step 6: Incorporate Real Data Sources

Your assistant is only as good as the data it processes. Sign up for six free newsletters and research sources such as Vital Knowledge, Hammerstone Reports, MarketWatch, Wall Street Journal, Bloomberg, and Trade the News. You can also have the AI scrape public data like 8-K filings (SEC material event filings), earnings call transcripts, and company websites. The AI can then parse and synthesize all of this into a single morning briefing, saving you about an hour every day.

### Step 7: Build Simple Widgets or Advanced Scanners

Start small and scale up. A simple first project might be a risk widget that sits on your screen and reminds you what your daily position sizes are for A+ setups (highest conviction), A setups (strong), B setups (marginal), and C setups (avoid). As you get comfortable, build more complex tools such as pre-market scanners, ThinkScript or TradingView studies, or backtesting scripts. For example, Justin built a low float scanner that filters for stocks with price greater than or equal to $0.20 and less than $10.00, excludes OTC (over-the-counter) stocks, requires at least 100,000 average daily cumulative volume, and is gapping up by at least 2% above the prior-day close, then sorts by dollar volume.

### Step 8: Validate and Refine Continuously

Never take the AI's output at face value. Always check for bad or outdated data. For example, Justin's AI once reported the VIX (CBOE Volatility Index) at 22 when it had actually moved to 19 because no recent email contained the updated number. If a data point does not exist in the parsed emails, you must explicitly tell the AI to exclude that data point. Also set personal filters: if Snapchat is blacklisted for you, tell the AI so it does not recommend it as a top idea. Review the output every morning and send corrections back to the Claude session you are using so it improves over time.

## Examples

### Example 1: Pre-Market Research Dashboard

Justin built a dashboard that runs every morning and produces a macro rundown. It starts with the most important overnight development, provides an economic calendar rated by importance (such as MBA (Mortgage Bankers Association) mortgage applications at 7:00 a.m. marked as low importance), lists key events like Tax Day or historical retail buy-the-dip dynamics, summarizes earnings that came out in pre-market, and then identifies what the AI thinks will move the market most that day along with the catalysts. It also surfaces secondary names from research emails with quick notes. This project took 18–22 hours initially; it can now be rebuilt in approximately 60 minutes if needed.

### Example 2: Trade Tracker Dashboard

 A trader with little or no coding experience could build a dashboard where they upload their end-of-day trade data and the AI calculates win rate, win-loss ratio, average winning trade, average losing trade, and any other statistics they specify. This replaces manual spreadsheet work and gives a TradingView-like interface without any coding.

### Example 3: Low Float Scanner

Justin built a scanner that looks for low float stocks gapping up. Parameters: price greater than or equal to $0.20 and less than $10.00, excludes OTC stocks, average daily cumulative volume at least 100,000 shares, and gapping up by at least 2% above the prior-day close. Results are sorted by dollar volume. During the week of April 15, this scanner identified runners like Bird (IRD) and Snail (SNAL), with daily dollar volume between $1 billion and $4 billion.

### Example 4: ThinkScript or TradingView Study

If you use ThinkorSwim or TradingView, Claude Code can build studies that would normally require learning proprietary scripting languages. For example, a study that compares today's cumulative volume to the cumulative volume over the last five regular trading sessions (09:30–16:00 ET) at that same intraday timestamp. This kind of study would require manual workarounds in ThinkScript, but Claude can generate it quickly.

### Example 5: Gap Up Backtest Script

Tim, a trader at SMB Capital, described building a backtesting script where you pull the last year of data for stocks that gapped up by 0.5 × the 14-day Average True Range (ATR), where 0.5 ATR is a common threshold for identifying meaningful intraday gaps, compute stats like how many times it happened, what the average close was, what percentage closed green versus red, and the average move from open to high. This gives you conviction on whether a setup is worth trading before you actually press the keys.

## Best Practices

- ✅ Start by identifying a specific daily process you already do manually and describe it to Claude in plain language
- ✅ Use plan mode in Claude Code to brainstorm the full project brief before switching to build mode
- ✅ Refine your prompts using ChatGPT or another LLM when Claude does not understand what you want
 - ✅ Teach Claude about your trading playbook, rules, blacklisted tickers, and past good trades to tailor the output to your trading setups
 - ✅ Subscribe to six free newsletters including Vital Knowledge, Hammerstone Reports, MarketWatch, Wall Street Journal, Bloomberg, and Trade the News
- ✅ Review AI output every morning and immediately correct mistakes so the tool improves over time
 - ✅ Use your own previously written scripts or templates as a starting point when building automated models or backtests (for example, a script you have previously written that pulls the last year of data for stocks gapping up by 0.5 × the 14-day Average True Range (ATR), where 0.5 ATR is a common threshold for identifying meaningful intraday gaps, then computes win rate, percentage of green closes, average close, and average move from open to high)
- ✅ Isolate the mutable "control center" of a script — the entry and exit trade logic — while keeping the data collection and feature pipelines intact

## Keep In Mind

- A practical advantage with AI is operational efficiency (reducing the time spent on repetitive data gathering and formatting tasks): how quickly you prepare, how organized your process is, and how effectively you execute on your trading ideas. It is not about getting AI to predict where a stock is going.
- AI trading assistants are not "set it and forget it." They require regular review and updates. Justin's dashboard is on version three and he still identifies refinements to implement daily.
 - The quality of the output depends heavily on the quality of the data you feed it. If you only read one news source, an AI summary is less valuable because you lose the benefit of cross-referencing multiple perspectives. The value comes from cross-referencing at least six independent sources — so first identify and subscribe to at least six qualifying news or research feeds before aggregating.
- You do not need to be a coder to build useful tools. Justin had minimal coding experience when he started. However, some basic coding literacy helps with debugging and making small manual adjustments.
- The time you save can be used for other activities such as building more complex models, refining your playbook, or simply having more time outside of work.

## Security & Safety Notes

 - Never share proprietary trading algorithms, API keys, or sensitive financial data with AI tools hosted on cloud-hosted AI services (Claude API, ChatGPT), shared team environments, or any server you do not fully control where data could be accessed by unauthorized parties
 - Always verify AI-generated market data, prices, and economic figures against official exchange data, SEC filings, or established financial data providers before making trading decisions
- Be aware that AI can produce outdated information if it is not in the dataset it parsed; set explicit rules to exclude data that does not exist in your feeds
- Do not let the AI execute live trades without your explicit review and approval; use it for research, preparation, and analysis only
 - Keep personal filters such as blacklisted tickers, maximum position sizes, and risk management rules (for example, maximum daily loss limits) configured so the AI does not suggest trades outside the strategy you have documented and taught to the AI

## Common Pitfalls

- **Problem:** The AI produces generic recommendations that do not match your trading style (your specific setups — such as breakouts, mean reversion, or catalyst plays — your position sizing rules for A+ setups (highest conviction), A setups (strong), B setups (marginal), and C setups (avoid), and your blacklisted tickers)
  **Solution:** Spend time teaching the AI about your playbook, your pre-trade conditions that must be true before entering a position, your rules, and examples of your best trades. The more context you provide, the more personalized and useful the output becomes.
- **Problem:** The AI reports outdated or incorrect data such as outdated VIX levels that no longer reflect current market conditions
  **Solution:** Review the output daily. When you catch an error, go back and tell Claude to exclude that data point if it is not present in your parsed sources. Treat it as a project that improves with each iteration.
- **Problem:** You get stuck on a prompt and Claude keeps producing output that does not match your intended strategy logic, data collection approach, or trade rules
  **Solution:** Use a separate LLM like ChatGPT to help you refine your prompt into clearer, more specific language. Then copy the improved prompt back into Claude. You can also use Claude's plan mode to brainstorm before building.
- **Problem:** The tool suggests tickers or trades that you would never take
  **Solution:** Explicitly tell the AI which tickers, sectors, or asset classes are blacklisted for you. Remind it that its suggestions are just ideas for you to evaluate, not direct trade recommendations.
- **Problem:** You spend more time debugging the AI assistant than saving time
  **Solution:** Start with a single-function project that requires fewer than 200 lines of code and solves one specific pain point. Expand gradually as you learn how to prompt effectively. The initial effort pays off once you have a working baseline.
