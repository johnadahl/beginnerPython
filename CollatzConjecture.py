#Basic tests I hope to get
#Test to see if a chosen number breaks the collatz conjecture
#add that number to a list of numbers that work
#add all the numbers that were required to show that the first number works to a list 
#(if var(a) is 16, it will go 16, 8, 4, 2, 1. Add all of those numbers to a list)
#With this list, I should be able to make a program that checks to see if a number is part of a list
#So I can quickly 'prove' the collatz conjecture without infinite calculations

print('Try to break the collatz conjecture')
# a = int(input("Type your chosen number: "))
# a = int(input())
#cowbunga = []
#cowbunga.append(a)
quick = []

for i in range(1, 100, 1):
    a = i

    while a != 1:
        if a % 2 == 0:  
                b = a
                a = b / 2
                #cowbunga.append(a)
        else:
            b = a
            a = b * 3 + 1
            #cowbunga.append(a)
    #cowbunga.sort(reverse = False)
    quick.append(a)
print(quick)
