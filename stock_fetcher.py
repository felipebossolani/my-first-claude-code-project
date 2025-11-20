#!/usr/bin/env python3
"""
Stock Price Fetcher - Retrieve historical stock prices from Yahoo Finance

This script fetches the last 30 days of historical stock price data for a given ticker symbol.
If no ticker is provided, it defaults to AAPL (Apple Inc.).

Usage:
    python stock_fetcher.py [TICKER]
    python stock_fetcher.py              # Uses AAPL as default
    python stock_fetcher.py MSFT         # Fetches Microsoft stock data
"""

import sys
import argparse
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd


def fetch_stock_prices(ticker: str = "AAPL", days: int = 30) -> pd.DataFrame:
    """
    Fetch historical stock price data from Yahoo Finance.

    Args:
        ticker (str): Stock ticker symbol (default: AAPL)
        days (int): Number of days of historical data to fetch (default: 30)

    Returns:
        pd.DataFrame: DataFrame containing historical stock price data with columns:
                     Date, Open, High, Low, Close, Volume

    Raises:
        ValueError: If ticker is invalid or data cannot be fetched
    """
    try:
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        # Fetch data from Yahoo Finance
        print(f"\nFetching {days} days of historical data for {ticker}...")
        ticker_obj = yf.Ticker(ticker)
        stock_data = ticker_obj.history(start=start_date, end=end_date)

        if stock_data.empty:
            raise ValueError(f"No data found for ticker '{ticker}'. Please check the ticker symbol.")

        return stock_data

    except Exception as e:
        raise ValueError(f"Error fetching data for {ticker}: {str(e)}")


def display_stock_data(stock_data: pd.DataFrame, ticker: str) -> None:
    """
    Display stock price data in a formatted table.

    Args:
        stock_data (pd.DataFrame): Historical stock price data
        ticker (str): Stock ticker symbol for display purposes
    """
    print(f"\n{'='*80}")
    print(f"Historical Stock Prices for {ticker} (Last 30 Days)")
    print(f"{'='*80}\n")

    # Display summary statistics
    print("Summary Statistics:")
    print(f"  Highest Close Price:  ${stock_data['Close'].max():.2f}")
    print(f"  Lowest Close Price:   ${stock_data['Close'].min():.2f}")
    print(f"  Average Close Price:  ${stock_data['Close'].mean():.2f}")
    print(f"  Trading Days:         {len(stock_data)}")

    # Display the data table
    print(f"\n{'Date':<12} {'Open':<10} {'High':<10} {'Low':<10} {'Close':<10} {'Volume':<15}")
    print("-" * 80)

    for date, row in stock_data.iterrows():
        date_str = date.strftime("%Y-%m-%d")
        print(f"{date_str:<12} ${row['Open']:<9.2f} ${row['High']:<9.2f} ${row['Low']:<9.2f} ${row['Close']:<9.2f} {int(row['Volume']):<15,}")


def main():
    """Main entry point for the stock price fetcher script."""

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Fetch and display historical stock prices from Yahoo Finance",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python stock_fetcher.py              # Fetch AAPL data (default)
  python stock_fetcher.py MSFT         # Fetch Microsoft data
  python stock_fetcher.py GOOGL        # Fetch Google data
        """
    )

    parser.add_argument(
        "ticker",
        nargs="?",
        default="AAPL",
        help="Stock ticker symbol (default: AAPL)"
    )

    args = parser.parse_args()
    args = parser.parse_args()
    
    # Split tickers by comma and clean up whitespace
    tickers = [t.strip().upper() for t in args.ticker.split(',')]

    for i, ticker in enumerate(tickers):
        if not ticker:
            continue
            
        try:
            # Fetch stock data
            stock_data = fetch_stock_prices(ticker)

            # Display the data
            display_stock_data(stock_data, ticker)

            # Print separator if not the last ticker
            if i < len(tickers) - 1:
                print(f"\n{'='*80}\n")

        except ValueError as e:
            print(f"\nError: {e}", file=sys.stderr)
        except Exception as e:
            print(f"\nUnexpected error processing {ticker}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
