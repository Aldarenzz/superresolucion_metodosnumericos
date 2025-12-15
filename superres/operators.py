import numpy as np
from scipy.ndimage import gaussian_filter

class DegradationOperator:
    def __init__(self, sigma=1.0, s=2):
        self.sigma = sigma
        self.s = s

    def A(self, x):
        blurred = gaussian_filter(x, self.sigma)
        return blurred[::self.s, ::self.s]

    def AT(self, y, shape):
        up = np.zeros(shape)
        up[::self.s, ::self.s] = y
        return gaussian_filter(up, self.sigma)
