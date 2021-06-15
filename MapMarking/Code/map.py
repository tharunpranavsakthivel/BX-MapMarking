import folium as fm
import pandas as pd



data_v = pd.read_csv('D:/IP PROJECT/Maps/Code/Volcanoes.txt')
data_m = pd.read_csv('D:/IP PROJECT/Maps/Code/Data.csv')
data_m=data_m.dropna(subset=['longitude'])

data_m=data_m.dropna(subset=['latitude'])

lat_v = list(data_v['LAT'])
lon_v = list(data_v['LON'])
elev_v = list(data_v['ELEV'])
lat_m = list(data_m['latitude'])
lon_m = list(data_m['longitude'])
det_m = list(data_m['commodity'])


maps = fm.Map(location=[45.372, -121.6972], zoom_start=12, tiles="OpenStreetMap")

def color(x):
    x = x.lower()
    if x == "nickel":
        return 'grey'
    elif x == "iron":
        return 'red'
    elif x == "aluminium":
        return 'White'
    elif x == "copper":
        return 'Gold'
    elif x == "lead":
        return 'green'
    elif x == "zinc":
        return 'green'
    elif x == "pge":
        return 'blue'
    elif x == "gold":
        return 'yellow'
    elif x == "rare earth elements":
        return 'purple'
    elif x == "diamond":
        return 'pink'
    elif x == "clays":
        return '#ffff99'
    elif x == "potash":
        return '#b3ff99'
    else:
        return 'Cyan'
    
fgm = fm.FeatureGroup(name='Minerals')
for lt, ln, dt in zip(lat_m, lon_m, det_m):
    fgm.add_child(fm.CircleMarker([lt,ln],radius=6, popup=str(dt), fill_color=color(dt), color='grey', fill_opacity=1))


fgv =fm.FeatureGroup(name='Volcanoes') 

for lt, ln, el in zip(lat_v, lon_v, elev_v):
    fgv.add_child(fm.CircleMarker([lt,ln], radius=6, popup=str(el)+'m Volcano', fill_color='red', color='black', fill_opacity=0.7))

fgp = fm.FeatureGroup(name='Population')
fgp.add_child(fm.GeoJson(open('D:/IP PROJECT/Maps/Code/world.json', 'r', encoding="utf-8-sig").read(), style_function=lambda x:{'fillColor': 'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000<= x['properties']['POP2005']<20000000 else 'red'}))


maps.add_child(fgv)
maps.add_child(fgp)
maps.add_child(fgm)
fm.LayerControl().add_to(maps)
maps.save('D:/IP PROJECT/Maps/maps.html')

