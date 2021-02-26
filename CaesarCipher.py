#This is a caesar cypher decoder.
#I found this at https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python

#I need to get a string and shift it. I'm going for a brute force method here.
def caesar(text, shift):
    #We need to take the text as an argument,
    #and the letter shift as anothe argument.
    alphabet = string.ascii_lowercase
    #make it all lowercase.
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    #the [shift:] means shift and everything after the shift,
    #and [:shift is everything before the shift.]
    #I'm going to make another project that uses this later.
