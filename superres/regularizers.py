import numpy as np

def gradients(x):
    Dx = np.roll(x,-1,axis=1) - x
    Dy = np.roll(x,-1,axis=0) - x
    return Dx, Dy

def div(px, py):
    rx = px - np.roll(px,1,axis=1)
    ry = py - np.roll(py,1,axis=0)
    return rx + ry

class L2Regularizer:
    def gradient(self, x):
        Dx, Dy = gradients(x)
        return -div(Dx, Dy)

class HuberRegularizer:
    def __init__(self, delta=0.01):
        self.delta = delta

    def gradient(self, x):
        Dx, Dy = gradients(x)
        px = Dx / np.maximum(self.delta, np.abs(Dx))
        py = Dy / np.maximum(self.delta, np.abs(Dy))
        return -div(px, py)
