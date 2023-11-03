#req methods:

import random
import pygame as pygame

#keystroke identity (key.Q is assigned str value "Q")



#defining the word bank to select from

wordbank = ["kangaroo", "ocelot", "baboon", "swordfish", "duck"]

#Retrieve a random word from wordbank

random_word = random.choice(wordbank)

#info needed abt word: length, possible spaces & where, if a letter occurs (how many times & where), 

len_word = len(random_word) #checks the length of the word 


#if letter_picked in random_word: