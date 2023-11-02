#req methods:
import random

#defining the word bank to select from

wordbank = ["kangaroo", "ocelot", "baboon", "swordfish", "duck"]


random_word = random.choice(wordbank) #gets a random word from the wordbank

len_word = len(random_word) #checks the length of the word 

letter_picked = input("Pick a letter ") #asks the user to pick a letter and takes input 

if letter_picked in random_word:
