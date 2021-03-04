#This is a caesar cypher decoder.
#I found this at https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python

#I need to get a string and shift it. I'm going for a brute force method here.
print('Please Input your phrase to be translated.')
plaintext = str(input())
print('Please input your shift amount.')
shift = int(input())
def caesar(plaintext, shift):
    #We need to take the text as an argument,
    #and the letter shift as anothe argument.
    alphabet = str.lower
    #make it all lowercase.
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    #the [shift:] means shift and everything after the shift,
    #and [:shift is everything before the shift, but excluding the shift]
    #I'm going to make another project that uses this later.
    table = str.maketrans(alphabet, shifted_alphabet)

    return plaintext.translate(table)
    print(plaintext.translate(table))
caesar(plaintext, shift)
