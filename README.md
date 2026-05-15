# AI Trading Bot

This repository contains a minimal, self-contained AI trading bot example that
uses a simple trend strategy:

- **Buy** when the recent short-term average is above the previous average.
- **Sell** when the recent short-term average is below the previous average.
- **Hold** when there is not enough signal.

## Run tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Run a quick simulation

```bash
python ai_trading_bot.py
```
