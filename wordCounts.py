count = dict() 
words = input('Paste your copy pasta. \n')

wordsaslist = words.split()

for word in wordsaslist:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(max)

