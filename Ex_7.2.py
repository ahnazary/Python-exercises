fname = input("enter the file name")
try:
    fhandle = open(fname, 'r')
except:
    print("File not found")
    quit()
total = 0.0
count = 0
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.rfind(" ")
        num = float(line[pos+1:len(line)])
        total += num
        count = count + 1
print("Average spam confidence:", total/count)
