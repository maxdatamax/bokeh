from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import CheckboxButtonGroup

checkbox_button_group = CheckboxButtonGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])

show(widgetbox(checkbox_button_group))
