import cvxpy as cp
import cvxpylayers as cplay
import numpy as np

x = cp.Parameter(nonneg = True)
x.value = 1
z1 = cp.Variable()
z2 = cp.Variable()

lowObj = cp.Minimize((z1 + x)**2 + (x-2)*(z1+z2) + z2**2)

lowProb = cp.Problem(lowObj)
#lowLayer = layer(lowProb, parameters = [x], variables = [z1, z2])

lowResult = lowProb.solve()

print(lowProb.status)
print(z1.value)
print(z2.value)
