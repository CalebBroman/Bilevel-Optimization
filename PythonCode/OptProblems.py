import cvxpy as cp
import cvxpylayers as cplay
import numpy as np

x = cp.Variable()
z = cp.Variable()

constraints = []

obj = cp.Minimize()

prob = cp.Problem(obj, constraints)
prob.solve()

prob.status
prob.value
x.value
z.value
