import numpy as np
import pandas as pd
class DataCleaner:
    def __init__(self):
        """
        
        """

    def remove_duplicates(self, df):
        """
        
        """
        if isinstance(df, pd.DataFrame):
            if "timestamp" not in df.columns:
                raise ValueError(f"'timestamp'-column missing.")
            else:
                df = df.drop_duplicates(subset=["timestamp"])
            return df
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")

    def convert_to_float(self, df):
        """
        
        """
        if isinstance(df, pd.DataFrame):
            for column in df.columns:
                if column != "timestamp":
                    df[column] = pd.to_numeric(
                        df[column], errors="coerce").round(4)
            return df
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")

    def fill_missing_with_forward(self, df):
        """
        
        """
        if isinstance(df, pd.DataFrame):
            for column in df.columns:
                if column != "timestamp":
                    df[column] = df[column].ffill()
            return df
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")

    def fill_missing_with_backward(self, df):
        """
        
        """
        if isinstance(df, pd.DataFrame):
            for column in df.columns:
                if column != "timestamp":
                    df[column] = df[column].bfill()
            return df
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")

    def fill_missing_with_interpolation(self, df):
        """
        
        """
        if isinstance(df, pd.DataFrame):
            for column in df.columns:
                if column != "timestamp":
                    df[column] = df[column].interpolate(method="linear")
            return df
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")

    def fill_missing_with_mean(self, df):
        """
        
        """
        if isinstance(df, pd.DataFrame):
            for column in df.columns:
                if column != "timestamp":
                    df[column] = df[column].fillna(value=df[column].mean())
            return df
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")

    def fill_missing_with_median(self, df):
        """
        
        """
        if isinstance(df, pd.DataFrame):
            for column in df.columns:
                if column != "timestamp":
                    df[column] = df[column].fillna(value=df[column].median())
            return df
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")

    def sort_data(self, df):
        """
        
        """
        if isinstance(df, pd.DataFrame):
            if "volume" in df.columns:
                df = df.sort_values(by="volume").reset_index(drop=True)
                return df
            else:
                raise ValueError("Timestamp column missing in pd.DataFrame.")
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")

    def correct_extream_peaks(self, df):
        """

        """
        if isinstance(df, pd.DataFrame):
            for column in df.columns:
                if column != "timestamp":
                    Q1 = df[column].quantile(0.25)
                    Q3 = df[column].quantile(0.75)
                    IQR = Q3 - Q1
                    lower = Q1 - 1.5 * IQR
                    upper = Q3 + 1.5 * IQR
                    df[column] = df[column].clip(lower=lower, upper=upper)
            return df
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")

    def normalize_data(self, df):
        """
        
        """
        if isinstance(df, pd.DataFrame):
            for column in df.columns:
                if column != "timestamp":
                    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
            return df
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")

    def standardize_data(self, df):
        """
        
        """
        if isinstance(df, pd.DataFrame):
            for column in df.columns:
                if column != "timestamp":
                    df[column] = (df[column] - df[column].mean()) / df[column].std()
            return df
        else:
            raise ValueError(
                f"Expected a pandas DataFrame, got {type(df).__name__} instead.")
