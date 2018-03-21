from bokeh.io import show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
from bokeh.sampledata.sample_geojson import geojson

geo_source = GeoJSONDataSource(geojson=geojson)

p = figure(background_fill_color="lightgrey")
p.circle(x='x', y='y', size=15, alpha=0.7, source=geo_source)

show(p)
