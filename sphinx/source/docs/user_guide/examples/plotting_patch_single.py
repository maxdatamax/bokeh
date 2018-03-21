from bokeh.plotting import figure, show

p = figure(plot_width=400, plot_height=400)

# add a patch renderer with an alpha an line width
p.patch([1, 2, 3, 4, 5], [6, 7, 8, 7, 3], alpha=0.5, line_width=2)

show(p)
