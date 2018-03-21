from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import TextInput

text_input = TextInput(value="default", title="Label:")

show(widgetbox(text_input))
