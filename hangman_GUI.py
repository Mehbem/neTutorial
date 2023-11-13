import pygame as pg
import os
import random
import menus

pg.init()
#info regarding the pop-up screen the player plays through
screen_info = pg.display.Info() #takes the info of the users screen
screen_width = screen_info.current_w #makes the pop-up screens width based on user's screen info
screen_height = screen_info.current_h #makes the pop-up screens height based on user's screen info
screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN) #creates the display

#defined starting values for defined function
correct_letter = 0
incorrect_guesses = 0 
starting_place = 0

#defining the word bank to select from
wordbank = ["kangaroo"]
#A list of guessed letters
guessed_letters = []
#picks a random word from the wordbank
random_word = random.choice(wordbank)



def linear_search(arr, target):
    
    positions = []
    for i in range(len(arr)):
        if arr[i] == target:
            positions.append(i)
    return positions


def letter_typed(correct_letter):
    
    location_letter = linear_search(random_word, letter)
    letter_file_name = "letter_" + letter + ".png"
    print (location_letter)
    
    for character in location_letter:
        
        x_position = (screen_width - 810 ) + (character * 70) 
        y_position = lines_y - 100
        letter_image = pg.image.load(os.path.join("letters", letter_file_name)).convert()
        letter_image_resized = pg.transform.scale(letter_image, (screen_width // 20, screen_height // 9))
        letter_image_resized.set_colorkey((0, 0, 0))
        screen.blit(letter_image_resized, (x_position, y_position))
        correct_letter += 1
        
    return correct_letter

   
def draw_body_part(incorrect_guesses):
    
    body_parts_positions = {
        0: (screen_width-1060, screen_height-575),   # Head
        1: (screen_width-990, screen_height-465),   # Torso
        2: (screen_width-1140, screen_height-440),   # Left arm
        3: (screen_width-990, screen_height-440),   # Right arm
        4: (screen_width-990, screen_height-280),   # Left leg
        5: (screen_width-1064, screen_height-280)    # Right leg
    }
    
    if incorrect_guesses < len(body_parts_positions):
        x, y = body_parts_positions[incorrect_guesses]
        body_parts = pg.image.load("part_" + str(incorrect_guesses) + ".png")
        # Display the resized image on the screen
        screen.blit(body_parts, (x, y))

        

def draw_wrong_letter():
    letter_file_name = "letter_" + letter + ".png"
    wrong_y_position = screen_height - 600
    wrong_x_position = starting_place * 100 + 600
    letter_image = pg.image.load(os.path.join("letters", letter_file_name)).convert()
    letter_image_resized = pg.transform.scale(letter_image, (screen_width // 20, screen_height // 9))
    letter_image_resized.set_colorkey((0, 0, 0))
    screen.blit(letter_image_resized, (wrong_x_position, wrong_y_position))


# creating the background image and scaling the background image to fit any given screen
background_image = pg.image.load("2102.i518.009_sky_cloud_evening_illustration.jpg")
background_image = pg.transform.scale(background_image, (screen_width, screen_height))
screen.blit(background_image, (0,0))
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



#responsible for actually displaying the gibbet and the grass while the loop is running
screen.blit(grass_resized, (0,screen_height-200))
pg.draw.rect(screen, (106, 59, 43), bottom_gibbet)
pg.draw.rect(screen, (106, 59, 43), body_gibbet)
pg.draw.rect(screen, (106, 59, 43), hanger_gibbet)
pg.draw.rect(screen, (210, 175, 135), rope_gibbet)


for line in lines_under_letters:
    pg.draw.rect(screen, (255, 255, 255), line)


state = 'main_menu'
while run:
    pg.display.update()
    menus.state_check()
    if state == 'play_game':
        for event in pg.event.get():
        
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                    #checks if the user is pressing a letter key
                elif event.unicode.isalpha():
                    #converts whats pressed into a string letter equivalence
                    letter = str(event.unicode)
                    #makes sure that a letter only appears in a space if it's correct and the person hasn't already made 6 incorrect guesses
                    if letter in random_word and letter not in guessed_letters and incorrect_guesses < 6:  
                        letter_typed(correct_letter)
                    
                    else:
                        if letter not in guessed_letters:
                            draw_body_part(incorrect_guesses) 
                            incorrect_guesses += 1  # Increment the incorrect guess count
                            if incorrect_guesses <=6:
                                draw_wrong_letter()
                                starting_place += 1
                            else:
                                None
                    guessed_letters.append(letter)  # Add the letter to the guessed_letters list

    

    pg.display.update()
              
                        
pg.quit()



