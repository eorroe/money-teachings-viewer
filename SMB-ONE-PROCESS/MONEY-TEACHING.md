# SMB ONE-PROCESS

## Overview

This money teaching distills the systematic trading process shared by Dave Mabe with SMB Capital on the Trading Floor podcast. The core message is that a trading strategy fails not because the initial signal is weak, but because the trader lacks a defined process for developing, optimizing, and refining that strategy through backtesting. By building a personal column library, testing a wider range of threshold values with initial backtests (for example, testing a 3 percent gap threshold when you assume 5 percent is optimal), using optimization tools to identify rules, reviewing trades daily, and collaborating with other traders, you can systematically turn strategy ideas grounded in observable price and volume patterns into a strategy that produces positive returns over the backtest period that you can clearly explain using backtest data and the logic from your own backtest.

## When to Follow These Money Teachings

- When you are building or refining a trading strategy and want to move beyond guess-and-check backtesting
- When your backtests do not produce the trade count or return that meets defined performance criteria
- When you are unsure how to use optimization without overfitting
- When you want to build a reusable set of indicators (columns) that improves every strategy over time
- When you are reviewing trades and noticing patterns you cannot explain or strategies that underperform across multiple backtest periods
- When you need to decide on stop placement, profit targets, or trade filtering rules
- When you want to collaborate with other traders to generate new strategy ideas

## Steps

### Step 1: Take Full Ownership of Your Strategy

Do not rely on someone else's strategy or unshared logic. You must build or deeply adapt your own system so that you understand why it works, what its documented weaknesses are based on backtest results, and how to adjust it when drawdowns occur within historical ranges. If you cannot explain why the strategy works, you will abandon the strategy when the strategy enters drawdown.

### Step 2: Test a Broader Range With Your Initial Backtest

Do not optimize for the final answer on the initial attempt. Set thresholds lower than your initial assumption. For example, if you think a gap strategy requires a 5 percent gap, backtest with 3 percent to capture additional trades. This gives the optimization tool additional data points to identify the threshold that produces the highest returns for your dataset.

### Step 3: Build and Maintain a Column Library

Create a shared library of indicators (columns) that you include in every backtest. Start with a brainstormed set and add to it over time. Examples include ATR (average true range), relative volume, position in range, yesterday's range, distance from open in ATR units, and custom measures you invent. A column library with at least 250 indicators (Dave Mabe reports using approximately 250–300) can increase the probability that optimization will find rules that meet a performance threshold.

### Step 4: Use an Optimization Tool to Identify Rules

Run your backtest through a tool such as the Strategy Cruncher that ranks columns by their importance and shows the optimal cutoff for each. Apply only the rules identified by the optimization tool to keep the strategy simple. Do not fear specific optimal values such as 3.8% for a gap threshold; threshold values do not need to be round numbers.

### Step 5: Determine Optimal Stops

Run an initial backtest with no stop and no target, only a time-based exit rule that exits the trade after a holding period defined by the strategy's timeframe. Use the resulting trade data to calculate MF (maximum favorable excursion) and MAE (maximum adverse excursion) for every trade. MF and MAE analysis identifies stop levels based on actual trade excursion data. Then run the backtest again with that stop level identified through MF/MAE analysis in place to create your trade set for optimization.

### Step 6: Decide on Profit Targets Carefully

Avoid taking partial profits (selling a portion of the position before the target) and moving your stop to break even. Dave Mabe's backtesting shows that holding your entire position to a target or to the close of the day can produce higher total returns than strategies using partial profits. In Dave Mabe's testing, taking partial profits reduced total returns. Letting winners run to target is where most of your returns come from. Test both approaches on your own data to see the specific tradeoff.

### Step 7: Review Every Trade Daily

At the end of each day, examine every trade the strategy took and every trade the strategy skipped. Ask why the model took or skipped each trade. Look for situations where the model skipped a trade that the strategy rules suggest should have been taken. Reviewing skipped trades reveals gaps in the column library or rules that need adjustment.

### Step 8: Seek Out the Unusual

Place yourself in a position to notice market activity that deviates from your strategy's typical entry parameters every day. Maintain a list stored in a dedicated journal or document of market observations, unusual price or volume activity, and near-miss trades. Strategy ideas come from near-miss trades. Reviewing near-miss trades reveals new strategy rules outside your current filters.

### Step 9: Run Thought Experiments to Create Inverse Strategies

If your primary strategy is long, deliberately design a strategy that takes the opposite position (e.g., short if primary is long) with the same universe filters and position sizing. Ask: what criteria define the trades that stopped out in the short strategy, and could I create a long strategy from those same criteria? This design process uncovers independent strategies with separate rule sets, universes, and no overlapping positions based on the same raw idea, creating additional strategies from a single concept.

### Step 10: Avoid the Guess-and-Check Loop

Traders who skip the process create a backtest, see results that fall below defined performance thresholds, make an unspecified adjustment without justification supported by backtest data, and run again. This cycle does not produce a strategy profitable across multiple market conditions and time periods. Instead, commit to a process: broader-range backtest, column library, optimization tool, single-rule application, chart review, and iteration. A defined process produces higher returns than ad-hoc adjustments.

### Step 11: Collaborate With Traders Who Do Things Differently

Seek out traders with different strategy types (e.g., day trading versus swing trading), different timeframes (e.g., intraday, daily, weekly), and different market focuses (e.g., equities, futures, forex). Share openly and ask how they think about the market. Their perspectives generate strategy ideas you would not develop alone. Building trust and approaching collaborations by sharing ideas and asking how you can help others is the core of these relationships. Building a network of traders supports strategy development.

## Examples

### Example 1: Gap Strategy Optimization

Dave Mabe's first strategy looked for stocks gapping above a threshold with a tight range in the first 30 minutes, then going long on a breakout. Initially he assumed 5% was the right gap threshold. After testing a broader range with 3%, the optimization tool revealed additional profitable trades between 3% and 5%. He increased his trade count by letting the tool find the threshold that produced the highest returns rather than imposing his assumption upfront.

### Example 2: Inverse Gap Strategy

While trading the gap strategy long, Mabe noticed that some of the gapping stocks would gap up, break out, then immediately tank and stop him out. Instead of just accepting these losing trades, he created a completely separate strategy that went short on the same conditions. Because it was isolated with its own rules and universe filters, he could run both long and short strategies without conflicting positions. The losing longs became the basis for a profitable short strategy.

### Example 3: Position in Range Filter

In a gap strategy, a trade that triggers when price is in the upper portion of today's range produces higher returns for a long position than a trade near the bottom. By adding a "position in range" column (0 = near low, 100 = near high) to the column library and running it through the optimizer, the tool confirmed that only trades above the 70th percentile should be taken. This single rule eliminated 30 percent of losing trades.

### Example 4: Adam Grimes and the One R Profit Target

Adam Grimes believed that holding for gains of at least one risk unit (the amount you are risking on a single trade) produced higher returns. When someone suggested he try a one risk unit profit target (selling as soon as the trade made as much as he was risking), he resisted. Backtesting showed the one risk unit target produced a higher total return on the backtested dataset compared to the prior approach. Grimes adopted it contrary to his prior belief, demonstrating that backtesting can challenge initial assumptions when the process is trusted.

### Example 5: Daily Review of Skipped Trades

Garrett and Tim at SMB review trades their model did not take. If they see a stock like Tesla that matched the strategy criteria except for one filter, they investigate why. Reviewing skipped trades leads directly to brainstorming modifications or new columns that can capture that edge, turning near-misses into strategy improvements or entirely new strategies.

## Best Practices

- ✅ Start every initial backtest with a threshold 2 percentage points lower than your initial assumption to test a wider range
- ✅ Build a column library once and reuse it across all strategies you develop
- ✅ Use an optimization tool rather than manual guess-and-check
- ✅ Run your first backtest for a strategy with no stop and no target, then use MF and MAE analysis to identify exit levels
- ✅ Apply only rules identified by the optimization tool to keep strategies simple
- ✅ Review every trade and skipped trade daily
- ✅ Maintain a list in a dedicated journal or document of unusual observations and near-miss trades
- ✅ Design inverse or complementary strategies to capture ignored edges
- ✅ Share openly with traders who have different strategy types and market focuses
- ✅ Test controversial ideas like one risk unit targets or no targets on your own data before rejecting them
- ❌ Do not manually tweak thresholds between backtests without justification supported by backtest data
- ❌ Do not fear curve fitting to the point of inaction; start with a minimum of 100 trades and let tools identify rules that meet a performance threshold
- ❌ Do not take partial profits (selling a portion of the position before the target) and move stops to break even without running backtests to compare outcomes
- ❌ Do not abandon a strategy during a drawdown within your predefined drawdown tolerance if you did not build and understand it yourself
- ❌ Do not hoard ideas; sharing strategy concepts generates reciprocal collaboration

## Keep In Mind

- The optimization process is the primary driver of returns because it determines which trades from a signal are taken; the signal provides the opportunity set, but optimization selects the profitable subset.
- Two traders using the same base strategy can have different returns because one filters out losing trades and the other does not.
- Backtesting provides objective data that can challenge initial assumptions.
- If you have not built the strategy yourself, you may lack the discipline to continue trading during drawdown periods.
- Your column library is a reusable set of indicators that becomes more effective at filtering losing trades as you develop more strategies.
- The strategy that produces the highest total returns in your backtests has not been identified yet through your current process; your process determines whether you identify it.

## Security & Safety Notes

- Never share backtest CSV files or column libraries containing strategy rules you developed independently and have not published publicly.
- Be cautious about who you collaborate with; share ideas only with traders you know personally and have collaborated with previously rather than in open forums where you have no relationship history.
- Do not include real account numbers, broker credentials, or live API keys in any backtesting tools or spreadsheets.
- When testing new strategies, always use historical data and a demo or paper trading environment before deploying real capital.

## Common Pitfalls

- **Problem:** You get a profitable backtest on the first try and start live trading immediately.
  **Solution:** Always test a broader range first. An initial backtest that meets your performance criteria with fewer than 100 trades is overfitted to the historical dataset. Widen your thresholds, add columns, and confirm the rule holds across a sufficient number of trades before risking capital.

- **Problem:** You keep tweaking parameters after each backtest in a guess-and-check loop.
  **Solution:** Define your process upfront and stick to it. Use an optimization tool to find optimal values in one step rather than iterating manually.

-   **Problem:** You add several rules to filter trades and end up curve fitting.
  **Solution:** Let the optimizer identify the rules. One to three rules produce more robust strategies than adding multiple rules.

- **Problem:** You take partial profits for psychological comfort and watch your equity curve suffer.
  **Solution:** Run a side-by-side backtest with and without partial profits (selling a portion of the position before the target). Let the data show you the return reduction from taking partial profits.

- **Problem:** You abandon a strategy during a drawdown because you do not understand how it was built.
  **Solution:** Only trade strategies you built or fully rebuilt from raw price and volume data. If you inherited a strategy, rebuild it from scratch from the original raw data so you have the discipline to continue trading through drawdowns.

-   **Problem:** You believe a strategy is "dead" because traders no longer discuss it.
  **Solution:** Strategies can still produce profits when traders continue applying the filters that remove losing trades. Revisit old ideas with a fresh column library and optimization process.
