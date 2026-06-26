import cvxpy as cp
import numpy as np

x1 = cp.Variable()
x2 = cp.Variable()

obj = cp.Minimize(cp.norm2(cp.hstack([1, x1+2])) + (1/2) * (x2 - 4) ** 2)

prob = cp.Problem(obj)
prob.solve()

print(prob.status)
print(prob.value)
print(x1.value)
print(x2.value)
