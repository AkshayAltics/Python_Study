'''
Created on 13-Mar-2019

@author: Admin
'''
import pandas
from geopy.geocoders import ArcGIS
import folium




df=pandas.read_csv("Volcanoes.txt")
lat=list(df["LAT"])
lon=list(df["LON"])
elev=list(df["ELEV"])
name=list(df["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def color_producer(elevation):
    if elevation <1000:
        return "green"
    elif 1000 <= elevation < 3000:  
        return "blue"
    else:
        return "red" 
   


map=folium.Map
map=folium.Map(location=[38.59, -99.82],zoom_start=6,tiles="Mapbox Bright")
map.save("Valcanos1.html")
fg=folium.FeatureGroup(name="mu map")
for lt,ln,add,name in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html % (name,name,add), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color=color_producer(add))))
map.add_child(fg)
map.save("Valcanos1.html")
print("DONE")