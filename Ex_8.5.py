fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.rstrip().startswith("From:"):
        continue
    if line.rstrip().startswith("From"):
        count = count + 1
        address = line.split()[1]
        print(address)

print("There were", count, "lines in the file with From as the first word")
