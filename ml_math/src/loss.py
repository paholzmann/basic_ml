import numpy as np # type: ignore

class Loss:
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
    
    def mse(self, x):
        """
        
        """
