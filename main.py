import folium
import pandas

data_count_disc= pandas.read_csv("countries of the world.csv")
data_capital= pandas.read_csv("concap.csv")

data_count_disc['Country'] = data_count_disc['Country'].str.replace(" ","")

df4 = pandas.merge(data_count_disc, data_capital, on = 'Country')
df4.to_csv('CSV4.csv')

cap = list(df4["Country"])
lat = list(df4["CapitalLatitude"])
lon = list(df4["CapitalLongitude"])
place = zip(lat,lon,cap)

map = folium.Map(location=[48.2,16.366667],zoom_start=5, tiles='cartodbdark_matter', overlay=False, name="lol")

fgc = folium.FeatureGroup(name="Countries", overlay=True)

for lat, lon,con in place:
    fgc.add_child(folium.CircleMarker(location=[lat,lon], radius = 10,popup=con, fill_color='red', color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population", overlay=True)

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange ' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))

fga = folium.FeatureGroup(name="Area", overlay=True)

fga.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['AREA']<10000
else 'orange ' if 10000<=x['properties']['AREA']<50000 else 'red'}))


map.add_child(fgc)
map.add_child(fgp)
map.add_child(fga)
map.add_child(folium.LayerControl())

map.save("New_Map1.html")


