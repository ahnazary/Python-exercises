import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1: quit()

parms = dict()
parms['address'] = address
url = address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')
numbers = list()
for item in counts:
    # print(item.text)
    numbers.append(int(item.text))
    # print(numbers)

sum = 0
for num in numbers:
    sum = sum + num

print(sum)