counts = {}
copyPasta = input('Please input your copy pasta. \n')
wordsOfCopyPasta = copyPasta.split()

for word in wordsOfCopyPasta:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

tmp = {}

#print(counts)
#This proves that the program works until line 13 perfectly how I want it to.

#This takes all the items in counts and rearanges them so the number is first. That way it can be sorted.
for (k,v) in counts.items():
    tmp[v] = k

print(tmp)
#This shows that the program works perfectly to the line above.
tmp = sorted(tmp, reverse = True)

print(tmp)
#I don't know why this doesn't print both the value and the key. It is only printing the key which is an integer. Super annoying.
#Now I just need to make it get sorted and then pring only the first x number of words.

for i in tmp():
    print(i, tmp[i])



















#count = dict()
#words = input('Paste your copy pasta. \n')

#wordsaslist = words.split()

#for word in wordsaslist:
#    if word in count:
#        count[word] += 1
#    else:
#        count[word] = 1


# print(count)
#for word in count:
#    if count[word] > 10:
#        print(count)
#    else:
#        continue


#chunk = {}
#for (word, number) in count:
#    chunk.append(number, word)
#print(chunk.sort(reverse = True))
