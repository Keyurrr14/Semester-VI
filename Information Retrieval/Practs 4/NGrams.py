string = "I love Natural Language Processing"
splitString = string.split()
nGram = 4
res = []

for i in range(len(splitString)):
    sliced = splitString[i:i+nGram]
    if len(sliced) < nGram:
        break
    res.append(sliced)

print(res)
