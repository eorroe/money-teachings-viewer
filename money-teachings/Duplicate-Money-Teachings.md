# Duplicate Money Teachings Report

Generated: 2026-09-11

This report identifies groups of similar or duplicate money teachings across the 23 MONEY-TEACHING.md files in the money-teachings directory. Each group contains files that share overlapping strategies, step-by-step instructions, examples, or topic coverage.

---

## Group 1: Building AI Trading Assistants with Claude (3 files)

| File | Description | Key Differences | Recommendation |
|------|-------------|-----------------|----------------|
| `SMB-Capital-4-Things-Knew-Creating-AI-Trading-Assistant/MONEY-TEACHING.md` | Focuses on 4 critical mistakes to avoid when building an AI trading assistant with Claude Code, emphasizing inference architecture, separate chat sessions, architecture docs, and settings tab. | Most technical; emphasizes inference architecture where the LLM actively processes data at runtime, per-layer architecture documents, and "closing the loop." | **Keep** - Unique focus on architecture design and avoiding context degradation in Claude Code sessions. |
| `SMB-Capital-Build-Claude-AI-Trading-Assistant/MONEY-TEACHING.md` | Beginner-friendly guide to building a Claude AI trading assistant with zero coding experience. Covers identifying daily processes, building with Claude Code, refining prompts, adding real-time data, and building scanners. | Most comprehensive beginner guide; focuses on operational edge (workflow automation) rather than predictive signals. Includes specific examples like pre-market research digests and trade tracker dashboards. | **Keep** - Unique beginner-focused, operational automation angle. |
| `SMB-Capital-Simple-4-Step-Process-Build-AI-Trading-Assistant/MONEY-TEACHING.md` | Simple 4-step process (Plan, Build, Personalize, Automate) for building an AI trading assistant with Claude. | Most structured and concise; emphasizes plan mode, personalization to trading style, and integration with TradingView/broker tools. Uses Pine Script v5 and Python script examples. | **Keep** - Unique 4-step framework structure and specific tool integration examples. |

**Summary:** All three teach building AI trading assistants with Claude Code. They share similar core advice (prompt refinement, personalization, validation) but differ in focus: architecture design vs. beginner operational automation vs. simple 4-step process. The content overlap is moderate (~30-40%). Consider merging into one comprehensive file or keeping all three for different audience levels.

---

## Group 2: Pink Line / Breakout Trading Methodology (2 files)

| File | Description | Key Differences | Recommendation |
|------|-------------|-----------------|----------------|
| `SMB-Capital-7-Trading-Signals-Cant-Trade-Without/MONEY-TEACHING.md` | Seven critical checks for breakout trades, including pink line (signal 1), higher time frame compression (signal 2), blue sky (signal 3), narrative (signal 4), volume moment (signal 5), clean tape (signal 6), and hidden relative strength (signal 7). | Broader scope; pink line is only one of seven signals. Includes ATR thresholds (1.5% minimum), momentum name criteria, and market tailwind requirements. | **Keep** - Unique as a comprehensive 7-signal framework. |
| `SMB-Capital-End-Needless-Losses-Catch-More-Winners/MONEY-TEACHING.md` | Entirely focused on the "pink line rule" — waiting for a full candle close above the most recent multi-week/month high before entering. Includes four exceptions (catalyst, compression, strong close, in-play intraday). | Deep dive on pink line only; includes energy expenditure measurement (0.50x ATR), 10-minute price discovery avoidance, trading at range edges, and extensive examples (Tesla, SMCI). | **Keep** - Unique as a standalone pink line methodology with exceptions. |

**Summary:** Both files cover the pink line breakout concept, but the "7 Signals" file treats it as one component of a larger framework, while "End Needless Losses" is an exhaustive deep dive on the pink line rule alone. The overlap is primarily in the pink line identification and grading steps (~25-30%). The "End Needless Losses" file adds unique exceptions and energy measurement not found in "7 Signals."

---

## Group 3: Parabolic Mean Reversion Short Strategies (3 files)

| File | Description | Key Differences | Recommendation |
|------|-------------|-----------------|----------------|
| `SMB-Capital-Gold-Going-Parabolic-Traders-Losing/MONEY-TEACHING.md` | Structured framework for parabolic mean reversion short trades in any asset class. Covers identification, euphoria confirmation, technical levels, pre-market probing, regular session entries, lagard correlations, options expirations, and market session timing. | Broadest scope; covers commodities, equities, ETFs. Includes laggard correlation (silver vs. gold), options expiration dynamics (0DTE delta hedging), and London close timing. | **Keep** - Unique in covering options expiration effects and multi-asset class application. |
| `SMB-Capital-Most-Profitable-RSI-Strategy-Used-Our-Traders/MONEY-TEACHING.md` | SMB Capital's #1 revenue-generating strategy: customized RSI (20-period, 80/20 thresholds) mean reversion short on overextended assets across daily, intermediate, and short-term time frames. | Most indicator-specific; focuses exclusively on RSI configuration and multi-timeframe alignment. Includes opening range breakdown entry trigger. Examples: SLV, GLD, MSTR, SMCI. | **Keep** - Unique in its RSI-specific configuration and multi-timeframe alignment methodology. |
| `SMB-Capital-Secrets-Behind-7-Figure-Short-Trade/MONEY-TEACHING.md` | Breakdown of a seven-figure gold short trade using daily/intraday technical analysis, scanner criteria (consecutive up days, rising volume, ATR expansion), two-step entries, and systematic exits. | Most specific to a single trade example (GLD Oct 21); includes scanner build instructions, two-step entry with two-bar break, and exit on biggest volume candle of the day. | **Keep** - Unique in its trade-review approach, scanner criteria, and two-step entry methodology. |

**Summary:** All three cover parabolic/overextended mean reversion short trades, often using gold examples. However, each has a distinct methodology: RSI multi-timeframe alignment, options expiration dynamics, and scanner-based two-step entries. The overlap is in the general concept and gold examples (~20-30%). They complement each other well.

---

## Group 4: Trading Playbook / Grading Systems (2 files)

| File | Description | Key Differences | Recommendation |
|------|-------------|-----------------|----------------|
| `SMB-Capital-Become-7-Figure-Trader-Elite-Prop-Firm-Playbook/MONEY-TEACHING.md` | 10-variable playbook template for building a profitable trading career. Covers daily playbook exercise, 10 variables (big picture through diligence), scoring 80+, defining entries/exits, tape reading, due diligence, catalyst scoring, risk allocation, and trade reviews. | Specific 10-variable template with 1-10 scoring. Focuses on daily playbook exercise and compiling a database of playbook trades. | **Keep** - Unique 10-variable framework. |
| `SMB-Capital-What-Prop-Desks-Dont-Want-Know/MONEY-TEACHING.md` | Grading trading setups by category (A+, A, A-, B, C) with percentage risk allocations and distinct risk management approaches per grade. | Grade-based system (A+ = 80% of daily limit, A = 40%, etc.). Focuses on position sizing by grade rather than a 10-variable score. Includes misgrade tracking and monthly review. | **Keep** - Unique grading and risk allocation framework. |

**Summary:** Both teach systematic trading with structured frameworks, but use different grading systems (10-variable score vs. A+/A/A-/B/C grades). They can be used together but are not duplicates. Overlap is in the philosophy of systematic trading and trade review (~15-20%).

---

## Group 5: Theme / Catalyst-Based Trade Selection (2 files)

| File | Description | Key Differences | Recommendation |
|------|-------------|-----------------|----------------|
| `SMB-Capital-Secret-Finding-Most-Profitable-Trades/MONEY-TEACHING.md` | How to identify "stocks in play" by combining catalysts with themes. Covers theme watch lists, volume scanning, sympathy plays, projecting future catalysts, and executing by trading style. | Focus on theme building, watch list maintenance, and sympathy plays. Examples: data center (Enphase, Iron, Cypher), robotics (Tesla, IRBT), quantum. | **Keep** - Unique theme-building and sympathy play focus. |
| `SMB-Capital-Best-Earnings-Trading-Strategy/MONEY-TEACHING.md` | "Hot theme getting rewarded" earnings strategy — trading later reporters in a theme after early reporters show strong follow-through. | Specific to earnings season; focuses on theme momentum overriding individual fundamentals. Includes float/short interest filters and day-one volume confirmation. | **Keep** - Unique earnings-specific theme momentum strategy. |

**Summary:** Both cover themes and catalysts, but "Secret Finding" is about general theme building and sympathy plays, while "Best Earnings Strategy" is specifically about earnings season theme momentum. Overlap is in the theme/catalyst philosophy (~20-25%).

---

## Group 6: Backtesting / Strategy Development with Claude (1 file)

| File | Description | Key Differences | Recommendation |
|------|-------------|-----------------|----------------|
| `SMB-Capital-Built-Backtested-Trading-Strategies-Claude-Code/MONEY-TEACHING.md` | Using Claude Code to build, backtest, and automate trading strategies. Covers strategy design in plain English, Pine Script generation, realistic backtesting (commission/slippage), verification, and automated execution. | Unique in its focus on backtesting with realistic settings (0.05% commission, 1-tick slippage) and automating TradingView alerts to brokers. | **Keep** - No significant duplicate. |

**Note:** This file overlaps with Group 1 (AI assistants) in using Claude Code, but its focus on backtesting and strategy automation makes it distinct.

---

## Summary of Duplicates Found

| Group | Files | Overlap Level | Action |
|-------|-------|---------------|--------|
| AI Trading Assistants (3 files) | 4-Things, Build, Simple-4-Step | Moderate (30-40%) | Keep all — different audience levels and angles |
| Pink Line Methodology (2 files) | 7-Signals, End-Needless-Losses | Moderate (25-30%) | Keep all — one is a framework, one is a deep dive |
| Parabolic Mean Reversion Shorts (3 files) | Gold-Parabolic, Most-Profitable-RSI, 7-Figure-Short | Low-Moderate (20-30%) | Keep all — distinct methodologies |
| Trading Playbook / Grading (2 files) | Become-7-Figure, What-Prop-Desks-Dont-Want-Know | Low (15-20%) | Keep all — complementary systems |
| Theme / Catalyst Selection (2 files) | Secret-Finding, Best-Earnings-Strategy | Low-Moderate (20-25%) | Keep all — general vs. earnings-specific |

**Conclusion:** No files are exact duplicates. The highest overlap is in Group 1 (AI Trading Assistants) at 30-40%, but each file serves a different purpose and audience. All 23 files are recommended to be kept as they cover distinct aspects of trading education, even when sharing common concepts like the pink line, parabolic shorts, or Claude Code usage.
