# SMB ONE-PROCESS

## Overview

This money teaching distills the systematic trading process shared by Dave Mabe with SMB Capital on the Trading Floor podcast. The core message is that a trading strategy fails not because the initial signal is weak, but because the trader lacks a rigorous process for developing, optimizing, and refining that strategy through backtesting. By building a personal column library, casting a wide net with initial backtests, using optimization tools to identify high-impact rules, reviewing trades daily, and collaborating with diverse traders, you can systematically turn any strategy idea into a strategy with positive returns that you can fully explain and defend.

## When to Follow These Money Teachings

- When you are building or refining a trading strategy and want to move beyond guess-and-check backtesting
- When your backtests do not produce the trade count or return level that matches your strategy requirements
- When you are unsure how to use optimization without overfitting
- When you want to build a reusable set of indicators (columns) that improves every strategy over time
- When you are reviewing trades and noticing patterns you cannot explain or strategies that consistently underperform
- When you need to decide on stop placement, profit targets, or trade filtering rules
- When you want to collaborate with other traders to generate new strategy ideas

## Steps

### Step 1: Take Full Ownership of Your Strategy

Do not rely on someone else's strategy or unshared logic. You must build or deeply adapt your own system so that you understand why it works, what its weaknesses are, and how to fix it when drawdowns occur. If you cannot explain why the strategy works, you will abandon it when the strategy enters drawdown.

### Step 2: Cast a Wide Net With Your First Backtest

Do not optimize for the final answer on the first attempt. Set thresholds lower than your initial assumption. For example, if you think a gap strategy requires a 5 percent gap, backtest with 3 percent to capture more trades. This gives the optimization tool more data points to identify the threshold that produces the highest risk-adjusted returns for your dataset.

### Step 3: Build and Maintain a Column Library

Create a shared library of indicators (columns) that you include in every backtest. Start with a brainstormed set and add to it over time. Examples include ATR, relative volume, position in range, yesterday's range, distance from open in ATR units, and custom measures you invent. A column library with 200 or more indicators increases the probability that optimization will find statistically significant rules.

### Step 4: Use an Optimization Tool to Identify High-Impact Rules

Run your backtest through a tool such as the Strategy Cruncher that ranks columns by their predictive importance and shows the optimal cutoff for each. Apply only the rules that rank highest in predictive importance to keep the strategy simple. Do not fear specific optimal values such as 3.8% for a gap threshold; threshold values do not need to be round numbers.

### Step 5: Determine Optimal Stops

Run an initial backtest with no stop and no target, only a time stop. Use the resulting trade data to calculate MF (maximum favorable excursion) and MAE (maximum adverse excursion) for every trade. MF and MAE analysis identifies stop levels based on actual trade excursion data. Then run the backtest again with that optimal stop in place to create your realistic trade set for optimization.

### Step 6: Decide on Profit Targets Carefully

Avoid taking partial profits and moving your stop to break even. Backtesting shows that holding full size to a target or to the close of the day produces a higher risk-adjusted return. Partial profits reduce total returns over time. Letting winners run to target produces the majority of returns. Test both approaches on your own data to see the specific tradeoff.

### Step 7: Review Every Trade Daily

At the end of each day, examine every trade your strategy took and every trade it skipped. Ask why the model took or skipped each one. Look for situations where the model skipped a trade that your strategy rules suggest should have been taken. Reviewing skipped trades reveals gaps in the column library or rules that need adjustment.

### Step 8: Seek Out the Unusual

Place yourself in a position to notice unusual market activity every day. Maintain a running list of observations, anomalies, and "almost met criteria" trades. Strategy ideas come from near-miss trades. Reviewing near-miss trades reveals new strategy rules outside your current filters.

### Step 9: Run Thought Experiments to Create Inverse Strategies

If your primary strategy is long, deliberately design a strategy that takes the opposite position in the same universe. Ask: what criteria define the trades that stopped out in the short strategy, and could I create a long strategy from those same criteria? This design process uncovers independent strategies based on the same raw idea, creating multiple strategies from a single concept.

### Step 10: Avoid the Guess-and-Check Loop

Traders who skip the process create a backtest, see poor results, make an adjustment without statistical justification, and run again. This cycle does not produce a consistently profitable strategy. Instead, commit to a process: wide-net backtest, column library, optimization tool, single-rule application, chart review, and iteration. A defined process produces higher risk-adjusted returns than ad-hoc adjustments.

### Step 11: Collaborate With Traders Who Do Things Differently

Seek out traders with different strategy types such as day trading versus swing trading, different timeframes, and different market focuses such as equities versus futures. Share openly and ask how they think about the market. Their perspectives generate strategy ideas you would not develop alone. Building trust and being a "giver not a taker" is the foundation of these relationships. Building a network of traders supports strategy development.

## Examples

### Example 1: Gap Strategy Optimization

Dave Mabe's first strategy looked for stocks gapping above a threshold with a tight range in the first 30 minutes, then going long on a breakout. Initially he assumed 5% was the right gap threshold. After casting a wider net with 3%, the optimization tool revealed additional profitable trades between 3% and 5%. He increased his trade count by letting the tool find the threshold that produced the highest returns rather than imposing his assumption upfront.

### Example 2: Inverse Gap Strategy

While trading the gap strategy long, Mabe noticed that some of the gapping stocks would gap up, break out, then immediately tank and stop him out. Instead of just accepting these losing trades, he created a completely separate strategy that went short on the same conditions. Because it was isolated with its own rules and universe filters, he could run both long and short strategies without conflicting positions. The losing longs became the basis for a profitable short strategy.

### Example 3: Position in Range Filter

In a gap strategy, a trade that triggers when price is in the upper portion of today's range produces higher returns for a long position than a trade near the bottom. By adding a "position in range" column (0 = near low, 100 = near high) to the column library and running it through the optimizer, the tool confirmed that only trades above the 70th percentile should be taken. This single rule eliminated 30 percent of losing trades and improved strategy consistency.

### Example 4: Adam Grimes and the One R Profit Target

Adam Grimes believed that holding for gains of at least 1R produced higher risk-adjusted returns. When someone suggested he try a one R profit target (selling as soon as the trade made as much as he was risking), he resisted. Backtesting showed the one R target produced a higher total return. Grimes adopted it contrary to his prior belief, demonstrating that backtesting can contradict initial assumptions when the process is trusted.

### Example 5: Daily Review of Skipped Trades

Garrett and Tim at SMB review trades their model did not take. If they see a stock like Tesla that matched the strategy criteria except for one filter, they investigate why. Reviewing skipped trades leads directly to brainstorming modifications or new columns that can capture that edge, turning near-misses into strategy improvements or entirely new strategies.

## Best Practices

- ✅ Start every first backtest with a threshold at least 2 percentage points lower than your initial assumption to cast a wide net
- ✅ Build a column library once and reuse it across every strategy
- ✅ Use an optimization tool rather than manual guess-and-check
- ✅ Run your first backtest with no stop and no target, then use MF and MAE analysis to identify exit levels
- ✅ Apply only the highest-ranked rules to keep strategies simple
- ✅ Review every trade and skipped trade daily
- ✅ Maintain a running list of unusual observations and near-miss trades
- ✅ Design inverse or complementary strategies to capture ignored edges
- ✅ Share openly with traders who have different strategy types and market focuses
- ✅ Test controversial ideas like one R targets or no targets on your own data before rejecting them
- ❌ Do not manually tweak thresholds between backtests without statistical justification
- ❌ Do not fear curve fitting to the point of inaction; start with at least 200 trades and let tools identify statistically significant rules
- ❌ Do not take partial profits and move stops to break even without testing the math
- ❌ Do not abandon a strategy during a drawdown of less than 10 percent if you did not build and understand it yourself
- ❌ Do not hoard ideas; sharing strategy concepts generates reciprocal collaboration

## Keep In Mind

- The signal is one of the least important parts of a strategy; the optimization process determines trading performance.
- Two traders using the same base strategy can have different results because one filters out losing trades and the other does not.
- Backtesting provides objective data that contradicts initial assumptions.
- If you have not built the strategy yourself, you will lack the discipline to continue trading during drawdown periods.
- Your column library is a reusable set of indicators that improves with each strategy you develop.
- Your highest-performing strategy has likely not been discovered yet; your process determines whether you identify it.

## Security & Safety Notes

- Never share proprietary backtest CSV files or column libraries publicly; they represent accumulated work and trading advantage.
- Be cautious about who you collaborate with; share ideas in trusted relationships rather than open forums.
- Do not include real account numbers, broker credentials, or live API keys in any backtesting tools or spreadsheets.
- When testing new strategies, always use historical data and a demo or paper trading environment before deploying real capital.

## Common Pitfalls

- **Problem:** You get a profitable backtest on the first try and start trading it live immediately.
  **Solution:** Always cast a wide net first. A profitable first backtest with fewer than 200 trades is overfitted. Widen your thresholds, add columns, and confirm the rule holds across at least 200 trades before risking capital.

- **Problem:** You keep tweaking parameters after each backtest in a guess-and-check loop.
  **Solution:** Define your process upfront and stick to it. Use an optimization tool to find optimal values in one step rather than iterating manually.

- **Problem:** You add more than 5 rules to filter trades and end up curve fitting.
  **Solution:** Let the optimizer select the highest-ranked rules. Fewer than 5 high-ranked rules produce strategies with lower drawdown than more than 5 low-ranked rules.

- **Problem:** You take partial profits for psychological comfort and watch your equity curve suffer.
  **Solution:** Run a side-by-side backtest with and without partial profits. Let the data show you the return reduction from taking partial profits.

- **Problem:** You abandon a strategy during a drawdown because you do not understand how it was built.
  **Solution:** Only trade strategies you built or fully rebuilt from original data. If you inherited it, rebuild it from scratch so you have the discipline to continue trading through expected drawdowns.

- **Problem:** You believe a strategy is "dead" because nobody talks about it anymore.
  **Solution:** Strategies remain viable when traders continue applying the filters that remove losing trades. Revisit old ideas with a fresh column library and optimization process.
