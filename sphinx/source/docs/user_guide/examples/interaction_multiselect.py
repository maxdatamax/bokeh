from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import MultiSelect

multi_select = MultiSelect(title="Option:", value=["foo", "quux"],
                           options=[("foo", "Foo"), ("bar", "BAR"), ("baz", "bAz"), ("quux", "quux")])

show(widgetbox(multi_select))
