fname = input("Enter file name: ")
fh = open(fname)
lst = list()


totalWords = []
for line in fh:
    # print(line.rstrip())
    words = line.split()
    for word in words:
        # print(word)
        totalWords.append(word)

def isPresent (input, words):
    for word in words:
        if word == input:
            return 'true'
            break
    return "false"

nonRepeated = []
# print(totalWords)
for word in totalWords:
    if isPresent(word, nonRepeated) == "false":
        nonRepeated.append(word)

# print(nonRepeated)
sorted = sorted(nonRepeated)
print(sorted)