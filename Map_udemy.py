'''
Created on 13-Mar-2019

@author: Admin
'''
import pandas
from geopy.geocoders import ArcGIS
import folium




df=pandas.read_csv("f://CodeRepo/demo_c.txt")
print(df)
nom=ArcGIS()
print(nom.geocode("akluj,Malshiras,Maharshtra "))
n=nom.geocode("akluj,Malshiras,Maharshtra ")
print(n)
nlat=n.latitude
nlong=n.longitude
print(nlat,nlong)

df["Address"]=df["Address"]+","+df["City"]+","+df["State"]+","+df["Country"]
print(df)
df["Co-ordinates"]=df["Address"].apply(nom.geocode)
print(df["Co-ordinates"])
print(df["Co-ordinates"][0].latitude)
print(df["Co-ordinates"][0].longitude)
df["Latitude"]=df["Co-ordinates"][0].longitude
df["Latitude"]=df["Co-ordinates"].apply(lambda x:x.latitude if x!=None else None)
df["longitude"]=df["Co-ordinates"].apply(lambda x:x.longitude if x!=None else None)
print(df)
lat1=list(df["Latitude"])
lon1=list(df["longitude"])
address=list(df["Address"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

map=folium.Map
map=folium.Map(location=[18.499097, 73.828352],zoom_start=6)

fg=folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location=[18.499097, 73.828352],popup="HII im Marker",icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("map1.html")

for lt,ln,add in zip(lat1,lon1,address):
    iframe = folium.IFrame(html=html % str(add), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe),icon=folium.Icon(color="green")))
map.add_child(fg)
map.save("map2.html")
print("DONE")
