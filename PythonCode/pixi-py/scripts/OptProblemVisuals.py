import numpy as np
import matplotlib
import plotly
import plotnine


def lowProbFunc(z1, z2, x):
    return (z1 + x)^2 + (x-2)*z1*z2 + z2^2
