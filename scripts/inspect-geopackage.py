import geopandas as gpd
from pathlib import Path

gpkg_path = Path(r"C:\Users\YouEffOhh\Desktop\OTF Marine\Marine.gpkg")
print(gpkg_path.exists())

layers = gpd.list_layers(gpkg_path)
print(layers)


waypoint = gpd.read_file(gpkg_path, layer="fishing_waypoints")
print(waypoint.head())
print(waypoint.crs)
print(waypoint.geometry)