import pandas as pd
import numpy as np
from src.data.data_cleaner import DataCleaner
# 


class FeatureEngineering:
    """
    
    """

    def __init__(self):
        """
        
        """
        self.data_cleaner = DataCleaner()
    
    def check_valid_input(self, df):
        """
        
        """
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        elif not isinstance(df, pd.DatetimeIndex):
            if "timestamp" in df.columns:
                df["timestamp"] = pd.to_datetime(df["timestamp"])
                df.set_index("timestamp", inplace=True)
        return df
    
    def replace_nan(self, df):
        """
        
        """
        self.check_valid_input(df=df)
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.dropna(inplace=True)
        
    def split_data(self, df, target="close", train_size=80):
        """
        
        """
        df = self.check_valid_input(df=df)
        train_nums = int((len(df) / 100) * train_size)
        features = [column for column in df.columns if column not in [target, "timestamp"]]
        train_df = df.sample(n=train_nums, random_state=42)
        test_df = df.drop(train_df.index)
        x_train = train_df[features]
        y_train = train_df[target]
        x_test = test_df[features]
        y_test = test_df[target]
        return x_train, y_train, x_test, y_test
    
    def prepare_data_classification(self, df):
        """
        
        """
        df = self.check_valid_input(df=df)
        df["target"] = (df["close"].shift(-1) > df["close"]).astype(int)
        return df

    def variance(self, df, columns):
        """
        
        """
        df = self.check_valid_input(df=df)
        df = df[columns].var()
        return df

    def skewness(self, df, columns):
        """
        
        """
        df = self.check_valid_input(df=df)
        df = df[columns].skew(axis=0)
        return df
    
    def kurtosis(self, df, columns):
        """
        
        """
        df = self.check_valid_input(df=df)
        df = df[columns].kurtosis(axis=0)
        return df
    
    def period_returns(self, df, columns):
        """
        
        """
        df = self.check_valid_input(df=df)
        for column in columns:
            df[f"{column}_1d_returns"] = df[column].pct_change(1)
            weekly_returns = df[column].resample("W").last().pct_change()
            df[f"{column}_1W_returns"] = weekly_returns.reindex(df.index, method="ffill")
            monthly_returns = df[column].resample("ME").last().pct_change()
            df[f"{column}_1M_returns"] = monthly_returns.reindex(df.index, method="ffill")
            yearly_returns = df[column].resample("YE").last().pct_change()
            df[f"{column}_1Y_returns"] = yearly_returns.reindex(df.index, method="ffill")
        # self.replace_nan(df=df)
        return df
    
    def rolling_volatility(self, df, columns, windows):
        """
        
        """
        df = self.check_valid_input(df=df)
        for column in columns:
            for window in windows:
                df[f"{column}_vol_{window}"] = df[column].rolling(window=window).std()
        return df
    
    def drawdown(self, df, columns):
        """
        
        """
        df = self.check_valid_input(df=df)
        for column in columns:
            df[f"{column}_drawdown"] = (df[column] - df[column].cummax()) / df[column].cummax() * 100
            df[f"{column}_max_drawdown"] = df[f"{column}_drawdown"].min()
        return df
    
    def lags(self, df, columns, lags):
        """
        
        """
        df = self.check_valid_input(df=df)
        for column in columns:
            for lag in lags:
                df[f"{column}_lag_{lag}"] = df[column].shift(lag)
        return df