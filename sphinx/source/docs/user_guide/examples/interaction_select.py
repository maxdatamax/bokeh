from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select

select = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])

show(widgetbox(select))
