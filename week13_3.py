import urllib.error, urllib.parse, urllib.request
import ssl 
import json

api_key = False
# url1="https://maps.googleapis.com/maps/api/geocode/json?"
# API_key="AIzaSyCc-FiNMEM2mxjI_4HUyswRqUvgIce69G8"  #API key has been changed after completing assignment
if api_key is False:
    api_key = 42
    url1 = 'http://py4e-data.dr-chuck.net/json?'
else :
    url1 = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


location=input("Enter location: ")
if(len(location)<1):
    print("invalid input!!!!")
    exit()
final_url=url1+urllib.parse.urlencode({'address':location,'key':api_key})
print("Retrieving:",final_url)
data=urllib.request.urlopen(final_url).read().decode()
json1=json.loads(data)
# if 'status' not in data or 'status'!="OK":
#     print("Something went wrong while receiving...!!!")
# else:
print("Retrieved",len(data), "characters")
print("Place id",json1["results"][0]["place_id"])

a=[{'address_components': [{'long_name': '103', 'short_name': '103', 'types': ['street_number']}, {'long_name': 'Hillcrest Road', 'short_name': 'Hillcrest Rd', 'types': ['route']}, {'long_name': 'Westhill', 'short_name': 'Westhill', 'types': ['neighborhood', 'political']}, {'long_name': 'Mobile', 'short_name': 'Mobile', 'types': ['locality', 'political']}, {'long_name': 'Mobile County', 'short_name': 'Mobile County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Alabama', 'short_name': 'AL', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '36608', 'short_name': '36608', 'types': ['postal_code']}, {'long_name': '5306', 'short_name': '5306', 'types': ['postal_code_suffix']}], 'formatted_address': '103 Hillcrest Rd, Mobile, AL 36608, USA', 'geometry': {'location': {'lat': 30.688114, 'lng': -88.19016219999999}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 30.68946298029149, 'lng': -88.18881321970848}, 'southwest': {'lat': 30.6867650197085, 'lng': -88.19151118029149}}}, 'place_id': 'ChIJy0Uc1Zmym4gR3fmAYmWNuac', 'plus_code': {'compound_code': 'MRQ5+6W Mobile, AL, USA', 'global_code': '862HMRQ5+6W'}, 'types': ['atm', 'establishment', 'finance', 'point_of_interest']}]