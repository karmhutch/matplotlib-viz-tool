from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# Import helper functions
from vizkarmhutch.functions import *
# Import style specs and update rcParams
from vizkarmhutch import style_web as style
plt.rcParams.update(style.params)


# Demonstrate how to access style attributes ---------------------------------------------------------------------------

fonts = FontSize()

# Demonstrate how to generate figures ----------------------------------------------------------------------------------

# Import example data as CSV
# Note: data from ...
data = ...


# helper function for formating Axes
def format_list(axes):
    for row in axes:
        for ax in row:
            format_axes(ax)
            format_axis(ax)

# Generate a single-axes figure
fig1, axes1 = generate_figure(style, num_rows=1, num_cols=1)
# format axes
format_list(axes1)
plt.show()


# Generate a dual-axes figure
fig2, axes2 = generate_figure(style, num_rows=1, num_cols=2)

# Generate a figure with 4 axes (2-by-2)
fig3, axes3 = generate_figure(style, num_rows=2, num_cols=2)
