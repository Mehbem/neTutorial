import pygame as pg

import random
#defining the word bank to select from

wordbank = ["kangaroo", "ocelot", "baboon", "swordfish", "duck"]

#Retrieve a random word from wordbank

random_word = random.choice(wordbank)

pg.init()

correct_guesses = ['_' for _ in random_word]

screen_info = pg.display.Info() #takes the info of the users screen
screen_width = screen_info.current_w #makes the pop-up screens width based on user's screen info
screen_height = screen_info.current_h #makes the pop-up screens height based on user's screen info

screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN) #creates the display

run = True

#each variable is responsible for its respective visuals coordinates and size
bottom_gibbet = pg.Rect((60, 800, 300, 50)) 

body_gibbet = pg.Rect((180, 200, 50, 650))

hanger_gibbet = pg.Rect((180, 200, 300, 50))

rope_gibbet = pg.Rect((450, 250, 10, 80))

lines_x = 500
lines_y = 200
letter_width = 60
line_spacing = 10

horizontal_position = [lines_x + i * (letter_width + line_spacing) for i in range(len(random_word))]

lines_under_letters = [pg.Rect(horizontal_position[i], lines_y, letter_width, 10) for i in range(len(random_word))]


while run:
#this portion is responsible for actually displaying the the previously defined shapes on the op-up screen
    pg.draw.rect(screen, (106, 59, 43), bottom_gibbet)
    pg.draw.rect(screen, (106, 59, 43), body_gibbet)
    pg.draw.rect(screen, (106, 59, 43), hanger_gibbet)
    pg.draw.rect(screen, (210, 175, 135), rope_gibbet)
    
    
    for line in lines_under_letters:
        pg.draw.rect(screen, (255, 255, 255), line)


    pg.display.update()
    
#these if statements are responsible for making it full-screen and than checking if the user clicks ESCAPE allowing them to leave that screen
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                fullscreen = not fullscreen
            elif event.unicode.isalpha():
                 # Check if the pressed key is a letter and if it's in the word
                letter = event.unicode.upper()
                if letter in random_word:
                    for i in range(len(random_word)):
                        if random_word[i] == letter:
                            correct_guesses[i] = letter
                            

    # Draw the current state of the word with underscores and guessed letters
    display_word = ' '.join(correct_guesses)
    # Draw display_word on the screen as needed

    # Check if the word has been guessed completely
    if ''.join(correct_guesses) == random_word:
    #if event.key == pg.K_a
        #if str(pg.K_a)
           # p
                #pg.display.flip()
            
        pg.display.update()
    
pg.quit()
haha


        

