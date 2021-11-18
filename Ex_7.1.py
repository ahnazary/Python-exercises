fname = input("enter the file name")
try:
    fhandle = open(fname, 'r')
except:
    print("File not found")
    quit()
for line in fhandle:
    print(line.strip().upper())