from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


def func(url, count, pos):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    posIt = 0;

    for tag in tags:
        posIt = posIt + 1
        if posIt == pos:
            # Look at the parts of a tag
            # print('TAG:', tag)
            # print('URL:', tag.get('href', None))
            # print('Contents:', tag.contents[0])
            # print('Attrs:', tag.attrs)
            return tag.get('href', None)


url = input('Enter - ')
count = int(input('Enter count: '))
pos = int(input('Enter Position: '))

print('Retrieving : ', url)
for x in range(0, count):
    print('Retrieving : ', func(url, count, pos))
    url = func(url, count, pos)
