import numpy as np # type: ignore
from scipy.special import erf # type: ignore

class Activations:
    def __init__(self):
        """
        
        """

    def get_arr(self, x):
        """
        
        """
        if not isinstance(x, (list, np.ndarray)):
            raise TypeError("Input must be a list or numpy array of numbers.")
        arr = np.asarray(x)
        if not np.issubdtype(arr.dtype, np.number):
            raise TypeError("Input must contain numeric types only.")
        return arr
    # -------------------------------------------------- LINEAR & CLASSIC ACTIVATIONS --------------------------------------------------
    def linear(self, x):
        """
        f(x) = x
        """
        arr = self.get_arr(x=x)
        return arr
    
    def binary_step(self, x):
        """
        if x >= 0 -> 1
        if x < 0 -> 0
        """
        arr = self.get_arr(x=x)
        return np.where(arr >= 0, 1, 0)

    # -------------------------------------------------- SIGMOID FAMILY --------------------------------------------------
    def sigmoid(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return 1 / (1 + np.exp(-arr))
    
    def tanh(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return (np.exp(arr) - np.exp(-arr)) / (np.exp(arr) + np.exp(-arr))
    
    def hard_sigmoid(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.maximum(0, np.minimum(1, 0.2 * arr + 0.5))
    
    def hard_tanh(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.maximum(-1, np.minimum(1, arr))
    
    # -------------------------------------------------- RELU FAMILY --------------------------------------------------
    def relu(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.maximum(0, arr)
    
    def leaky_relu(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.where(arr > 0, arr, 0.01 * arr)
    
    def parametric_relu(self, x, alpha=0.01):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.where(arr > 0, arr, alpha * arr)
    
    def randomized_relu(self, x, training=False):
        """
        
        """
        arr = self.get_arr(x=x)
        l, u = 0.01, 0.03
        if training:
            alpha = np.random.uniform(l, u, size=x.shape)
        else:
            alpha = (l + u) / 2
        return np.where(arr > 0, arr, alpha * arr)
    
    def elu(self, x, alpha=0.01):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.where(arr > 0, arr, alpha * (np.exp(arr) -1))
    
    def selu(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        alpha, scale = 1.6732632423543772, 1.0507009873554805
        return scale * np.where(arr > 0, arr, alpha * (np.exp(arr) -1))
    
    def gelu(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return arr * 0.5 * (1 + erf(arr / np.sqrt(2)))
    
    def swish(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return arr *  (1 / (1 + np.exp(-arr)))
    
    def mish(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return arr * ((np.exp(np.log1p(np.exp(arr))) - np.exp(-np.log1p(np.exp(arr)))) / (np.exp(np.log1p(np.exp(arr))) + np.exp(-np.log1p(np.exp(arr)))))
    
    def softplus(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.log1p(np.exp(arr))
    
    # -------------------------------------------------- SOFTMAX FAMILY --------------------------------------------------
    def softmax(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.exp(arr) / np.sum(np.exp(arr))

    def log_softmax(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.log1p(np.exp(arr) / np.sum(np.exp(arr)))

    # -------------------------------------------------- SPECIAL FUNCTIONS --------------------------------------------------
    def softsign(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return arr / (1 + np.abs(arr))

    def sin(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.sin(arr)
    
    def cos(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.cos(arr)

    def arctan(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.arctan(arr)

    def bent_identity(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return ((np.sqrt(arr ** 2 + 1) - 1) / 2) + arr
    
    def gaussian(self, x):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.exp(-arr ** 2)
    
    def rbf(self, x, c=0.0, sigma=1.0):
        """
        
        """
        arr = self.get_arr(x=x)
        return np.exp(-((arr - c) ** 2) / (2 * sigma ** 2))