# SMB - The Trading Floor: SMB Capital Podcast (Ep 1)

How to Identify, Execute, and Manage a High-Conviction Breakout Trade Using Fundamental Catalysts and Technical Setups

## Overview

This Money Teaching walks through SMB Capital's step-by-step approach to identifying, executing, and managing a breakout trade with multiple aligned catalysts, using the Ethereum 4K breakout from early August as a real-world case study. It covers how to build a checklist of tailwinds, evaluate technical bases, enter positions using TWAP algorithms, and manage exits without letting emotion drive decisions. The goal is to help traders replicate the disciplined process the SMB desk uses when a setup where a fundamental catalyst coincides with a strong technical pattern appears.

## When to Follow These Money Teachings

- When you notice a long-term technical base combined with a tightening daily consolidation
- When a fundamental catalyst emerges that could shift sentiment and accelerate a breakout
- When extreme short positioning exists in an asset, creating the potential for a short squeeze
- When Bitcoin is at all-time highs and risk assets are performing well across the market
- When you are deciding whether to hold a position into the weekend after a confirmed close above a key level
- When the tape fails to provide the high intraday volume surge confirming institutional participation and you must accumulate size algorithmically

## Steps

### Step 1: Build a Tailwind Checklist

Before entering any breakout trade, write down all relevant factors working in your favor. This should include:
- Long-term negative sentiment that has begun to reverse (e.g., Ethereum subject to widespread negative sentiment for years, then a catalyst reverses sentiment)
- Short positioning above the 90th percentile of historical levels that could be forced to cover
- A multi-year base without prior swing highs within 5% of the current level on the weekly or monthly chart
- A tight one-month compression on the daily chart
- Treasury or institutional accumulation announced within the prior 60 days (e.g., at least three Ethereum treasury firms emerging)
- Stablecoin adoption growth (stablecoins account for up to 40% of all blockchain transaction fees, and Ethereum hosts half of them)
- A macro environment where the S&P 500 is above its 50-day moving average
- Bitcoin trading at all-time highs

Only consider entering when more than one tailwind is aligned, not just one.

### Step 2: Identify the Technical Breakout Level

Find the exact price level that, if broken, would confirm the breakout. In this case, the level was 4K on the ETHA ETF. Confirm that:
- The level is a swing high within the prior 24 months
- The chart has been consolidating below it for at least one month
- The base is a prolonged sideways consolidation
- You are watching for a daily close above the level, not just an intraday spike

Do not assume the breakout will happen. Wait for a daily close above the breakout level before entering your planned position size.

### Step 3: Enter Using the Right Strategy for the Day

On the day before the confirmed close, when the asset gaps up within 2% of the range high but has not yet closed above:
- Do not lever up the full position yet because the breakout is not confirmed
- Use a TWAP (Time-Weighted Average Price) algorithm to build an initial position throughout the day as long as price holds above the level
- If the TWAP script is programmed to halt when price closes below the level, it will stop buying if price breaks back down
- Place bids at pullback levels to accumulate additional size

On the day of the confirmed close, once the asset closes above the breakout level:
- You can manually add to the position at close
- Decide your total position size by the close (stock + calls if the setup warrants a leveraged upside bet)
- Take the position overnight only if it closed in the upper half of the day's trading range

### Step 4: Manage the Trade Through the Weekend

If the close above the breakout level held in the top 20% of the day's range and you are holding overnight into the weekend:
- Do not sell immediately just because the gap is large. Debate with your trading partners whether this is an intraday or single-session trade to exit quickly or a 3-to-10 day swing trade to hold
- If the fundamental backdrop includes the tailwinds listed in Step 1, hold the stock and close the call position to capture implied volatility (IV) expansion
- Move your stop to below the prior day's low or the prior bar low once the breakout is confirmed
- If trading a cryptocurrency directly, remember the asset trades overnight; expect sideways movement over the weekend and do not panic if it drifts

### Step 5: Let the Trade Work or Exit on a Clear Signal

Once you have entered a multi-day swing position with aligned catalysts:
- Do not sell every day just because the stock is up. If there is no technical reason to sell (no break below the prior bar low, no volume climax, no breakdown), hold
- Use a trailing stop based on the prior bar low, not a price target set without technical justification
- If the prior bar low breaks, exit immediately. Do not reverse the exit decision after the plan is broken
- Selling on a rally is fine if it is part of the plan, but selling due to when the position moves against you by more than your predetermined threshold or when the position is up more than your plan targets before your technical exit triggers is a mistake

### Step 6: Review and Update Your Playbook

After the trade is closed:
- If trading with a team, hold a review discussing what worked, where execution deviated from the plan, and what specific signals or decisions you missed
- Split your playbook into sub-playbooks: trades to hold for a swing, trades to exit quickly on momentum, and trades to size at the 90th percentile of your typical position size
- Use the debate process to create clearer decision criteria with defined triggers for the next time you face a similar situation
- Document the exact sequence of events so the next trade does not require the same debate

## Examples

### Example 1: Ethereum 4K Breakout (SMB Capital, the first week of August 2025)

The SMB desk identified Ethereum (traded via ETHA ETF) as a candidate in around June 10 when data from Glassnode and Coinglass on high short positioning surfaced. The thesis intensified on June 28 when Tom Lee was appointed chairman of BMnR, and on June 30 when he announced a $250M private placement to build an Ethereum treasury. Additional catalysts followed: Peter Thiel took a stake in BMnR (July 15), Cathie Wood announced a stake (July 22), and Tom Lee held an investor presentation discussing the "alchemy of 5%" strategy. Ethereum treasuries collectively acquired ~$17B worth of ether by mid-August.

On the technical side, Ethereum had built a four-year base on the monthly chart and was consolidating tightly below the 4K level in the first week of July. The desk noted the ETH/BTC ratio turning by July 15, confirming Ethereum was the asset to play. When ETHA closed above 4K on Friday, the desk entered using TWAP on Thursday and added stock at close on Friday, also buying 2-week-out calls. They held into the weekend because the fundamental and technical tailwinds warranted holding the position beyond a single day. Ethereum rallied for four more days, almost reaching 5K, before the prior bar low broke and they exited.

### Example 2: The Expected Volume Surge That Never Came

During the ETHA breakout on Thursday and Friday, the traders expected a high intraday volume surge — a "see-it moment" where the tape would confirm institutional participation. It never fully arrived. The volume was RVOL 1.5x the 20-day average but not at the levels seen on the June 28 and June 30 breakout days. Instead of waiting until the price breaks below the consolidation low, they used a TWAP script to accumulate size over time as long as price held up. This allowed them to get filled without chasing and without requiring a single dramatic volume print to justify the position.

## Best Practices

- ✅ Write out a full tailwind checklist before entering a high-conviction trade. When at least 5 of 7 tailwinds are present, scale position size proportionally to the number of aligned tailwinds.
- ✅ Use a TWAP algorithm when the setup is well-defined but the high intraday volume surge confirming institutional participation is absent. Accumulate while price remains above the breakout level and volume is above the 20-day average.
- ✅ Wait for a daily close above the breakout level before adding to your position. Intraday spikes above resistance are not enough.
- ✅ Hold overnight only if the close held in the top quartile of the day's range. A close below the midpoint of the day's range is a reason to reduce size, not hold.
- ✅ Debate trade management openly within the team. Different views are a strength, not a weakness.
- ✅ Review every trade afterward and split your playbook into sub-categories so the next debate is 30% faster on recurring setups and more clearly informed.
- ❌ Do not lever up before the breakout is confirmed. A gap up near resistance can fail.
- ❌ Do not sell every day just because the trade is up. If your trading plan says hold, hold until the plan breaks.
- ❌ Do not second-guess the stop after it is hit. A break of the prior bar low is an exit, not a reason to wait for a recovery.
- ❌ Do not ignore crypto's 24/7 nature. Crypto assets often trade sideways over the weekend; do not panic if price drifts.

## Keep In Mind

- A failed breakdown that reclaims and then gaps up and holds at the top of the range is a strong bullish pattern. In this trade, Ethereum had a failed breakdown six days before the breakout, then reclaimed and gapped up.
- Bitcoin can break out to all-time highs while Ethereum consolidates for four years. The relative strength turn in ETH/BTC is a signal that Ethereum is the asset to own, not Bitcoin.
- Stablecoin adoption is a fundamental driver for Ethereum because over half of stablecoins are built on the Ethereum blockchain. Growth in stablecoin usage increases Ethereum transaction fees and network value.
- The "big pink line" (the breakout level) should be drawn with a distinct line and respected. Do not buy aggressively above it until the close confirms the break.
- Team debate is common because many traders see risk differently. The goal is to reach an equilibrium point, not to force unanimity.

## Security & Safety Notes

- This teaching is for educational purposes only. It documents a real trade but does not constitute financial advice.
- Trading leveraged instruments such as options carries the risk of losing the entire premium. Only risk capital traders can afford to lose.
- Cryptocurrency assets are volatile and can gap against you overnight, especially over weekends when traditional markets are closed.
- Always use a stop loss and never add to a losing position in hopes of averaging down.
- TWAP and algorithmic execution tools require testing and calibration. Do not deploy custom scripts with real capital without understanding their behavior in adverse conditions.

## Common Pitfalls

- **Problem:** Buying the high after a sharp ramp into resistance without confirmation.
  **Solution:** Wait for a close above the breakout level or a TWAP that accumulates only while price holds. Do not chase.
- **Problem:** Selling too early into strength because the gap exceeds your planned exit threshold.
  **Solution:** If the fundamental backdrop includes at least three aligned catalysts from Step 1, hold the stock and take profits via short-dated calls instead of selling the position outright.
- **Problem:** Raising the stop before the breakout level is confirmed, after the opening drive.
  **Solution:** Keep the stop wide until the close above the level is confirmed. Only then tighten it to the prior day's low or the breakout level.
- **Problem:** Failing to exit when the plan breaks because you are focused on the highest profit you could have captured.
  **Solution:** The goal is not to sell the high. The goal is to follow the process. If the prior bar low breaks, exit. Do not rationalize staying in.
- **Problem:** Treating every breakout as the same regardless of backdrop.
  **Solution:** Split your playbook. Momentum-only breakouts are trades to exit quickly. Breakouts with a catalyst with at least three supporting news events are a 1-to-4 week swing trade to hold because the catalyst justifies a larger price move.
