from matplotlib.pyplot import rcParams


# -----------------------------------------------------------------------------

class TextElement(object):

    # each text element has a name, font size, font weight, and color
    def __init__(self, name: str, size: int, weight: str, color: str):
        self.name = name
        self.size = size
        self.weight = weight
        self.color = color


# define font sizes of text elements
class FontSize(object):

    # it may be necessary to scale the figures/text to 
    # different mediums (e.g. web pages, pdf, or ppt)
    def __init__(self, medium: str):

        # require that the medium is within a specific set
        assert medium in ('web', 'pdf')

        # define dictionaries of font sizes for each medium
        web_size = dict(
            title=22, subtitle=18, axis_label=16, tick_label=14, data_label=16,
            callout=14, legend_label=14, figure_note=12, source_note=10
        )
        pdf_size = dict(
            title=8, subtitle=7, axis_label=7, tick_label=7, data_label=10,
            callout=7, legend_label=7, figure_note=7, source_note=5
        )

        # set font size attributes based on medium
        # Note: the following requires >= Python v3.10
        match medium:
            case 'web':
                use_dict = web_size
            case 'pdf':
                use_dict = pdf_size

        for element, fontsize in use_dict.items():
            setattr(self, element, fontsize)

    def items(self):
        return vars(self).items()


# define weights of text elements
class FontWeight(object):

    def __init__(self):

        norm_elements = ("subtitle", "data_label", "callout", "legend_label",
                         "figure_note", "source_note")
        for element in norm_elements:
            setattr(self, element, "normal")

        bold_elements = ("title", "axis_label", "tick_label")
        for element in bold_elements:
            setattr(self, element, "bold")

    def get_weight(element: str):
        return getattr(FontWeight(), element)


# define colors of text elements
class FontColor(object):

    # all elements are set to either dark or light gray
    def __init__(self):

        dark_gray = "#333333"
        dark_gray_elements = ("title", "axis_label", "tick_label",
                              "data_label", "callout", "legend_label",
                              "figure_note")
        for element in dark_gray_elements:
            setattr(self, element, dark_gray)

        light_gray = "#565656"
        light_gray_elements = ("subtitle", "source_note")
        for element in light_gray_elements:
            setattr(self, element, light_gray)

    def get_color(element: str):
        return getattr(FontColor(), element)


# define specs for text elements
class FontSpecs(object):

    # zip text attributes into a single object
    def __init__(self, medium: str):
        # require that the medium is within a specific set
        assert medium in ('web', 'pdf')

        # initialize visualization elements
        self.title: TextElement
        self.subtitle: TextElement
        self.axis_label: TextElement
        self.tick_label: TextElement
        self.data_label: TextElement
        self.callout: TextElement
        self.legend_label: TextElement
        self.figure_note: TextElement
        self.source_note: TextElement

        for element, size in FontSize(medium).items():
            weight: str = FontWeight.get_weight(element)
            color: str = FontColor.get_color(element)
            specs = TextElement(element, size, weight, color)
            setattr(self, element, specs)


# define object used to automate styling
class Style(FontSpecs):

    def __init__(self, medium: str):
        super().__init__(medium)

        self.medium = medium
        self.font_name = "Times"
        self.fig_width_pixels = 2140
        self.fig_width_inches = self.fig_width_pixels / rcParams['figure.dpi']

    @property
    def params(self) -> dict:
        rcparams = {
            # set font 
            'font.sans-serif': self.font_name,

            # set grid specs
            'grid.color': "#d4d2d2",

            # set title specs
            'figure.titlesize': self.title.size,
            'figure.titleweight': self.title.weight,
            # Note: user must manually set title color if using plt.suptitle()
            'axes.titlesize': self.title.size,
            'axes.titleweight': self.title.weight,
            'axes.titlecolor': self.title.color,

            # set label specs
            'axes.labelsize': self.axis_label.size,
            'axes.labelweight': self.axis_label.weight,
            'axes.labelcolor': self.axis_label.color,
            'xtick.labelsize': self.tick_label.size,
            'xtick.labelcolor': self.tick_label.color,
            'ytick.labelsize': self.tick_label.size,
            'ytick.labelcolor': self.tick_label.color,

            # set legend specs
            'legend.fontsize': self.legend_label.size,
            'legend.labelcolor': self.legend_label.color,
        }

        return rcparams


# -----------------------------------------------------------------------------

class Color(object):

    def __init__(self, name: str, series: str, label: str):
        self.name = name
        self.series = series
        self.label = label

    def __repr__(self):
        return f"Color(name={self.name}, series={self.series}, label={self.label}"


class ColorSet(object):

    def __init__(self):
        self.color_names = []

    def _add_to_names(self, new_colors):
        existing_colors = self.color_names
        updated_colors = set().union(*[new_colors, existing_colors])
        self.color_names = updated_colors

    def __repr__(self):
        return "ColorSet(" + ", ".join(self.color_names) + ")"


class MainColors(ColorSet):
    teal = Color("teal", "#a2dadb", "#567a78")
    orange = Color("orange", "#ffae5f", "#b24d28")
    purple = Color("purple", "#8782ba", "4f465e")
    yellow = Color("yellow", "#ffe18b", "#8a732b")

    def __init__(self):
        super().__init__()
        main_color_names = ["teal", "orange", "purple", "yellow"]
        self._add_to_names(main_color_names)


class SpecialtyColors(ColorSet):
    dark_gray = aggregate = Color("dark_gray", "#333333", "#333333")
    green = positive_growth = Color("green", "#bbd976", "#6b7f2b")
    red = negative_growth = Color("red", "#c84933", "#80171a")

    def __init__(self):
        super().__init__()
        specialty_color_names = ["dark_gray", "green", "red"]
        self._add_to_names(specialty_color_names)


class AllColors(MainColors, SpecialtyColors):

    def __init__(self):
        MainColors.__init__(self)
        SpecialtyColors.__init__(self)
