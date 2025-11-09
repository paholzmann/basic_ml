import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from src.math.activations import Activations
from src.math.loss import Loss
from src.data.data_loader import DataLoader
from src.data.feature_engineering import FeatureEngineering
from src.data.data_cleaner import DataCleaner
from src.visualization.model_visualization import ModelVisualization

# python -m src.models.logistic_regression

class ComplexLogisticRegression:
    def __init__(self):
        """
        
        """
        self.model = None

    def train(self, df):
        """
        
        """
        X = df.drop(columns=["target"])
        y = df["target"]
        self.model = LogisticRegression(solver="lbfgs", max_iter=1000, random_state=42)
        self.model.fit(X, y)

    def predict(self, x_test, y_test):
        y_pred = self.model.predict(x_test)
        print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
        print(classification_report(y_test, y_pred))
        return y_pred
    

df = DataLoader().create_coin_df(coin="BTC", fiat="USDC", timeframe="1d")
df = FeatureEngineering().prepare_data_classification(df=df)
df = FeatureEngineering().period_returns(df=df, columns=["close", "open", "high", "low", "volume"])
df = FeatureEngineering().rolling_volatility(df=df, columns=["volume"], windows=[7, 14, 30])
df = FeatureEngineering().lags(df=df, columns=["close", "open", "high", "low", "volume"], lags=[1, 2, 3])
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)
x_train, y_train, x_test, y_test = FeatureEngineering().split_data(df=df, target="target")
model = LogisticRegression(solver="lbfgs", max_iter=10000, random_state=42)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))
y_pred_train = model.predict(x_train)
print(f"Accuracy: {accuracy_score(y_train, y_pred_train)}")
print(classification_report(y_train, y_pred_train))