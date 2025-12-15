import numpy as np

class GradientDescentSR:
    def __init__(self, A, AT, reg, lr=0.1, lam=0.1, iters=50):
        self.A = A
        self.AT = AT
        self.reg = reg
        self.lr = lr
        self.lam = lam
        self.iters = iters

    def solve(self, b, x0):
        x = x0.copy()
        shape = x0.shape
        cost_hist = []

        for _ in range(self.iters):
            Ax = self.A(x)
            grad = self.AT(Ax - b, shape) + self.lam * self.reg.gradient(x)
            x -= self.lr * grad
            x = np.clip(x, 0, 1)
            cost_hist.append(0.5 * np.sum((Ax - b)**2))

        return x, cost_hist
