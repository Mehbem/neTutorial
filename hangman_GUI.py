import pygame as pg

import random
#defining the word bank to select from

wordbank = ["kangaroo", "ocelot", "baboon", "swordfish", "duck"]

#Retrieve a random word from wordbank

random_word = random.choice(wordbank)

pg.init()

#info regarding the pop-up screen the player plays through
screen_info = pg.display.Info() #takes the info of the users screen
screen_width = screen_info.current_w #makes the pop-up screens width based on user's screen info
screen_height = screen_info.current_h #makes the pop-up screens height based on user's screen info
screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN) #creates the display


# creating the background image and scaling the background image to fit any given screen
background_image = pg.image.load("2102.i518.009_sky_cloud_evening_illustration.jpg")
background_image = pg.transform.scale(background_image, (screen_width, screen_height))

run = True

#grass terrarion below the gibbet
grass_terrain = pg.image.load("pngimg.com - grass_PNG401.png")
grass_resized = pg.transform.scale(grass_terrain,(screen_width, 200))

#each variable is responsible for its respective visuals coordinates and size
bottom_gibbet = pg.Rect((60, screen_height-50, 300, 50)) 
body_gibbet = pg.Rect((180, screen_height-700, 50, 650))
hanger_gibbet = pg.Rect((180, screen_height-700, 300, 50))
rope_gibbet = pg.Rect((450, screen_height-650, 10, 80))


#the white lines that are under each letter
lines_x = screen_width-800
lines_y = screen_height-700
letter_width = 60
line_spacing = 10
horizontal_position = [lines_x + i * (letter_width + line_spacing) for i in range(len(random_word))]
lines_under_letters = [pg.Rect(horizontal_position[i], lines_y, letter_width, 10) for i in range(len(random_word))]


while run:
#responsible for actually displaying the gibbet and the grass while the loop is running
    screen.blit(grass_resized, (0,screen_height-200))
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
                run = False
            elif event.unicode.isalpha():
                 # Check if the pressed key is a letter and if it's in the word
                letter = event.unicode.upper()
                #if letter in random_word:
                    #for i in range(len(random_word)):
                        #if random_word[i] == letter:
    screen.blit(background_image, (0,0))



pg.quit()

        

