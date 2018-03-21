from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Button

button = Button(label="Foo", button_type="success")

show(widgetbox(button))
