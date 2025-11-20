# Stock Price Fetcher

A simple Python script to fetch and display historical stock prices from Yahoo Finance using the `yfinance` library.

[Abrir no Binder](https://mybinder.org/v2/gh/felipebossolani/my-first-claude-code-project/HEAD)

## Features

- Fetches the last 30 days of historical stock price data
- Displays stock data in a formatted table
- Shows summary statistics (high, low, average prices)
- Supports command-line arguments for custom stock tickers (single or multiple)
- Defaults to AAPL (Apple Inc.) if no ticker is provided

## Requirements

- Python 3.7+
- yfinance >= 0.2.35
- pandas >= 1.3.0

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/my-first-claude-code-project.git
cd my-first-claude-code-project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Fetch Apple stock data (default):
```bash
python stock_fetcher.py
```

### Fetch a specific stock ticker:
```bash
python stock_fetcher.py MSFT      # Microsoft
python stock_fetcher.py GOOGL     # Google
python stock_fetcher.py TSLA      # Tesla
```

### Fetch multiple stock tickers:
```bash
python stock_fetcher.py AAPL,MSFT,GOOGL
```

### View help:
```bash
python stock_fetcher.py --help
```

## Output

The script displays:
- Summary statistics (highest, lowest, and average closing prices)
- A detailed table with dates and OHLCV (Open, High, Low, Close, Volume) data
- Data is formatted for easy reading

Example output:
```
Fetching 30 days of historical data for AAPL...

================================================================================
Historical Stock Prices for AAPL (Last 30 Days)
================================================================================

Summary Statistics:
  Highest Close Price:  $275.25
  Lowest Close Price:   $258.20
  Average Close Price:  $268.15
  Trading Days:         23
```

## Error Handling

If an invalid ticker is provided, the script will display an error message:
```
Error: No data found for ticker 'INVALID'. Please check the ticker symbol.
```

## File Structure

```
my-first-claude-code-project/
├── stock_fetcher.py      # Main script
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## License

This project is open source and available under the MIT License.
