import folium
import pandas
# map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

# # map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi, I am a marker", icon=folium.Icon(color='green')))
# for coordinates in [[38.2, -99.1], [39.2, -97,1]]:
#     fg.add_child(folium.Marker(location=coordinates, popup="Hi, I am a marker", icon=folium.Icon(color='green')))
# # fg.add_child(folium.Marker(location=[37.2, -97.1], popup="Hi, I am a marker", icon=folium.Icon(color='green')))
# map.add_child(fg)
# map.save("Map1.html")
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln],
                               popup=str(el) + " m",
                               icon=folium.Icon(color=color_producer(el))))
    # fg.add_child(folium.Marker(location=[lt, ln], radius=6,
    #                            popup=str(el) + " m", fill_color=color_producer(el),
    #                            fill=True, color='grey', fill_opacity=0.7))

# fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
#                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
#                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
map.save("Map1.html")