counts = {}
copyPasta = "The FitnessGram Pacer test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter Pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal *boop*. A single lap should be completed each time you hear this sound *ding*. Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start."
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
#tmp = sorted(tmp, reverse = True)
#So this turns tmp into a list instead of a dictionary like I wanted it to be. That is why it only printed out some of the data, that data being the key.
tmp = tmp.sort()


print(tmp)
#I don't know why this doesn't print both the value and the key. It is only printing the key which is an integer. Super annoying.
#Now I just need to make it get sorted and then pring only the first x number of words.

for (k, v) in tmp.items():
    print(v, k)


#for i in tmp:
#    print(i, tmp[i])



















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
