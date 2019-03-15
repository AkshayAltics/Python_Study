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
fg=folium.FeatureGroup(name="Valcanoes")
fg.add_child(folium.Marker(location=[18.499097, 73.828352],popup="HII im Marker",icon=folium.Icon(color="green")))
for lt,ln,add,name in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html % (name,name,add), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt,ln],radius=6, popup=folium.Popup(iframe),fill_color=color_producer(add),color="gray",fill_opacity=0.9))


fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),style_function=lambda x:{'fillColor':'green' if x["properties"]["POP2005"]<10000000 
else 'orange' if 10000000<= x["properties"]["POP2005"]<20000000 else 'red'  if 20000000<= x["properties"]["POP2005"]<50000000 else 'black'}))    





df=pandas.read_csv("f://CodeRepo/demo_c.txt")
print(df)
nom=ArcGIS()



df["Address"]=df["Address"]+","+df["City"]+","+df["State"]+","+df["Country"]
print(df)
'''
#df["Co-ordinates"]=df["Address"].apply(nom.geocode)
print(df["Co-ordinates"])
print(df["Co-ordinates"][0].latitude)
print(df["Co-ordinates"][0].longitude)
df["Latitude"]=df["Co-ordinates"][0].longitude
df["Latitude"]=df["Co-ordinates"].apply(lambda x:x.latitude if x!=None else None)
df["longitude"]=df["Co-ordinates"].apply(lambda x:x.longitude if x!=None else None)
print(df)'''
lat1=list([18.20,18.30,18.40,18.50])
lon1=list([73.10,73.20,73.40,73.50])
address=list(df["Address"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""


fgi=folium.FeatureGroup(name="icon")
for lt,ln,add in zip(lat1,lon1,address):
    iframe1 = folium.IFrame(html=html % str(ln), width=200, height=100)
    fgi.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe1),icon=folium.Icon(color="green")))
map.add_child(fgi)







map.add_child(fgp)
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("Valcanos1.html")
print("DONE")