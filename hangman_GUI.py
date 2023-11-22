import pygame as pg
import os
import random

pg.init()


#info regarding the pop-up screen the player plays through
screen_info = pg.display.Info() #takes the info of the users screen
screen_width = screen_info.current_w #makes the pop-up screens width based on user's screen info
screen_height = screen_info.current_h #makes the pop-up screens height based on user's screen info
screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN) #creates the display

#defined starting values for certain functions and uses these as the basis of the incrementation points
correct_letter = 0 #change this to number of letters 
incorrect_guesses = 0 
starting_place = 0

#the word bank of the game that a random word gets picked from
wordbank = ["swordfish"]
#A list of guessed letters
guessed_letters = []
#picks a random word from the wordbank
random_word = random.choice(wordbank)


#searches for everytime a letter appears in a word and creates a list of their positions
def linear_search(arr, target):
    
    positions = []
    for i in range(len(arr)):
        if arr[i] == target:
            positions.append(i)
    return positions

#this function uses the linear search previously defined and generates a letter on the screen even if it's wrong 
def letter_typed():
    
    location_letter = linear_search(random_word, letter)
    letter_file_name = "letter_" + letter + ".png"
    
    for character in location_letter:
        
        x_position = (screen_width - 810 ) + (character * 70) 
        y_position = lines_y - 100
        
        letter_image = pg.image.load(os.path.join("letters", letter_file_name)).convert()
        letter_image_resized = pg.transform.scale(letter_image, (screen_width // 20, screen_height // 9))
        letter_image_resized.set_colorkey((0, 0, 0))
        
        screen.blit(letter_image_resized, (x_position, y_position))

def draw_body_part(incorrect_guesses):
    
    body_parts_positions = {
        1: (screen_width-1060, screen_height-575),   # Head
        2: (screen_width-990, screen_height-465),   # Torso
        3: (screen_width-1140, screen_height-440),   # Left arm
        4: (screen_width-990, screen_height-440),   # Right arm
        5: (screen_width-990, screen_height-280),   # Left leg
        6: (screen_width-1064, screen_height-280)    # Right leg
    }
    
    if incorrect_guesses < len(body_parts_positions):
        x, y = body_parts_positions[incorrect_guesses]
        body_parts = pg.image.load("part_" + str(incorrect_guesses) + ".png")
        # Display the resized image on the screen
        screen.blit(body_parts, (x, y))

        

def draw_wrong_letter(starting_place):
    letter_file_name = "letter_" + letter + ".png"
    wrong_y_position = screen_height - 600
    wrong_x_position = starting_place * 100 + 600
    letter_image = pg.image.load(os.path.join("letters", letter_file_name)).convert()
    letter_image_resized = pg.transform.scale(letter_image, (screen_width // 20, screen_height // 9))
    letter_image_resized.set_colorkey((0, 0, 0))
    screen.blit(letter_image_resized, (wrong_x_position, wrong_y_position))

def you_lose_screen():
    font_size = screen_width//20
    adelia = pg.font.Font('ADELIA.otf', font_size)
    text_colour = (69, 69, 69)
    
    background_lose_screen = pg.image.load("Losescreen.jpg")
    background_lose_screen = pg.transform.scale(background_lose_screen, (screen_width, screen_height))
    screen.blit(background_lose_screen, (0,0))
    
    lose_screen_text = "You lost, the word was:" 
    lose_screen_text = adelia.render(lose_screen_text, True, text_colour)
    what_the_word_was = str(random_word)
    what_the_word_was = adelia.render(what_the_word_was, True, text_colour)
    
    screen.blit(lose_screen_text, (screen_width // 2 - 600,screen_height// 2 - 100))
    screen.blit(what_the_word_was, ((screen_width // 2 - (len(random_word) // 2 * 50)),screen_height// 2 + 50) )

def you_win_screen():
    font_size = screen_width//30
    adelia = pg.font.Font('ADELIA.otf', font_size)
    text_colour = (100, 56, 154)
    
    background_win_screen = pg.image.load("YouWin.jpg")
    background_win_screen = pg.transform.scale(background_win_screen, (screen_width, screen_height))
    screen.blit(background_win_screen, (0,0))
    
    win_screen_text = "Congrats you guessed the correct word:" 
    win_screen_text = adelia.render(win_screen_text, True, text_colour)
    what_the_word_was = str(random_word)
    what_the_word_was = adelia.render(what_the_word_was, True, text_colour)
    
    screen.blit(win_screen_text, (screen_width // 2 - 675,screen_height// 2 - 100))
    screen.blit(what_the_word_was, ((screen_width // 2 - (len(random_word) // 2 * 40)),screen_height// 2 + 50) )
   
    
# creating the background image and scaling the background image to fit any given screen
background_image = pg.image.load("2102.i518.009_sky_cloud_evening_illustration.jpg")
background_image = pg.transform.scale(background_image, (screen_width, screen_height))
screen.blit(background_image, (0,0))
run = True

#creating the lose background image and scaling the background image

#grass terrarion below the gibbet
grass_terrain = pg.image.load("pngimg.com - grass_PNG401.png")
grass_resized = pg.transform.scale(grass_terrain,(screen_width, 200))

#each variable is responsible for its respective visuals coordinates and size
bottom_gibbet = pg.Rect((60, screen_height-50, 300, 50)) #mention it is making it proportional whenever the term screen_height and screen_width
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


#this is what is known as the main game loop 
while run:
    for event in pg.event.get():
        #checks if a key is being pressed down on 
        if event.type == pg.KEYDOWN:
            #if the person presses the escape key the game closes
            if event.key == pg.K_ESCAPE:
                run = False
                #checks if the user is pressing down on a letter key
            elif event.unicode.isalpha():
                #converts whats pressed into a string letter equivalence
                letter = str(event.unicode)
                #makes sure that a letter only appears in a space if it's correct and the person hasn't already made 6 incorrect guesses
                if letter in random_word and letter not in guessed_letters and incorrect_guesses < 6:  
                    letter_typed()
                    correct_letter += len(linear_search(random_word, letter))
                else:
                    if letter not in guessed_letters:
                        incorrect_guesses += 1  # causes a new body part to be formed everytime
                        draw_body_part(incorrect_guesses) 
                        if incorrect_guesses < 6:
                            draw_wrong_letter(starting_place)
                            starting_place += 1 #this increment is used in calculating the spacing between each wrong letter generated in the bottom 
                        else:
                        #once the player makes 6 wrong guesses this function gets called which opens the lose screen
                            you_lose_screen()
                guessed_letters.append(letter)  # Add the letter to the guessed_letters list
    #this checks if the player won and if they did it calls the win screen function which opens the win screen
    if correct_letter == len(random_word):
        you_win_screen()
    

    pg.display.update()
              

pg.quit()


