#This is a caesar cypher decoder.
#I found this at https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
import string

#I need to get a string and shift it. I'm going for a brute force method here.
print('Please Input your phrase to be translated.')
plaintext = str(input())
plaintext = plaintext.lower()
#The lower recieves an arguemtn in the () for what letters should become
#lower. With an empty () meaning all letters.
print('Please input your shift amount.')
#shift = int(input())
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

    print(plaintext.translate(table))

    return plaintext.translate(table)
#caesar(plaintext, shift)

for i in range(1,26):
    caesar(plaintext, i)
