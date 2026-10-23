import geopandas as gpd
from pathlib import Path
from pyproj import Geod 

geod = Geod(ellps="WGS84")

gpkg_path = Path(r"C:\Users\YouEffOhh\Desktop\OTF Marine\Marine.gpkg")
print(gpkg_path.exists())

'''layers = gpd.list_layers(gpkg_path)
print(layers)


waypoint = gpd.read_file(gpkg_path, layer="fishing_waypoints")
print(waypoint.head())
print(waypoint.crs)
print(waypoint.geometry)'''



routes = gpd.read_file(gpkg_path, layer="route")
print(routes.head())
print(routes.crs)

route_geometry = routes.geometry.iloc[0] 

coordinates = list(route_geometry.coords) 
total_distance = 0 



for start, end in zip(coordinates[:-1], coordinates[1:]):
    lon1, lat1 = start
    lon2, lat2 = end
    azimuth1, azimuth2, distance = geod.inv(lon1, lat1, lon2, lat2)
    total_distance += distance
    
print("Segment distance:", distance, "meters")
nautical_miles = total_distance / 1852

print("Total route distance:", nautical_miles, "NM")