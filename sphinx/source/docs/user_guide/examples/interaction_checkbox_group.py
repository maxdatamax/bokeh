from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import CheckboxGroup

checkbox_group = CheckboxGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])

show(widgetbox(checkbox_group))
