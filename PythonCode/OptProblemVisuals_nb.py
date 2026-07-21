import marimo

__generated_with = "0.23.14"
app = marimo.App()


@app.cell
def _():
    import numpy as np
    import matplotlib
    import plotly


    def lowProbFunc(z1, z2, x):
        return (z1 + x)^2 + (x-2)*z1*z2 + z2^2



    return


if __name__ == "__main__":
    app.run()
