# SMB - The Trading Floor: SMB Capital Podcast (Ep 1)

How to Identify, Execute, and Manage a High-Conviction Breakout Trade Using Fundamental Catalysts and Technical Setups

## Overview

This Money Teaching walks through SMB Capital's step-by-step approach to identifying, executing, and managing a breakout trade with multiple aligned tailwinds, using the Ethereum 4K breakout from early August as a real-world case study. It covers how to build a checklist of tailwinds, evaluate technical bases, enter positions using TWAP algorithms, and manage exits without letting emotion drive decisions. The goal of this teaching document is to help traders replicate the disciplined process the SMB desk uses when a fundamental catalyst coincides with a strong technical pattern in a trade setup.

## When to Follow These Money Teachings

- When you notice a long-term technical base (a multi-month or multi-year sideways price pattern on the weekly or monthly chart) combined with a tightening daily consolidation (where daily price movement narrows)
- When a fundamental catalyst (a news or event-driven factor that can shift market sentiment) emerges that could accelerate a breakout
- When extreme short positioning (short interest above the 90th percentile of historical levels) exists in an asset, creating the potential for a short squeeze (where short sellers are forced to buy back shares to cover their positions, driving the price higher)
- When Bitcoin is at all-time highs and risk assets (stocks, commodities, and other investments that gain value in a strong economy) are performing well across the market
- When you are deciding whether to hold a position into the weekend after a confirmed close above the breakout level
- When the price chart (the "tape") fails to provide a high intraday volume surge (a sharp, above-average spike in trading volume during the trading day) confirming institutional participation and you must accumulate size algorithmically

## Steps

### Step 1: Build a Tailwind Checklist

Before entering any breakout trade, write down all relevant factors working in your favor. This checklist should include:
- Long-term negative sentiment that has begun to reverse, measured by a shift in social media, news, or analyst tone (e.g., Ethereum subject to widespread negative sentiment for years, then a catalyst reverses sentiment)
- Short positioning above the 90th percentile of historical levels measured over the prior two years, creating conditions where short sellers may be forced to buy back shares to cover
- A multi-year base (at least two years of sideways price action) without prior swing highs within 5% of the current level on the weekly or monthly chart
- A tight one-month compression (daily price movement narrowing within a one-month window) on the daily chart
- Treasury or institutional accumulation announced within the prior 60 days (e.g., at least three Ethereum treasury firms emerging)
- Stablecoin adoption growth measured by stablecoin transaction fee share on Ethereum (stablecoins account for up to 40% of all blockchain transaction fees, and Ethereum hosts half of them)
- A macro environment where the S&P 500 is above its 50-day moving average
- Bitcoin trading at all-time highs

Only consider entering when at least 3 of the 8 listed tailwinds are aligned, not just one or two.

### Step 2: Identify the Technical Breakout Level

Find the exact price level that, if broken, would confirm the breakout. In this case, the level was 4K on the ETHA ETF (Ethereum's exchange-traded fund). Confirm that:
- The level is a swing high within the prior 24 months
- The chart has been consolidating below it for at least one month
- The base is a prolonged sideways consolidation
- You are watching for a daily close above the level, not just an intraday spike

Do not assume the breakout will happen. Wait for a daily close above the breakout level before entering your full planned position size.

### Step 3: Enter Using the Right Strategy for the Day

On the day before the confirmed close, when the asset gaps up within 2% of the prior day's range high but has not yet closed above:
- Do not deploy the full planned position size because the breakout is not confirmed
- Use a TWAP (Time-Weighted Average Price) algorithm — a tool that divides a large order into smaller equal-sized orders sent at regular intervals — to build an initial position throughout the day as long as price holds above the breakout level
- If the TWAP script is programmed to halt buying when price closes below the breakout level for the session, it will stop accumulating if price breaks back down
- Place bids at pre-identified pullback support levels (prior swing lows or technical support zones) to accumulate additional size

On the day of the confirmed close, once the asset closes above the breakout level:
- You can manually add to the position at the session close
- Decide your total position size by the close: stock plus call options if the setup warrants a leveraged upside bet
- Hold the position overnight into the weekend only if the close was in the top 20% of the day's trading range

### Step 4: Manage the Trade Through the Weekend

If the close above the breakout level was in the top 20% of the day's range and you are holding overnight into the weekend:
- Do not sell immediately just because the gap is large. Debate with your trading partners whether this is an intraday or single-session trade to exit quickly or a multi-day swing trade to hold
- If the fundamental backdrop includes the tailwinds listed in Step 1, hold the stock position and consider selling (closing) the call options position to capture implied volatility (IV) expansion
- Move your stop-loss order to below the prior day's low (the lowest price of the session before the breakout confirmed) or below the prior bar low (the lowest price of the most recently completed daily bar) once the breakout is confirmed
- If trading a cryptocurrency directly, remember the asset trades overnight; expect sideways movement over the weekend and do not panic if it drifts

### Step 5: Let the Trade Work or Exit on a Clear Signal

Once you have entered a multi-day swing position with aligned tailwinds:
- Do not sell every day just because the stock is up. If there is no technical reason to sell — no break below the prior bar low (the low of the most recently completed daily price bar), no volume climax (an extreme spike in trading volume that signals buying or selling exhaustion), no breakdown of the technical setup — hold
- Use a trailing stop-loss order based on the prior bar low, not a price target set without technical justification
- If the prior bar low breaks, exit immediately. Do not reverse the exit decision after the plan is broken
- Selling on a rally is fine if it is part of the pre-defined plan, but selling because the position moves against you by more than your pre-defined loss threshold or because the position exceeds your pre-defined profit targets before your technical exit trigger (a break below the prior bar low) activates is a mistake

### Step 6: Review and Update Your Playbook

After the trade is closed:
- If trading with a team, hold a review discussing what worked, where execution deviated from the plan, and what specific signals or decisions were missed
- Split your playbook into sub-playbooks (separate trading plans): trades to hold for a swing, trades to exit quickly on momentum, and trades to size at the 90th percentile of your typical position size (the upper end of your normal position sizing range)
- Use the debate process to create clearer decision criteria with defined numerical or price-based triggers for the next time you face a similar situation
- Document the exact sequence of price levels, news events, and decisions so the next trade does not require the same debate

## Examples

### Example 1: Ethereum 4K Breakout (SMB Capital, the first week of August 2025)

The SMB desk identified Ethereum (traded via ETHA ETF) as a candidate in early June when data from Glassnode and Coinglass on high short positioning surfaced. The thesis intensified on June 28 when Tom Lee was appointed chairman of BMnR (the firm building an Ethereum treasury under Tom Lee), and on June 30 when he announced a $250M private placement to build an Ethereum treasury. Additional catalysts followed: Peter Thiel took a stake in BMnR (July 15), Cathie Wood announced a stake (July 22), and Tom Lee held an investor presentation discussing the "alchemy of 5%" strategy (Bitmain's plan to accumulate 5% of the total supply of Ethereum as part of the treasury plan). Ethereum treasuries collectively acquired approximately $17B worth of ether by mid-August 2025.

On the technical side, Ethereum had built a four-year base on the monthly chart and was consolidating tightly below the 4K level in the first week of July. The desk noted the ETH/BTC ratio turning by July 15, confirming Ethereum was the asset to play. When ETHA closed above 4K on Friday, the desk entered using TWAP on Thursday and added stock at close on Friday, also buying 2-week-out calls. They held into the weekend because the fundamental and technical tailwinds warranted holding the position beyond a single day. Ethereum rallied for four more days, almost reaching 5K, before the prior bar low broke and they exited.

### Example 2: The Expected Volume Surge That Never Came

During the ETHA breakout on Thursday and Friday, the traders expected a high intraday volume surge — a "see-it moment" where the tape would confirm institutional participation. It never fully arrived. The volume was relative volume (RVOL, the ratio of current volume to the average volume over a lookback period) at 1.5x the 20-day average but not at the levels seen on the June 28 and June 30 breakout days. Instead of waiting until the price breaks below the consolidation low, they used a TWAP script to accumulate size over time as long as price held up. This allowed them to get filled without chasing and without requiring a single significant volume spike to justify the position.

## Best Practices

- ✅ Write out a full tailwind checklist before entering a high-conviction trade. When at least 5 of the 8 checklist tailwinds are present, increase (scale up) position size in proportion to the number of aligned tailwinds — for example, use a larger position when 7 or 8 tailwinds are present than when 5 are present.
- ✅ Use a TWAP (Time-Weighted Average Price) algorithm — a tool that splits a large order into smaller orders sent at regular intervals — when the setup is well-defined but the high intraday volume surge confirming institutional participation is absent. Accumulate while price remains above the breakout level and volume is above the 20-day average volume.
- ✅ Wait for a daily close above the breakout level before adding to your position. Intraday spikes above resistance are not enough.
- ✅ Hold overnight into the weekend only if the daily close was in the top 20% of that day's trading range (i.e., the closing price was in the highest 20% of prices traded during the session). A close below the midpoint of the day's range is a reason to reduce position size, not hold.
- ✅ Debate trade management openly within the team. Different views are a strength, not a weakness.
- ✅ Review every trade afterward and split your playbook into sub-categories so the next debate is faster on recurring setups and more clearly informed.
- ❌ Do not lever up before the breakout is confirmed. A gap up near resistance can fail.
- ❌ Do not sell every day just because the trade is up. If your trading plan says hold, hold until the plan breaks.
- ❌ Do not second-guess the stop after it is hit. A break of the prior bar low is an exit, not a reason to wait for a recovery.
- ❌ Do not ignore crypto's 24/7 nature. Crypto assets often trade sideways over the weekend; do not panic if price drifts.
- ❌ Do not add shares or contracts to a losing position (increase your position size after the price has moved against you) in hopes of averaging down your entry price.

## Keep In Mind

- A failed breakdown that reclaims and then gaps up and holds at the top of the range is a strong bullish pattern. In this trade, Ethereum had a failed breakdown six days before the confirmed breakout above 4K, then reclaimed and gapped up.
- Bitcoin can break out to all-time highs while Ethereum consolidates sideways for years (as Ethereum did for approximately four years prior to this trade). The relative strength turn in the ETH/BTC ratio is a signal that Ethereum is the asset to own, not Bitcoin.
- Stablecoin adoption is a fundamental driver for Ethereum because approximately half of all stablecoins are built on the Ethereum blockchain. Growth in stablecoin usage increases Ethereum transaction fees and network value.
- The "big pink line" (the breakout level) should be drawn as a distinct horizontal line on the chart and respected. Do not buy aggressively above it until the daily close confirms the break.
- Team debate is common because traders see risk differently. The goal is to reach an equilibrium point (a mutually agreed-upon trade decision that balances competing views), not to force unanimity.

## Security & Safety Notes

- This teaching is for educational purposes only. It documents a real trade but does not constitute financial advice.
- Trading leveraged instruments such as options carries the risk of losing the entire premium. Only risk capital that traders can afford to lose.
- Cryptocurrency assets are volatile and can gap against you overnight, especially over weekends when traditional markets are closed.
- Always use a stop loss and never add to a losing position in hopes of averaging down.
- TWAP and algorithmic execution tools require testing and calibration. Do not deploy custom scripts with real capital without understanding their behavior in adverse conditions.

## Common Pitfalls

- **Problem:** Buying the high after a sharp ramp into resistance without confirmation.
  **Solution:** Wait for a daily close above the breakout level or a TWAP (Time-Weighted Average Price) script that accumulates only while price holds above the level. Do not chase a moving price.
- **Problem:** Selling too early into strength because the gap exceeds your planned exit threshold.
  **Solution:** If the fundamental backdrop includes aligned tailwinds from Step 1, hold the stock position and take profits via short-dated call options (options expiring within approximately one to two weeks) instead of selling the stock position outright.
- **Problem:** Raising the stop-loss order before the breakout level is confirmed, after the opening drive.
  **Solution:** Keep the stop-loss order wide until the daily close above the level is confirmed. Only then tighten it to the prior day's low (the low of the session before the confirmed close) or the breakout level itself.
- **Problem:** Failing to exit when the plan breaks because you are focused on the highest profit you could have captured.
  **Solution:** The goal is not to sell the high. The goal is to follow the process. If the prior bar low (the low of the most recently completed daily price bar) breaks, exit. Do not rationalize staying in.
- **Problem:** Treating every breakout as the same regardless of backdrop.
  **Solution:** Split your playbook. Momentum-only breakouts (breakouts without aligned fundamental tailwinds) are trades to exit quickly. Breakouts with aligned tailwinds from Step 1 are a one-to-four-week swing trade to hold because the tailwinds justify a larger price move.
