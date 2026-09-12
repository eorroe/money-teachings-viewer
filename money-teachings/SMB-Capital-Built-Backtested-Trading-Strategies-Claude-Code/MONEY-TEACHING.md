# I Built & Backtested Trading Strategies with Claude Code

## Overview

This video teaches traders how to leverage Claude Code to build, backtest, and automate trading strategies using a disciplined, process-driven approach inspired by SMB Capital, a proprietary trading firm known for its professional trading desk and trader training. You will learn to use Claude for strategy development and research while maintaining human oversight, realistic backtesting standards, and automated execution to remove emotion from trading. The core message is that AI writes the code, but you supply the edge through preparation, verification, and disciplined rule-following.

## When to Follow These Money Teachings

- When you want to build algorithmic trading strategies using AI without writing Pine Script manually
- When you need to backtest strategies on TradingView with realistic execution costs
- When automating TradingView alerts to a broker or prop firm account
- When you want to use Claude Code as a research and strategy design tool for trading
- When you are setting up or evaluating a prop firm trading account with automated rules

## Steps

### Step 1: Design Your Strategy Logic in Plain English

Before opening Claude Code, write down your strategy clearly: entry conditions, filter conditions, exit logic, stop-loss and take-profit rules, and the timeframe you are trading. The more specific you are—such as "9 EMA crosses above 21 EMA on a 15-minute chart, only during the first 3 hours of the NYSE session, with RSI between 40 and 60"—the better Claude's output will be. Avoid vague prompts like "a moving average crossover."

### Step 2: Build the Strategy with Claude Code

Open Claude Code and prompt it with your detailed strategy description. Ask it to generate Pine Script v6 code for TradingView. Claude can build strategies in under 10 minutes from a single prompt, and it may ask clarifying questions that improve the logic. Do not manually edit the code unless you understand what you are changing.

### Step 3: Backtest on TradingView with Realistic Settings

Paste the generated Pine Script into TradingView's Strategy Tester. Before trusting results, configure realistic parameters: set commission to 0.04–0.05% per side (or $4–$5 per futures contract), set slippage to 1–2 ticks, and define position sizing as a percentage of account rather than arbitrary contract counts. A strategy must still show positive expectancy—above 1.0R average (where R equals your risk per trade) and above 45% win rate for trend-following systems, or above 55% for mean-reversion systems—to proceed.

### Step 4: Verify the Output and Avoid Technical Debt

Treat Claude's output like a research note from a junior analyst: it is a starting point to pressure-test, not a verdict to accept. Never trade a number Claude cites without checking the primary source. Review the code for logical errors, curve-fitting (over-optimizing to past data), and regime sensitivity (how the strategy performs across different market conditions). Strategies with trend filters (such as a 200 EMA) tend to filter out weak entries during low-volatility periods and tend to perform better than those without.

### Step 5: Automate Execution with a Rules-Based System

Once the strategy passes realistic backtests, connect it to automated execution. Use a webhook or alert service to route TradingView signals to your broker or prop firm account. This enforces your stop-loss, take-profit, and position-sizing rules without emotional interference. For prop firm accounts, automated rule enforcement is essential to prevent loss-limit violations caused by discretionary overrides.

## Examples

### Example 1: EMA Crossover with RSI Filter

Prompt: "Write a Pine Script strategy that goes long when the 9 EMA crosses above the 21 EMA, only if RSI(14) is between 40 and 65. Exit on opposite crossover or 1.5% loss. Add a daily trend filter using the 200 EMA." Backtest with 0.05% commission and 1-tick slippage. In backtesting, this strategy outperformed the benchmark.

### Example 2: Breakout Momentum with ATR Sizing

Prompt: "Create a breakout strategy that enters on a 4-candle high breakout with volume 1.5x the 20-bar average. Use ATR(14) to set stop loss at 1.5x ATR below entry. Trail profit at 2x ATR." After realistic backtest validation, this strategy was automated and performed well in testing.

### Example 3: Review Trade Journal with Claude

Export your trade journal to Claude and ask it to cluster wins and losses by setup, time of day, position size, and emotional notes. Claude can surface patterns faster than manual review—for example, revealing that 70% of losses come from trades taken in the first ten minutes or from sizing up after a win. Use those insights to refine your trading playbook (a documented record of your strategies and trade reviews) and pre-market preparation routine.

## Best Practices

- ✅ Design strategy logic in plain English with specific constraints before prompting Claude
- ✅ Backtest with realistic commission and slippage settings (0.05% commission, 1-tick slippage)
- ✅ Verify every output from Claude against original data sources and your own pre-written rules
- ✅ Automate execution so rules, not impulsive decisions driven by fear or greed, govern every trade
- ✅ Build a trading playbook (a documented record of your strategies and trade reviews) and review every trade to identify repeated setups that appear multiple times in your trading history and mistakes
- ✅ Prepare before the open by using Claude to rank watchlist names with identifiable catalysts (such as earnings reports, FDA decisions, or product launches) versus noise
- ❌ Do not ask Claude to predict stock prices or forecast market direction
- ❌ Do not let Claude size positions or place trades unsupervised
- ❌ Do not accept backtest results from default TradingView settings (zero commission, zero slippage)
- ❌ Do not skip the verification layer between Claude's output and your broker

## Keep In Mind

- AI generates syntax, not validated logic against live market conditions. LLMs may replicate over-fitted strategies published online.
- Backtest results are often too optimistic when default settings are used. Always apply realistic friction.
- A documented process improves results over time through repeated review and refinement. Codify your rules, review them, and repeat them.
- The edge comes from disciplined execution, not from the AI tool itself. Retail traders using AI often report lower profitability than expected.
- Strategies with trend filters tend to perform better during low-volatility regimes than those without.

## Security & Safety Notes

- Never share API keys, broker credentials, or account passwords with Claude or any AI assistant.
- Keep your own rules and judgment between Claude's suggestions and actual trade execution.
- Verify all numerical data, indicator values, and financial claims Claude produces against primary sources.
- Use webhook-based automation through reputable platforms rather than giving AI direct broker access.
- Review all generated code before deploying it to a live or prop firm account to prevent unintended behavior.

## Common Pitfalls

- **Problem:** Accepting Claude-generated backtest results from TradingView's default settings.  
  **Solution:** Always set commission to 0.04–0.05% per side, slippage to 1–2 ticks, and position sizing to a percentage of account before evaluating any strategy.

- **Problem:** Using vague prompts that produce generic, untestable strategy code.  
  **Solution:** Describe entry conditions, filter conditions, exit logic, timeframe, and session constraints with specificity.

- **Problem:** Overfitting to short backtests and assuming future performance will match.  
  **Solution:** Require testing across multiple market conditions—trending, ranging, high-volatility, and low-volatility—before going live.

- **Problem:** Automating raw AI signals without a human verification layer.  
  **Solution:** Treat Claude as a research analyst. Verify every signal against your pre-written rules and never let it size positions or place trades unsupervised.

- **Problem:** Ignoring regime sensitivity and market context changes.  
  **Solution:** Add trend filters (such as a 50 EMA or 200 EMA) to filter out weak entries during low-volatility periods, and re-evaluate strategies when market behavior shifts.