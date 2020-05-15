import numpy as np
import tensorflow as tf


import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon, MultiPolygon
import shapefile

import folium
import os


from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt



import matplotlib.pyplot as plt


import rasterio as rio
from rasterio.plot import show
import rasterio.mask
import fiona

# def bbox(lat,lng, margin):
#     return Polygon([[lng-margin, lat-margin],[lng-margin, lat+margin],
#     [lng+margin,lat+margin],[lng+margin,lat-margin]])
#
# gpd.GeoDataFrame(pd.DataFrame(['p1'], columns = ['geom']),
#      crs = {'init':'epsg:4326'},
#      geometry = [bbox(10,10, 0.25)]).to_file('poly.shp')

import os
import matplotlib.pyplot as plt
from ShapeFileCreator import ShapeFileCreator
# cwd = os.getcwd()


coord_file = "coordinates.csv"
sf_location = "shapefiles/test/sfile"

sfc = ShapeFileCreator()
sfc.create_shapefile(coord_file, sf_location)

# w = shapefile.Writer('shapefiles/test/polygon')
# w.field('name', 'C')
#
# w.poly([
# 	        [[122,37], [117,36], [115,32], [118,20], [113,24]], # poly 1
# 	        [[15,2], [17,6], [22,7]], # hole 1
#          [[122,37], [117,36], [115,32]] # poly 2
#         ])
# w.record('polygon1')
#
# w.close()
# sf = shapefile.Reader("shapefiles/test/polygon.shp")

nReserve = gpd.read_file('shapefiles/test/NaturalReserve_Polygon.shp')
sfPolygon = gpd.read_file(sf_location + ".shp")
# print(nReserve)
# print(type(nReserve))
# print(sf)
# print(type(sf))
# print(sf.shapeType)
# print(sf.shape(0))
# print(sf.shapeRecords())
# rec = sf.shapeRecords()
# for x in sf.shapeRecords():
#     print(x.record[0], x.shape.points[0])
# print(nReserve.crs)
sfPolygon.crs = "EPSG:4326"
# plt.figure()
# for shape in sf.shapeRecords():
#     x = [i[0] for i in shape.shape.points[:]]
#     y = [i[1] for i in shape.shape.points[:]]
#     plt.plot(x,y)
# plt.show()




m = folium.Map([41.7023292727353, 12.34697305914639], zoom_start=11)

folium.GeoJson(sfPolygon).add_to(m)

m.save("map.html")

