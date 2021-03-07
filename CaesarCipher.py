#This is a caesar cypher decoder.
#I found this at https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
import string
codes = []
#Make an empty list to append all the possible solutions for
#I need to get a string and shift it. I'm going for a brute force method here.
print('Please Input your phrase to be translated.')
plaintext = str(input())
plaintext = plaintext.lower()
#The lower recieves an arguemtn in the () for what letters should become
#lower. With an empty () meaning all letters.
#print('Please input your shift amount.')
#shift = int(input())
commonwords = ['the', 'of', 'to', 'and', 'in', 'is', 'it,' 'you', 'that', 'he', 'was', 'for', 'on', 'are']
def caesar(plaintext, shift):
    #We need to take the text as an argument,
    #and the letter shift as anothe argument.
    alphabet = string.ascii_lowercase
    #make it all lowercase.
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    #the [shift:] means shift and everything after the shift,
    #and [:shift is everything before the shift, but excluding the shift]
    #I'm going to make another project that uses this later.
    table = str.maketrans(alphabet, shifted_alphabet)

#    print(plaintext.translate(table))


    codes.append(plaintext.translate(table))
    return plaintext.translate(table)

#caesar(plaintext, shift)
print('below are the possible cyphers.')
print()
for i in range(1,26):
    caesar(plaintext, i)

for x in codes:
    print(x)
#so what I want to do now is create a dictoinary or list or array
#I'm not sure which yet, and populate it with all the strings
#Cretaed by the caesar cipher.
#At that point, I sort each list based on which string has the
#most letters e to the least.
#I then print all the strings from most likely to least.
