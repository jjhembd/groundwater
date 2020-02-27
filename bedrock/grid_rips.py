import pandas
import numpy
import web_mercator
import gaussian_interp
import webmerc_tif

rips = pandas.read_csv('data/lonlatrip_0-20_t2.csv')

# Project to Web Mercator
xyv = pandas.DataFrame({
    'x': rips['LONGITUDE'].map(web_mercator.lon_to_x),
    'y': rips['LATITUDE'].map(web_mercator.lat_to_y),
    'val': rips['RIPPABILITY']
    })

# Set up grids in x and y
dg = 2000 # meters. Will be adjusted to pixel spacing in nearest zoom level
tilesize = 1024 # pixels
x = web_mercator.get_tilegrid(xyv.x.min(), xyv.x.max(), dg, tilesize)
y = web_mercator.get_tilegrid(xyv.y.min(), xyv.y.max(), dg, tilesize)

kernel_radius = 3600 # meters
values, sampling = gaussian_interp.grid_data(xyv, x, y, kernel_radius)

vals32bit = values.astype(numpy.float32)

webmerc_tif.write('data/rippability_0-20_t5.tif', x, y, vals32bit)
