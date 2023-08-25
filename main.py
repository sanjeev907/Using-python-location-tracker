import phonenumbers
import opencage
import folium
from myphone import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode





pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
service_provider = phonenumbers.parse(number)
print(location)
print(carrier.name_for_number(service_provider,'en'))



key  = '42159f09dd544fb281677f30a743a4fd'
geocoder = OpenCageGeocode(key)

query = str(location)
result = geocoder.geocode(query)
# print(result)

# 'lng': "78° 40' 3.87408'

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

mymap = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(mymap)
mymap.save("mylocation.html")