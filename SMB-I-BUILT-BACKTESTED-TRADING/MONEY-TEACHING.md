# SMB-I-BUILT-BACKTESTED-TRADING

## Overview

This Money Teaching shows how to use Claude Code to automate backtesting and strategy development for systematic trading. It focuses on linking Claude to backtesting platforms like AmiBroker or RealTest, providing reference scripts for consistent strategy generation, and building verification skills so Claude can self-check its work. The goal is to help systematic traders run four to five times as many backtests in less time while following software development best practices to avoid technical debt.

## When to Follow These Money Teachings

- When you want to automate running backtests without manual intervention
- When you need Claude to generate new trading strategy code in a consistent style
- When you want to reduce the time spent iterating on strategy ideas
- When you need to verify strategy correctness quickly before running full backtests
- When you want to apply software development best practices to trading code

## Steps

### Step 1: Link Claude Code to Your Backtesting Platform

Connect Claude Code to a backtesting platform that supports automation, such as AmiBroker or RealTest. AmiBroker provides a standard Windows interface that allows Python scripts to run backtests, save results, and export to CSV without manual intervention. Configure Claude so that it can execute backtests on your behalf with a command. Automating backtests eliminates the need to manually click buttons, wait for results, and save files. If your current platform does not support external automation, consider switching to a platform that does, since this is a foundational step for the rest of the workflow.

### Step 2: Provide Claude with a Reference Script When Generating Strategies

When asking Claude to write a new trading strategy, always provide an example of an existing strategy script written in your preferred style. Include the conventions you follow, such as how trades are executed, how columns are captured, variable naming patterns, and how the script interacts with your backtesting platform. This is especially important for AmiBroker Formula Language (AFL) scripts, where there are different ways to write a strategy but only one structure that supports custom columns. By giving Claude a reference, you reduce token usage, and ensure new strategies integrate seamlessly with your existing codebase.

### Step 3: Build a Smoke Test Skill for Claude

Create a skill or function that allows Claude to run a quick smoke test on any new strategy before running a full backtest. The smoke test should run the strategy on a single symbol or a single day's data, which takes seconds instead of the 40 minutes to an hour that a full backtest requires. Configure Claude to use this skill automatically after generating a new strategy so it can immediately verify whether the code is working. If the smoke test returns no results, too many results, or results that do not match expected trades, Claude can diagnose the issue right away rather than waiting for a full backtest to complete.

### Step 4: Give Claude a Self-Verification Mechanism

Extend Claude's capabilities by giving it a way to verify its own correctness, similar to unit testing in software development. For each new strategy, specify expected trades, such as a Microsoft trade on a specific date that should appear in the back test. Have Claude run the backtest and check whether those expected trades are present. If an expected trade is missing, Claude can investigate the cause, such as a logic error in the strategy code or a data issue, and report back. This step ensures that strategies produce the expected trades specified in the verification step before they are used in production.

### Step 5: Run Parameterized Backtests Overnight

Once Claude can run backtests independently, set up parameterized variations of your strategies and let them run overnight. Instead of manually changing parameters one at a time, configure Claude to iterate through parameter sets and run each version automatically. Wake up to a full set of results and use them to optimize your strategy. This can increase the number of backtests you run by four to five times without any extra manual effort, turning a weekend task into an overnight batch job.

### Step 6: Use GitHub Properly for Version Control

Adopt standard GitHub practices, including using branches instead of committing directly to main. Create a new branch for every change or new strategy, do all development and testing in that branch, and submit a pull request when ready to merge. Use the pull request process to perform code reviews, including letting Claude review its own code or having reviewers look at it. Never develop directly in the main branch if your code controls live trading strategies, because a mistake could break production code. Bite-size branches are easier to merge and easier to debug when something goes wrong.

## Examples

### Example 1: Automating AmiBroker Backtests with Python

A systematic trader uses AmiBroker for backtesting but previously had to manually click the backtest button, wait for results, and save the CSV. By writing a Python script that uses AmiBroker's interface, they taught Claude to run backtests with a command. Claude executes the backtest, saves the results to a consistent location, and reports the output. This allows the trader to queue up four or five backtests and run them overnight, waking up to completed results instead of manually managing each run.

### Example 2: Using a Reference Script to Generate Consistent Strategies

A trader gave Claude an existing AmiBroker AFL script as a reference when asking it to write a new opening range breakout strategy. Because the reference included the exact structure, variable naming conventions, and column capture methods, Claude produced a new script that matched the trader's style and included the necessary custom columns for analysis. Without the reference, Claude returned different implementations that required additional rework and increased token usage.

### Example 3: Smoke Testing a New Strategy in Seconds

A trader created a Claude skill that runs a backtest on only the MSFT symbol for a single day. After Claude writes a new strategy, it automatically runs the smoke test and sees that the expected trade on MSFT for that day is present. This confirms the strategy logic is correct in under a minute, whereas a full backtest would take 40 minutes. When the smoke test fails, Claude investigates immediately and reports the issue, saving debugging time.

## Best Practices

- ✅ Use backtesting tools like AmiBroker or RealTest instead of trying to build your own backtesting system from scratch with Claude
- ✅ Provide Claude with a reference script and clear context so it generates code in your style and conventions
- ✅ Build reusable skills or functions for repetitive tasks like smoke tests, data lookups, and verification checks
- ✅ Use version control properly with branches, pull requests, and code reviews
- ✅ Keep changes to bite-size pieces so they are easy to test, merge, and debug
- ✅ Use consistent variable names across all strategies so changes can be made quickly
- ✅ Run parameterized backtests overnight to maximize the number of strategies tested
- ✅ Give Claude specific prompts with full context to reduce token usage

## Keep In Mind

- Claude Code is a tool that amplifies your existing process; it does not replace the need for judgment based on established software development practices such as version control, code reviews, and testing changes before merging
- The more context and specificity you provide in your prompts, the more specific and less costly the results will be
- Software development best practices apply directly to trading strategy code, including version control, code reviews, and avoiding technical debt
- The bottleneck for experienced traders shifts from insufficient ideas to test to an excess of ideas to test, so automation is key
- Projects that do not control live trades, such as research dashboards, are not mission critical compared to live trading strategies; prioritize best practices based on whether code controls live trades.

## Security & Safety Notes

- Never commit secrets, API keys, or credentials to version control or share them with Claude in prompts
- Always test new strategies in a paper trading or sandbox environment before deploying them to live accounts
- Use pull requests and code reviews to ensure that changes to production strategies are verified before merging
- Keep production code on a protected main branch and never develop directly on it when strategies are live
- Review Claude-generated code before using it in production, especially for risk management and position sizing logic

## Common Pitfalls

- **Problem:** Trying to build a custom backtesting system from scratch with Claude instead of using an established platform like AmiBroker
  **Solution:** Use tools that have been refined for 30 years, such as AmiBroker, which is the most efficient way for the retail trader.
- **Problem:** Not providing sufficient context in prompts, leading to inconsistent code and elevated token costs
  **Solution:** Give Claude a reference script, specify exact parameters, time frames, stops, and profit targets specifically. The more specific the prompt, the higher the likelihood of a successful one-shot result.
- **Problem:** Committing directly to the main branch without testing, risking broken production code
  **Solution:** Always create a feature branch, test changes in isolation, and merge via a pull request after review.
- **Problem:** Taking on projects that are too large to safely test and merge, making it impossible to identify what change broke production
  **Solution:** Break work into bite-size pieces. Create a branch for each piece, test it, and merge it before starting the next.
- **Problem:** Generating code without style guides, creating technical debt that is hard to maintain
  **Solution:** Define and enforce a style guide for all strategy code. Use consistent variable names and structure so all strategies conform to your defined style guide.
- **Problem:** Running full backtests every time you want to verify a bite-size change, wasting the 40 minutes to an hour a full backtest requires
  **Solution:** Build a smoke test skill that runs a single symbol or a single day of data in seconds. Use it after every code change before running a full backtest.
