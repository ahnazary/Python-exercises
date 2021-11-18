name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

d = dict()
for line in handle:
    if line.startswith("From:"):
        continue
    if line.startswith("From"):
        first = line.split(':')[0]
        temp = first.split()
        hour = temp[len(temp) - 1]
        d[hour] = d.get(hour, 0) + 1

finalList = list()
for k, v in d.items():
    newTup = (k,v)
    finalList.append(newTup)

sorted = sorted(finalList)

for k, v in sorted:
    print(k, v)