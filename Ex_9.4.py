fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

counts = dict()
for line in fh:
    if line.rstrip().startswith("From:"):
        continue
    if line.rstrip().startswith("From"):
        count = count + 1
        address = line.split()[1]
        if address  not in counts:
            counts[address] = 1
        elif address in counts:
            counts[address] = counts[address] + 1

maxNum = 0
maxAddress = None
for key in counts:
    if maxAddress == None or counts[key] > maxNum:
        maxAddress = key
        maxNum = counts[key]
print(maxAddress, maxNum)

