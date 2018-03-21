from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import RadioGroup

radio_group = RadioGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=0)

show(widgetbox(radio_group))
