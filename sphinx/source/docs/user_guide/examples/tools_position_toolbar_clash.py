from bokeh.plotting import figure, show

# create a new plot with the toolbar below
p = figure(plot_width=400, plot_height=400,
           title=None, toolbar_location="below")

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)
