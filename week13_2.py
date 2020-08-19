import urllib.error, urllib.request, urllib.parse
import json
import ssl

#ssl security 
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE


#retrieve data
url1=input("Enter location : ")
urlHandle=urllib.request.urlopen(url1,context=ctx)
print("Retrieving",url1)
raw_data=urlHandle.read().decode()
print("Retrieved", len(raw_data),"characters")
data=json.loads(raw_data)       #just loaded the JSON
sum=0
count=0

for i in data["comments"]:
    # print(i["count"]) #just debugging
    sum+=i["count"]
    count+=1
print("Count:",count)
print("Sum:",sum)

