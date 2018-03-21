from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Slider

slider = Slider(start=0, end=10, value=1, step=.1, title="Stuff")

show(widgetbox(slider))
