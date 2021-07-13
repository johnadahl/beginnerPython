counts = {}
copyPasta = input('Please input your copy pasta. \n')
wordsOfCopyPasta = copyPasta.split()

for word in wordsOfCopyPasta:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

tmp = {}

for (k,v) in counts:
    






















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
