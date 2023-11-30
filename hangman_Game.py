#all modules used in the code
import pygame as pg 
import os
import random
import sys
import menus

#initilalizing pygame (defined as pg above) and the mixer(sound)
pg.init()
pg.mixer.init()


#assigning three different playtracks to differeny channels for ease of use to turn off and on later in code
background_music = pg.mixer.Channel(0)
win_music = pg.mixer.Channel(1)
lose_music = pg.mixer.Channel(2)

#starts playing all the soundtracks and sets the volume of the background music 
background_music.set_volume(0.4)
background_music.play(pg.mixer.Sound("Music and Sound/glorious_morning.mp3"), loops = -1, fade_ms=5000)
win_music.play(pg.mixer.Sound("Music and Sound/Winning_Music.mp3"), loops = -1, fade_ms=5000)
lose_music.play(pg.mixer.Sound("Music and Sound/Losing_Music.mp3"), loops = -1, fade_ms=5000)

#since its currently on the menu screen, pausing the win and lose screen music for the time being 
win_music.pause()
lose_music.pause()


#responsible for all the sound effects of the game
correct_guess_sound = pg.mixer.Sound("Music and Sound/CorrectGuess.mp3")
correct_guess_sound.set_volume(1.0)
wrong_guess_sound = pg.mixer.Sound("Music and Sound/WrongGuess.mp3")
wrong_guess_sound.set_volume(1.0)

#info regarding the pop-up screen the player plays through
screen_info = pg.display.Info() #takes the info of the users screen
screen_width = screen_info.current_w #makes the pop-up screens width based on user's screen info
screen_height = screen_info.current_h #makes the pop-up screens height based on user's screen info
screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN) #creates the display

#defined starting values for certain functions and uses these as the basis of the incrementation points
number_of_correct_letters = 0 #change this to number of letters 
incorrect_guesses = 0 
starting_place = 0


#the word bank of the game that a random word gets picked from
wordbank = []
#opens a file and reads through each of the lines in the list of words
file = open('Animals.txt', 'r')
Lines = file.readlines() #reads through the lines of Animals.txt 
for line in Lines:
    if len(line.split(" ")) ==1: #removes any animals name ifs its not one word 
        wordbank.append(line.rstrip()) #adds that word to the wordbank and rstrip gets rid of invisible /n at the end of each word
        
#A list of guessed letters
guessed_letters = []
#picks a random word from the wordbank
random_word = random.choice(wordbank).lower()

#resets all relevant variables back to their original forms in order to allow the player to play again
def reset_game():
    #allows for variavles outside the function to be used in the function
    global number_of_correct_letters, incorrect_guesses, starting_place, guessed_letters, random_word, playing_state
    
    #setting back all the variables to their original values
    playing_state = True
    number_of_correct_letters = 0
    incorrect_guesses = 0
    starting_place = 0
    guessed_letters = []
    
    #rechooses a randomword
    random_word = random.choice(wordbank).lower()

    #Redraws the background image and grass
    screen.blit(background_image, (0, 0))
    screen.blit(grass_resized, (0, screen_height - 200))

    #function responsible for drawing all initial elments in the game like parts of the gibbet and the lines under letters
    play_game_state()

    # Reset the music channels to inital form 
    background_music.unpause()
    win_music.pause()
    lose_music.pause()

   
    pg.display.update()

    
def play_game_state():
    #making variables global allows these variables to get called by any function without having to redefine everytime
    global bottom_gibbet, body_gibbet, hanger_gibbet, rope_gibbet, lines_y, lines_x, line_width, line_spacing
       
    #each variable is responsible for its respective visuals coordinates and size as well as drawing it
    bottom_gibbet = pg.Rect((60, screen_height-50, 300, 50)) 
    pg.draw.rect(screen, (106, 59, 43), bottom_gibbet)
    body_gibbet = pg.Rect((180, screen_height-700, 50, 650))
    pg.draw.rect(screen, (106, 59, 43), body_gibbet)
    hanger_gibbet = pg.Rect((180, screen_height-700, 300, 50))
    pg.draw.rect(screen, (106, 59, 43), hanger_gibbet)
    rope_gibbet = pg.Rect((450, screen_height-650, 10, 80))
    pg.draw.rect(screen, (210, 175, 135), rope_gibbet)


    #the white lines that are under each letter
    #terms like screen_width and screen_height used throughout the game are used for making sure everything is proportional no matter what display the user has
    lines_x = screen_width//2 - len(random_word)*15
    lines_y = screen_height//3
    line_width = screen_width//24
    line_spacing = screen_width//144
    
    #ensures that the lines are evenly spaced with the specified width and spacing, uses the length of the word converts it to a range of values and assigns each of that to a line
    horizontal_position = [lines_x + i * (line_width + line_spacing) for i in range(len(random_word))]
    
    #creates a list of rectangles, each representing a line under a letter in random_word
    #These rectangles are positioned horizontally based on the horizontal_position list and vertically based on lines_y, with a specified width and thickness.
    lines_under_letters = [pg.Rect(horizontal_position[i], lines_y, line_width, screen_height//90) for i in range(len(random_word))]

    #for loop responsible for actually iterating through a list and drawing each of those rectangles in the lines_under_letters list
    for line in lines_under_letters:
        pg.draw.rect(screen, (255, 255, 255), line)
        
#this function draws a replay button and checks to see if the player is pressing it     
def draw_quit_replay_button():
    global run
    #defining all the variables and constraints of the text
    text_colour = (255, 255, 255)
    font_size = screen_width//20
    adelia = pg.font.Font('ADELIA.otf', font_size)
    
    #the actual play again text that will be displayed on the screen the function is called 
    replay_text = "Play Again"
    replay_text = adelia.render(replay_text, True, text_colour)
    
    #menus module made by Tom, it both returns the coordinates of a given text and blits it on the screen
    x_replay_button, y_replay_button = menus.show_text_centred(replay_text,2,1.3)
    replay_button = replay_text.get_rect()
    replay_button.topleft = (x_replay_button, y_replay_button)
    
    #the actual quit game text that will be displayed on the screen the function is called 
    quit_text = "Quit Game"
    quit_text = adelia.render(quit_text, True, text_colour)
    
    #menus module made by Tom, it both returns the coordinates of a given text and blits it on the screen
    x_quit_button, y_quit_button = menus.show_text_centred(quit_text,2,1.1)
    quit_button = quit_text.get_rect()
    quit_button.topleft = (x_quit_button, y_quit_button)
        
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mouse_x, mouse_y = pg.mouse.get_pos()
                if replay_button.collidepoint(mouse_x, mouse_y):
                    reset_game()
                if quit_button.collidepoint(mouse_x, mouse_y):
                    run = False
        if event.type == pg.KEYDOWN:
            #if the person presses the escape key the game closes
            if event.key == pg.K_ESCAPE:
                run = False


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
    #the letter varialbe is defined later and basically takes the letter key input of the user and converts it to a string
    #defines a variable for the png of every letter efficently 
    letter_file_name = "letter_" + letter + ".png"
    horizontal_position = [lines_x + i*line_width + (i-1)*screen_width//144 for i in range(len(random_word))]
    
    for character in location_letter:
        
        x_position = horizontal_position[character]
        y_position = screen_height//3 - screen_height//10
        letter_image = pg.image.load(os.path.join("letters", letter_file_name)).convert()
        letter_image_resized = pg.transform.scale(letter_image, (screen_width // 20, screen_height // 9))
        letter_image_resized.set_colorkey((0, 0, 0))
        
        screen.blit(letter_image_resized, (x_position, y_position))

def draw_body_part(incorrect_guesses):
    
    
    body_parts_positions = {
        1: (380, screen_height-575),   # Head
        2: (450, screen_height-465),   # Torso
        3: (446, screen_height-440),   # Left arm
        4: (320, screen_height-440),   # Right arm
        5: (454, screen_height-280),   # Left leg
        6: (380, screen_height-280)    # Right leg
    }
    
    if incorrect_guesses < len(body_parts_positions):
        x, y = body_parts_positions[incorrect_guesses]
        body_parts = pg.image.load("Body_parts/part_" + str(incorrect_guesses) + ".png")
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

def play_music(filename):
    pg.mixer.music.stop()
    pg.mixer.music.load(filename)
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.5)

def you_lose_screen():
    
    background_music.pause()
    lose_music.unpause()
    
    
    font_size = screen_width//20
    adelia = pg.font.Font('ADELIA.otf', font_size)
    text_colour = (69, 69, 69)
    
    background_lose_screen = pg.image.load("game visuals/Losescreen.jpg")
    background_lose_screen = pg.transform.scale(background_lose_screen, (screen_width, screen_height))
    screen.blit(background_lose_screen, (0,0))
    
    lose_screen_text = "You lost, the word was:" 
    lose_screen_text = adelia.render(lose_screen_text, True, text_colour)
    what_the_word_was = str(random_word)
    what_the_word_was = adelia.render(what_the_word_was, True, text_colour)
    
    menus.show_text_centred(lose_screen_text,2,2.3)
    menus.show_text_centred(what_the_word_was,2,1.7)
    
    if event.type == pg.KEYDOWN:
            #if the person presses the escape key the game closes
            if event.key == pg.K_ESCAPE:
                sys.exit(0)
    
    

def you_win_screen():
    
    background_music.pause()
    win_music.unpause()
    
    
    font_size = screen_width//30
    adelia = pg.font.Font('ADELIA.otf', font_size)
    text_colour = (100, 56, 154)
    
    background_win_screen = pg.image.load("game visuals/YouWin.jpg")
    background_win_screen = pg.transform.scale(background_win_screen, (screen_width, screen_height))
    screen.blit(background_win_screen, (0,0))
    
    win_screen_text = "Congrats you guessed the correct word:" 
    win_screen_text = adelia.render(win_screen_text, True, text_colour)
    what_the_word_was = str(random_word)
    what_the_word_was = adelia.render(what_the_word_was, True, text_colour)
    
    screen.blit(win_screen_text, (screen_width // 2 - screen_width*0.45,screen_height// 2 - 100))
    screen.blit(what_the_word_was, ((screen_width // 2 - (len(random_word) // 2 * 40)),screen_height// 2 + 50) ) 


# creating the background image and scaling the background image to fit any given screen
background_image = pg.image.load("game visuals/2102.i518.009_sky_cloud_evening_illustration.jpg")
background_image = pg.transform.scale(background_image, (screen_width, screen_height))
screen.blit(background_image, (0,0))


#defines the grass terrain below the gibbet, scales it, and draws it
grass_terrain = pg.image.load("game visuals/pngimg.com - grass_PNG401.png")
grass_resized = pg.transform.scale(grass_terrain,(screen_width, 200))
screen.blit(grass_resized, (0,screen_height-200))





#defines a list of allowed characters and prevents user from inputing non-roman letters
characters_allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
#used in the winscreen and lose screen to prevent the user from making anymore key inputs
playing_state = True
#when true allows game to run, thus setting it to false helps to quick close the game
run = True
state = 'main_menu'
while run:
    while state == 'main_menu':
        state = menus.main_menu(state)
    if state == 'settings_menu':
        menus.settings_menu()
    if state == 'quit':
        run = False
    if state == 'play_game':
        play_game_state()
        for event in pg.event.get():
            #checks if a key is being pressed down on 
            if event.type == pg.KEYDOWN:
                #if the person presses the escape key the game closes
                if event.key == pg.K_ESCAPE:
                    run = False
                    #checks if the user is pressing down on a letter key and if that letter is in the set of allowed characters
                elif event.unicode in characters_allowed and playing_state:
                    #converts whats pressed into a string letter equivalence and lowercases it 
                    letter = str(event.unicode).lower()
                
                    #makes sure that a letter only appears in a space if it's correct and the person hasn't already made 6 incorrect guesses
                    if letter in random_word and letter not in guessed_letters and incorrect_guesses < 6:  
                        letter_typed()
                        number_of_correct_letters += len(linear_search(random_word, letter))
                        correct_guess_sound.play()
                    else:
                        if letter not in guessed_letters:
                            incorrect_guesses += 1  #causes a new body part to be formed everytime
                            draw_body_part(incorrect_guesses)
                            wrong_guess_sound.play() 
                            if incorrect_guesses < 6:
                                draw_wrong_letter(starting_place)
                                starting_place += 1 #this increment is used in calculating the spacing between each wrong letter generated in the bottom 
                            else:
                            #once the player makes 6 wrong guesses this function gets called which opens the lose screen
                                you_lose_screen()
                                
                    guessed_letters.append(letter)  # Add the letter to the guessed_letters list
        #this checks if the player lost and if they did it calls the lose screen function 
        if incorrect_guesses == 6:
                #the playing_state variable is used in checking if the game is still running so when the play loses or wins it prevents any key input
                playing_state = False
                you_lose_screen()
                draw_quit_replay_button()
            
        #this checks if the player won and if they did it calls the win screen function  
        if number_of_correct_letters == len(random_word):
                playing_state = False
                you_win_screen()
                draw_quit_replay_button()
    

    pg.display.update()
              

pg.quit()