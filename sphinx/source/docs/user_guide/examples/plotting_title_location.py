from bokeh.plotting import figure, show

p = figure(title="Left Title", title_location="left",
           plot_width=300, plot_height=300)
p.circle([1,2], [3,4])

show(p)
