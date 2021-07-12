count = dict()
words = input('Paste your copy pasta. \n')

wordsaslist = words.split()

for word in wordsaslist:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
# print(count)
#for word in count:
#    if count[word] > 10:
#        print(count)
#    else:
#        continue
chunk = {}
for (word, number) in count:
    chunk.append(number: word)
print(chunk.sort(reversed = True))
