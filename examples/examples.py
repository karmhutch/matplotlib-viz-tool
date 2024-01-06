import os
from typing import List
import numpy as np

# Import style specs and update rcParams
from vizkarmhutch import (style_web as style, main_colors as colors)
# Import helper functions
from vizkarmhutch.functions import *

plt.rcParams.update(style.params)

np.random.seed(42)


# Demonstrate how to access style attributes ---------------------------------------------------------------------------

# text element
title = style.title

# element attributes
title_size = title.size
title_weight = title.weight
title_color = title.color
print(f"Title specs: [size = {title_size}, weight = {title_weight}, color = {title_color}]")

# color object
teal = colors.teal

# color attributes
series_hex_code = teal.series
label_hex_code = teal.label
print(f"Teal color specs: [series hex = {series_hex_code}, label hex = {label_hex_code}]")


# Demonstrate how to generate figures ----------------------------------------------------------------------------------

# helper function for formatting Axes
def format_list(axes: List[List]):
    for row in axes:
        for ax in row:
            format_axes(ax)
            format_axis(ax)


## Generate a single-axes figure

fig1, axes1 = generate_figure(style, num_rows=1, num_cols=1,
                              top_margin=0.11, bottom_margin=0.15,
                              left_margin=0.06, aspect=0.5)

# format axes
format_list(axes1)

# there is only one axes
ax1 = axes1[0][0]

# set titles and axis labels
ax1.set_title("Example #1: Single-axes figure", pad=20)
ax1.set_ylabel("Value")
ax1.set_xlabel("Year", labelpad=10)

# plot toy data
years = range(2010, 2024)
values = [np.random.randint(1, 100) for y in years]
ax1.plot(years, values, color=colors.purple.series)
ax1.set_ylim(0, 100)

# add source note
fig1.text(0.99, 0.01, "Source: vizkarmhutch (Karmen Hutchinson)", ha='right',
          fontsize=style.source_note.size, color=style.source_note.color)

# store figure
fig1.savefig(os.getcwd() + '/examples/example_fig1.png')
plt.close()


# Generate a dual-axes figure
fig2, axes2 = generate_figure(style, num_rows=1, num_cols=2, aspect=0.55,
                              top_margin=0.15, bottom_margin=0.24,
                              left_margin=0.06, space_btwn_axes_x=0.08)

# format axes
format_list(axes2)

# there are only two axes
ax_left = axes2[0][0]
ax_right = axes2[0][1]

# set titles and axis labels
fig2.suptitle("Example #2: Dual-axes figure", color=style.title.color)

ax_left.set_title("Left axes", fontsize=style.subtitle.size, color=style.subtitle.color)
ax_left.set_ylabel("Value A")
ax_left.set_xlabel("Year", labelpad=10)

ax_right.set_title("Right axes", fontsize=style.subtitle.size, color=style.subtitle.color)
ax_right.set_ylabel("Value B")
ax_right.set_xlabel("Year", labelpad=10)

# plot toy data
years = np.arange(2018, 2021)

values_left_grp1 = [np.random.randint(1, 100) for y in years]
values_left_grp2 = [np.random.randint(1, 100) for y in years]
ax_left.bar(years-0.2, values_left_grp1, color=colors.purple.series, width=0.4, label="Group 1", zorder=10)
ax_left.bar(years+0.2, values_left_grp2, color=colors.teal.series, width=0.4, label="Group 2", zorder=10)
ax_left.set_ylim(0, 100)
ax_left.set_xticks(years)

values_right_grp1 = [np.random.randint(1, 50) for y in years]
values_right_grp2 = [np.random.randint(1, 50) for y in years]
ax_right.bar(years-0.2, values_right_grp1, color=colors.purple.series, width=0.4, zorder=10)
ax_right.bar(years+0.2, values_right_grp2, color=colors.teal.series, width=0.4, zorder=10)
ax_right.set_ylim(0, 50)
ax_right.set_xticks(years)

# add legend to left axes only
ax_left.legend(loc='lower left', bbox_to_anchor=(-0.05, -0.36), frameon=False, ncol=2)

# add source note
fig2.text(0.99, 0.01, "Source: vizkarmhutch (Karmen Hutchinson)", ha='right',
          fontsize=style.source_note.size, color=style.source_note.color)

# store figure
fig2.savefig(os.getcwd() + '/examples/example_fig2.png')
plt.close()
