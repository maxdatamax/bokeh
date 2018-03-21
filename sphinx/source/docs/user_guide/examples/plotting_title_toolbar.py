from bokeh.plotting import figure, show

p = figure(title="Top Title with Toolbar", toolbar_location="above",
           plot_width=600, plot_height=300)
p.circle([1,2], [3,4])

show(p)
