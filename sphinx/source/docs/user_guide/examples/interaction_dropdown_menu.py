from bokeh.io import show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Dropdown

menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]
dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)

show(widgetbox(dropdown))
