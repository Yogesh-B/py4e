import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

name=input("Enter url - ")
data=urllib.request.urlopen(name,context=ctx).read()
tree = ET.fromstring(data)

counts=tree.findall('.//count')
sum=0
for count in counts:
    sum+=float(count.text)
print("sum = ",sum)