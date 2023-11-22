from pyproj import Transformer
import pyproj

lv95 ="EPSG:2056"
wgs84="EPSG:4326"

t1=Transformer.from_crs(wgs84,lv95)
t2=Transformer.from_crs(lv95,wgs84)

r1=t1.transform(47.53465751021417, 7.642289825877619)

print(r1)

r2=t2.transform(2615335.8573330143, 1264900.605952826)
print(r2)

start_lng=7.642289825877619
start_lat=47.53465751021417
end_lng=139.77070202953962
end_lat=35.68502755374897

g=pyproj.Geod(ellps="WGS84")

r=g.npts(start_lng,start_lat,end_lng,end_lat,2000)
r2=[]
for x in r:
    r2.append([x[0],x[1]])
    

all=list([[start_lng,start_lat]]+r2+[[end_lng,end_lat]])

geojson= f"""
{{
    "type": "Feature",
    "geometry": {{
        "type": "LineString",
        "coordinates":{all}
}}}}
"""

print(geojson)