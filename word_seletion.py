
wordbank = ["kangaroo", "ocelot", "baboon", "swordfish", "duck"] #word bank that is available in the game


import random #importng a method 

random_word = random.choice(wordbank) #gets a random word from the wordbank

len_word = len(random_word) #checks the length of the word 

letter_picked = input("Pick a letter ") #asks the user to pick a letter and takes input 

if letter_picked in random_word:
    print 