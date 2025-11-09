import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.math.activations import Activations
from src.math.loss import Loss
from src.data.data_loader import DataLoader
from src.data.feature_engineering import FeatureEngineering
from src.data.data_cleaner import DataCleaner
from src.visualization.model_visualization import ModelVisualization
# python -m src.models.linear_regression

class LinearRegression:
    def __init__(self, X, y, weights=None, bias=0.0, learning_rate=0.0001, epochs=10000):
        """
        """
        self.X = X
        self.y = y
        self.weights = weights if weights is not None else np.zeros(X.shape[1])
        self.bias = bias
        self.learning_rate = learning_rate
        self.epochs = epochs

    def train(self):
        """
        
        """
        mse_arr = []
        for epoch in range(self.epochs):
            N = self.X.shape[0]
            y_pred = self.X @ self.weights + self.bias
            error = y_pred - self.y
            dw = (2 / N) * (self.X.T @ error)
            db = (2 / N) * np.sum(error)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            mse = np.mean(error ** 2)
            mse_arr.append(mse)
            if epoch % 100 == 0:
                print(f"Epoch: {epoch + 100}")
                print(f"MSE: {mse}")
        return mse_arr, y_pred
    
    def predict(self, X):
        """
        
        """
        return X @ self.weights + self.bias
    


df = DataLoader().create_coin_df(coin="BTC", fiat="USDC", timeframe="1d")
df = FeatureEngineering().period_returns(df=df, columns=["close", "open", "high", "low", "volume"])
df = FeatureEngineering().rolling_volatility(df=df, columns=["volume"], windows=[7, 14, 30])
# df = FeatureEngineering().drawdown(df=df, columns=["close", "open", "high", "low", "volume"])
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)
df = DataCleaner().normalize_data(df=df)
x_train, y_train, x_test, y_test = FeatureEngineering().split_data(df=df)

model = LinearRegression(x_train, y_train)
mse_arr, y_pred_train = model.train()
y_pred_test = model.predict(x_test)
ModelVisualization().visualize_predictions(y_pred=y_pred_test, y=y_test)
ModelVisualization().visualize_loss(loss_arr=mse_arr, loss_name="MSE")