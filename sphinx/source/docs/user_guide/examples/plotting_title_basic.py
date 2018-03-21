from bokeh.plotting import figure, show

p = figure(title="Basic Title", plot_width=300, plot_height=300)
p.circle([1,2], [3,4])

show(p)
