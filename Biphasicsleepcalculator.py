#We will have sleep be the 6 hr sleep, and nap be the 30 min sleep.
print("Biphasic sleep is sleeping twice per day instead of once. \nIt allows for less total sleep but the same feeling of being rested.")
#What we want to do is allow someone to say when they want to go to bed, and have the program say the waking time, and the nap time.
print("What time do you want to sleep?")
timeinbed = input()
hourminute = timeinbed.split(':')
hourminute = list(map(int, hourminute))
#This somehow turns all the list items in list hourminute into integers.

bedtime = []

print(hourminute)
def sleepcalc(hourminute):
    #This is where it dies.
    for a in hourminute:
        hourminute[a] += 6
#I still think the comments underneath should work.
#I don't know why they don't.
#    for a in hourminute:
#        hourminute[a] = int(hourminute[a]) + 6
#    bedtime[0] += 6
    print(hourminute)

sleepcalc(hourminute)
