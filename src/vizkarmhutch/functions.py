import matplotlib.pyplot as plt

from vizkarmhutch.style import Style


def format_axes(ax: plt.Axes, keep_spine: str = "bottom"):
    """
    Make spines on the given Axes object invisible. It's most common 
    to keep the bottom spine, but user has flexibility to determine 
    which spine remains visible.

    :param ax: the Axes object
    :param keep_spine: spine to keep visible (e.g. 'top', 'bottom', 'left', 'right')
    :return: None. Axes object modified in place.
    """
    spines = ['top', 'bottom', 'left', 'right']
    spines.remove(keep_spine)
    for s in spines:
        ax.spines[s].set_visible(False)
    
    
def format_axis(ax: plt.Axes, axis: str = 'y', hide: bool = False):
    """
    Formats the x- or y-axis of an Axes object. If not removing the axis
    completely, then gridlines are added and the tick marks are hidden.

    :param ax: the Axes object
    :param axis: the axis to format; either 'x' or 'y'
    :param hide: determines whether to hide the axis completely
    :return: None. Axes object modified in place.
    """
    axis_to_format = ax.yaxis if axis == 'y' else ax.xaxis
    
    if hide: 
        # remove axis completely
        axis_to_format.set_visible(False)
        
    else:
        # add gridlines
        axis_to_format.grid(True, zorder=0)
        # hide tick marks
        ax.tick_params(axis=axis, which='major', length=0)


# function to generate figure
def generate_figure(style: Style,
                    left_margin: float = 0.04,
                    right_margin: float = 0.01,
                    top_margin: float = 0.07,
                    bottom_margin: float = 0.20,
                    num_rows: int = 2,
                    num_cols: int = 2,
                    space_btwn_axes_x: float = 0.05,
                    space_btwn_axes_y: float = 0.15,
                    aspect: float = 1.0):
    """
    Generate a Figure that has the specified margins, aspect ratio, and number of Axes.

    :param style: Style object with a fig_width_inches parameter
    :param left_margin: size of left margin (as a share of the Figure)
    :param right_margin: size of right margin (as a share of the Figure)
    :param top_margin: size of top margin (as a share of the Figure)
    :param bottom_margin: size of bottom margin (as a share of the Figure)
    :param num_rows: number of Axes along y-axis (e.g. 2 means there are 2 rows in each column)
    :param num_cols: number of Axes along x-axis (e.g. 2 means there are 2 columns in each row)
    :param space_btwn_axes_x: space between columns (as a share of the Figure)
    :param space_btwn_axes_y: space between rows (as a share of the Figure)
    :param aspect: ratio of figure height to figure width
    :return: (plt.Figure, list of plt.Axes)
    """
    # define width and height of all Axes combined
    total_width = 1 - left_margin - right_margin
    total_height = 1 - top_margin - bottom_margin
    
    # define width and height of each individual Axes
    gap_space_x = (num_cols - 1) * space_btwn_axes_x
    axes_width = (total_width - gap_space_x) / num_cols
    
    gap_space_y = (num_rows - 1) * space_btwn_axes_y
    axes_height = (total_height - gap_space_y) / num_rows
    
    # generate figure with target width and given aspect ratio
    fig = plt.figure(figsize=(style.fig_width_inches, style.fig_width_inches * aspect))
    
    # add all Axes to figure 
    axes = []  # convert this to a matrix for easier use later
    init_bottom = bottom_margin
    for _ in range(num_rows):
        
        current_row = []
        init_left = left_margin
        for _ in range(num_cols):
            
            ax = fig.add_axes((init_left, init_bottom, axes_width, axes_height))
            current_row.append(ax)
            init_left += (axes_width + space_btwn_axes_x)
            
        axes.insert(0, current_row)
        init_bottom += (axes_height + space_btwn_axes_y)
        
    # return figure and list of axes
    return fig, axes
