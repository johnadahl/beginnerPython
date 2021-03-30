#Basic tests I hope to get
#Test to see if a chosen number breaks the collatz conjecture
#add that number to a list of numbers that work
#add all the numbers that were required to show that the first number works to a list 
#(if var(a) is 16, it will go 16, 8, 4, 2, 1. Add all of those numbers to a list)
#With this list, I should be able to make a program that checks to see if a number is part of a list
#So I can quickly 'prove' the collatz conjecture without infinite calculations
import time

print('This runs the collatz conjecture for everynumber from 1 to 1000000.')

quick = []
#Make a list for every number that works
#time.sleep(3)

for i in range(1, 1000001, 1):
    a = i
    if a in quick:
            a = 1
    else:                 
        c = i
        while a != 1:
                if a % 2 == 0:  
                        b = a
                        a = b / 2
                else:
                        b = a
                        a = b * 3 + 1
        quick.append(c)
print(quick)
