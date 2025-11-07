import numpy as np # type: ignore

class Loss:
    def __init__(self):
        """
        
        """

    def get_arr(self, x):
        """
        
        """
        if isinstance(x, (int, float)):
            return np.array([x])
        if isinstance(x, list):
            return np.array(x)
        if isinstance(x, np.ndarray):
            return x
        raise TypeError("Input must be a list or numpy array of numbers.")
    
    def mse(self, i, t):
        """
        
        """
        i = self.get_arr(x=i)
        t = self.get_arr(x=t)
        return np.mean((t - i) ** 2)
    
    def rmse(self, i, t):
        """
        
        """
        i = self.get_arr(x=i)
        t = self.get_arr(x=t)
        return np.sqrt(np.mean((t - i) ** 2))
    
    def mae(self, i, t):
        """
        
        """
        i = self.get_arr(x=i)
        t = self.get_arr(x=t)
        return np.mean(np.abs(t - i))
    
    def huber(self, i, t, delta=1.0):
        """
        
        """
        i = self.get_arr(x=i)
        t = self.get_arr(x=t)
        return np.where(np.abs(t - i) <= delta, 0.5 * ((t - i) ** 2), delta * (np.abs(t - i) - 0.5 * delta))
    
    def log_cosh(self, i, t):
        """
        
        """
        i = self.get_arr(x=i)
        t = self.get_arr(x=t)
        x = i - t
        return x + np.log1p(np.exp(-2 * x)) - np.log(2)
    
    def binary_cross_entropy(self, i, t):
        """
        
        """
        i = self.get_arr(x=i)
        t = self.get_arr(x=t)
        i = np.clip(i, 1e-9, 1-1e-9)
        return - (t * np.log(i) + (1 - t) * np.log(1 - i))
    
    def categorical_cross_entropy(self, i, t):
        """
        
        """
        i = self.get_arr(x=i)
        t = self.get_arr(x=t)

# i = np.array([0.1, 0.2, 0.3])
# t = np.array([0.9, 0.4, 0.7])
# print(Loss().log_cosh(i=i, t=t))