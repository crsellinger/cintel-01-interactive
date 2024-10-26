#Caleb Sellinger
#44630 Module 1
#Dr. Case
#10-25-2024

"""
Look at this Histogram! Wow!
"""

import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
from shinyswatch import theme

#Page options, specifically the title
ui.page_opts(title="Big TITLE, Very Shiny",theme = theme.quartz,fillable=True)

#slider
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 186, 75)


#histogram chart

#decorator to render chart
@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    #function to create plot
    plt.hist(x, input.selected_number_of_bins(), color="cyan",density=True,edgecolor="blue")
