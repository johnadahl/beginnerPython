#take a string input
#Split it into words(where there is a space)
#take an arbitrary number of letters 
#Bowman's page https://github.com/shortbird/CP3/blob/main/projects/strand_one/pig_latin.md
#Further Rules can be found there

#piglatin = (input('Please input your string: ')
            #Strings aren't callable, and I don;'t understand what that means.
def main():
    lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl', ]
    #I think that is just taking all the most common constaning strings in the start of a word.
    #like ship, gloat, chirp, phart, tribe, bloat, great, steal, sleep, clap, please, flood
    piglatin = input('Please input your sentence: ')
    #I don't yet understand why this isn't a string.
    piglatin = piglatin.split()
    #this splits the piglatin every time there is a space. Turns it into a list.
    for k in range(len(piglatin)):
        #This will check through every list item, or word because we split it up above.
        i = piglatin[k]
        #Now we go through every list item without changing the original piglatin
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            #If the first letter of each word, or firts part of each list is a vowel
            piglatin[k] = i+'ay'
            #We just add 'ay' to the word.
        elif t(i) in lst:
            #So I think this is checking to see if the start of each word is a consanant string.
            #we have t(str) below.
                    piglatin[k] = i[2:]+i[:2]+'ay'
                    #This takes from the 2nd (Tehcnially the thrid. Lists start at 0) and above, and adds it from 0 to 2 with the two being exluded.
                    #https://docs.python.org/3/tutorial/introduction.html About half way down the page here.
        elif i.isalpha() == False:
            # .isalpha just checks if all in strig are letters.
                piglatin[k] = i
        else:
                piglatin[k] = i[1:]+i[0]+'ay'
    return ' '.join(piglatin)

def t(str):
        return str[0]+str[1]

if __name__ == "__main__":
        x = main()
        print(x)