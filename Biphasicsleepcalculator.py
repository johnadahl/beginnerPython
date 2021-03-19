#We will have sleep be the 6 hr sleep, and nap be the 30 min sleep.
print("Biphasic sleep is sleeping twice per day instead of once. \nIt allows for less total sleep but the same feeling of being rested.")
#What we want to do is allow someone to say when they want to go to bed, and have the program say the waking time, and the nap time.
print("What time do you want to sleep?")
timeinbed = '12:12'
#I'll return this to an input later. I can keep it at a chosen number
#That would break the program so I can ensure it works without typing
#An input all day.
hourminute = timeinbed.split(':')
hourminute = list(map(int, hourminute))
#This somehow turns all the list items in list hourminute into integers.

bedtime = []

print(hourminute)
def sleepcalc(hourminute):
    #This is where it dies.
    hourminute[0] += 6
    if hourminute[1] < 15:
        hourminute[0] -= 1
        hourminute[1] = 60 + (hourminute[1] - 15)
    else:
        hourminute[1] -= 15
    if hourminute[0] > 12:
        hourminute[0] -= 12
    else:
        return
#I still think the comments underneath should work.
#I don't know why they don't.
#    for a in hourminute:
#        hourminute[a] = int(hourminute[a]) + 6
#    bedtime[0] += 6
    print(hourminute)

sleepcalc(hourminute)
