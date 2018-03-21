from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Toggle

toggle = Toggle(label="Foo", button_type="success")

show(widgetbox(toggle))
