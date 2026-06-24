import cvxpy as cp
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
