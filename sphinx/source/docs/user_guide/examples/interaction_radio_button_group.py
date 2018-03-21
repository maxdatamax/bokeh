from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import RadioButtonGroup

radio_button_group = RadioButtonGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=0)

show(widgetbox(radio_button_group))
