import json
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    info = json.loads(data)
    # print(info)
    # print('User count:', len(info))
    # print(info["comments"])

    nums = list()
    for item in info["comments"]:
        # print('Name :', item["name"])
        # print('Count :', item["count"])
        nums.append(int(item["count"]))
    sum = 0
    for num in nums:
        sum = sum + num

    print(sum)