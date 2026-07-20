import cvxpy as cp
import cvxpylayers as cplay
import numpy as np
import plotly
import plotnine

x = cp.Parameter()
z1 = cp.Variable()
z2 = cp.Variable()

lowObj = cp.Minimize((z1 + x)^2 + (x-2)*z1*z2 + z2^2)

lowProb = cp.Problem(obj, constraints)
lowProb.solve()

prob.status
prob.value
x.value
z.value
