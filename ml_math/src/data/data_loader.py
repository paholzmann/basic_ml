from pathlib import Path
import os
import pandas as pd
import ccxt
import time

# python -m src.data_loader


class DataLoader:
    """
    
    """

    def __init__(self):
        """
        
        """
        self.exchange = ccxt.binance()
        self.limit = 1000

    def create_coin_df(self, coin, fiat, timeframe):
        """
        Creates a DataFrame for the selected coin, fiat and timeframe.

        Args:
            coins (str): String of coin.
            fiats (str): String of fiat.
            timeframes (str): String of timeframe.

        Returns:
            df (pd.DataFrame): DataFrame with OHLCV data.
                The DataFrame contains OHLCV data with the following columns:
                ["timestamp", "open", "high", "low", "close", "volume"]

        Example:
            >>>
            >>>
        """
        try:
            bars = self.exchange.fetch_ohlcv(
                f"{coin}/{fiat}", f"{timeframe}", limit=self.limit)
            df = pd.DataFrame(
                bars, columns=["timestamp", "open", "high", "low", "close", "volume"])
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        except Exception as error:
            print(f"Error fetching data for {coin}/{fiat}: {error}")
            bars = []
            df = pd.DataFrame(
                bars, columns=["timestamp", "open", "high", "low", "close", "volume"])
        return df

    def print_data_frame(self, coin=None, fiat=None, timeframe=None, df=None):
        """
        Prints DataFrames in a nestled dictionary for every coin, fiat and timeframe.

        Args:
            dfs (dict[str, dict[str, dict[str, pd.DataFrame]]]): Nestled dictionary for every coin, fiat and timeframe.

        Output:
            Coin: {coin}, fiat: {fiat}, timeframe: {timeframe}.
            pd.DataFrame

        Example:
            >>> obj.print_data_frames(dfs=crypto_dfs)
            Coin: BTC, fiat: USDT, timeframe: 1s
            pd.DataFrame

            Coin: ETH, fiat: USDT, timeframe: 1s
            pd.DataFrame
        """
        if isinstance(df, pd.DataFrame):
            print("*" * 200)
            print(f"Coin: {coin}, fiat: {fiat}, timeframe: {timeframe}")
            print(df)
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")
