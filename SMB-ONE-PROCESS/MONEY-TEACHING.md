# SMB ONE-PROCESS

## Overview

This money teaching distills the systematic trading process shared by Dave Mabe with SMB Capital on the Trading Floor podcast. The core message is that a trading strategy fails not because the initial signal is weak, but because the trader lacks a rigorous process for developing, optimizing, and refining that strategy through backtesting. By building a personal column library, casting a wide net with initial backtests, using optimization tools to identify high-impact rules, reviewing trades daily, and collaborating with diverse traders, you can systematically turn any strategy idea into a profitable, robust system that you own completely.

## When to Follow These Money Teachings

- When you are building or refining a trading strategy and want to move beyond guess-and-check backtesting
- When your backtests are not producing the number of trades or profitability you expect
- When you are unsure how to use optimization without overfitting
- When you want to build a reusable set of indicators (columns) that improves every strategy over time
- When you are reviewing trades and noticing patterns you cannot explain or strategies that consistently underperform
- When you need to decide on stop placement, profit targets, or trade filtering rules
- When you want to collaborate with other traders to generate new strategy ideas

## Steps

### Step 1: Take Full Ownership of Your Strategy

Do not rely on someone else's strategy or secret sauce. You must build or deeply adapt your own system so that you understand why it works, what its weaknesses are, and how to fix it when drawdowns occur. If you cannot explain the edge in your own words, you will abandon it at the first sign of trouble.

### Step 2: Cast a Wide Net With Your First Backtest

Do not optimize for the final answer on the first attempt. Set thresholds much lower than your intuition suggests. For example, if you think a gap strategy requires a 5% gap, backtest with 3% to capture many more trades. This gives the optimization tool a rich dataset to find the true optimal threshold and reveals profitable subsets you would have missed.

### Step 3: Build and Maintain a Column Library

Create a shared library of indicators (columns) that you include in every backtest. Start with a brainstormed set and add to it over time. Examples include ATR, relative volume, position in range, yesterday's range, distance from open in ATR units, and custom measures you invent. The larger and more diverse your column library, the more likely optimization will uncover predictive power and the easier it becomes to develop new strategies.

### Step 4: Use an Optimization Tool to Identify High-Impact Rules

Run your backtest through a tool like the Strategy Cruncher (or build your own) that ranks columns by their predictive importance and shows the optimal cutoff for each. Apply only the most powerful rules to keep the strategy simple and robust. Do not fear specific optimal values such as 3.8% for a gap threshold; the market does not care about round numbers, and the optimal value is simply the best fit for your data.

### Step 5: Determine Optimal Stops

Run an initial backtest with no stop and no target, only a time stop. Use the resulting trade data to calculate MF (maximum favorable excursion) and MAE (maximum adverse excursion) for every trade. This reveals the optimal stop placement without curve fitting. Then run the backtest again with that optimal stop in place to create your realistic trade set for optimization.

### Step 6: Decide on Profit Targets Carefully

Avoid the common trap of taking partial profits and moving your stop to break even. Backtesting shows that holding full size to a target or to the close of the day produces a higher equity curve. Partial profits provide psychological comfort but cost significant money over time. Letting winners run is where the majority of profit comes from. Test both approaches on your own data to see the real tradeoff.

### Step 7: Review Every Trade Daily

At the end of each day, examine every trade your strategy took and every trade it skipped. Ask why the model took or skipped each one. Look for situations where your intuition says the model should have acted but did not. These gaps often reveal missing columns or weak rules that can be added to your library.

### Step 8: Seek Out the Unusual

Place yourself in a position to notice unusual market activity every day. Maintain a running list of observations, anomalies, and "almost met criteria" trades. Many strategy ideas come from near-misses or trades that were filtered out by an arbitrary threshold. The edge often sits just beyond your current rules.

### Step 9: Run Thought Experiments to Create Inverse Strategies

If your primary strategy is long, deliberately design a strategy that does the opposite in the same universe. Ask: what would the worst short trades look like, and could I go long those instead? This reverse-engineering process often uncovers completely independent, additive strategies based on the same raw idea, doubling your output without doubling your work.

### Step 10: Avoid the Guess-and-Check Loop

Most traders create a backtest, see poor results, make a small "vibes"-based adjustment, and run again. This never ends with a truly profitable strategy. Instead, commit to a process: wide-net backtest, column library, optimization tool, single-rule application, chart review, and iteration. The process is the edge.

### Step 11: Collaborate With Traders Who Do Things Differently

Seek out traders with completely different approaches, styles, and specialties. Share openly and ask how they think about the market. Their mental models will generate ideas you would never reach alone. Building trust and being a "giver not a taker" is the foundation of these relationships. Network is a trading skill.

## Examples

### Example 1: Gap Strategy Optimization

Dave Mabe's first strategy looked for stocks gapping above a threshold with a tight range in the first 30 minutes, then going long on a breakout. Initially he assumed 5% was the right gap threshold. After casting a wider net with 3%, the optimization tool revealed many more profitable trades between 3% and 5%. He ended up with five times the number of trades by letting the tool find the true optimal cutoff rather than imposing his assumption upfront.

### Example 2: Inverse Gap Strategy

While trading the gap strategy long, Mabe noticed that some of the gapping stocks would gap up, break out, then immediately tank and stop him out. Instead of just accepting these as bad trades, he created a completely separate strategy that went short on the same conditions. Because it was isolated with its own rules and universe filters, he could run both long and short strategies without conflicting positions. The losing longs became the basis for a profitable short strategy.

### Example 3: Position in Range Filter

In a gap strategy, a trade that triggers when price is near the top of today's range is intuitively better for a long than a trade near the bottom. By adding a "position in range" column (0 = near low, 100 = near high) to the column library and running it through the optimizer, the tool confirmed that only trades above a certain percentile should be taken. This single rule eliminated a large portion of bad trades and made the strategy far more robust.

### Example 4: Adam Grimes and the One R Profit Target

Adam Grimes intuitively believed in holding for big winners. When someone suggested he try a one R profit target (selling as soon as the trade made as much as he was risking), he resisted. Backtesting showed the one R target produced a significantly higher equity curve. Grimes adopted it against his intuition, demonstrating that backtesting can override flawed intuition when the process is trusted.

### Example 5: Daily Review of Skipped Trades

Garrett and Tim at SMB review trades their model did not take. If they see a stock like Tesla that met the spirit of the strategy but was excluded by a rule, they investigate why. This often leads to brainstorming modifications or new columns that can capture that edge, turning near-misses into strategy improvements or entirely new strategies.

## Best Practices

- ✅ Start every first backtest with a much lower threshold than your intuition to cast a wide net
- ✅ Build a column library once and reuse it across every strategy
- ✅ Use an optimization tool rather than manual guess-and-check
- ✅ Run your first backtest with no stop and no target to let MF/MAE reveal optimal exits
- ✅ Apply only the most powerful rules to keep strategies simple and robust
- ✅ Review every trade and skipped trade daily
- ✅ Maintain a running list of unusual observations and near-miss trades
- ✅ Design inverse or complementary strategies to capture ignored edges
- ✅ Share openly with traders who have completely different approaches
- ✅ Test controversial ideas like one R targets or no targets on your own data before rejecting them
- ❌ Do not manually tweak thresholds between backtests based on vibes
- ❌ Do not fear curve fitting to the point of inaction; start with many trades and let tools select significance
- ❌ Do not take partial profits and move stops to break even without testing the math
- ❌ Do not abandon a strategy at the first drawdown if you did not build and understand it yourself
- ❌ Do not hoard ideas; the more you share, the more you get back

## Keep In Mind

- The signal itself is almost the least important part of a strategy; the optimization process is what separates good traders from bad.
- Two traders using the same base strategy can have wildly different results solely because one skips the bad trades and the other does not.
- Backtesting is a superpower that can prove your intuition flat out wrong.
- If you have not built the strategy yourself, you will not have the confidence to trade through drawdowns.
- Your column library is the most valuable asset you will ever build; it compounds over time.
- The best strategy of your career has probably not been thought of yet; your process determines whether you discover it.

## Security & Safety Notes

- Never share proprietary backtest CSV files or column libraries publicly; they represent years of work and real trading edge.
- Be cautious about who you collaborate with; share ideas in trusted relationships rather than open forums.
- Do not include real account numbers, broker credentials, or live API keys in any backtesting tools or spreadsheets.
- When testing new strategies, always use historical data and a demo or paper trading environment before deploying real capital.

## Common Pitfalls

- **Problem:** You get a profitable backtest on the first try and start trading it live immediately.
  **Solution:** Always cast a wide net first. A profitable first backtest is usually overfitted or too narrow. Widen your thresholds, add columns, and confirm the edge holds across many trades before risking capital.

- **Problem:** You keep tweaking parameters after each backtest in a guess-and-check loop.
  **Solution:** Define your process upfront and stick to it. Use an optimization tool to find optimal values in one step rather than iterating manually.

- **Problem:** You add too many rules to eliminate every losing trade and end up curve fitting.
  **Solution:** Let the optimizer select only the most powerful rules. Fewer, stronger rules produce more robust strategies than many weak rules.

- **Problem:** You take partial profits for psychological comfort and watch your equity curve suffer.
  **Solution:** Run a side-by-side backtest with and without partial profits. Let the data show you the real cost of "playing with house money."

- **Problem:** You abandon a strategy during a drawdown because you do not understand how it was built.
  **Solution:** Only trade strategies you built or fully own. If you inherited it, rebuild it from scratch so you have the confidence to endure normal variance.

- **Problem:** You believe a strategy is "dead" because nobody talks about it anymore.
  **Solution:** Strategies never die; traders just forget how to skip the bad trades. Revisit old ideas with a fresh column library and optimization process.
