import re

handle = open("text")
sum = 0;
count = 0;
for line in handle:
    res = re.findall('([0-9]+)',line)
    print(res)
    for temp in res:
        sum = sum + int(temp)
print(count, sum)