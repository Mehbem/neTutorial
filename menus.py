#This is to test the menu as a script with basic run loop, code contained is the same as is written below

import pygame as pg
pg.init()

screen_info = pg.display.Info() #takes the info of the users screen
screen_width = screen_info.current_w #makes the pop-up screens width based on user's screen info
screen_height = screen_info.current_h #makes the pop-up screens height based on user's screen info     
    
#Adding in font for menus text

font_size = screen_width//25
adelia = pg.font.Font('ADELIA.otf', font_size)
text_colour = (255, 255, 255) #white, can change later


screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN) #creates the display

background_image = pg.image.load("2102.i518.009_sky_cloud_evening_illustration.jpg")

# Scale the background image to fit the screen
background_image = pg.transform.scale(background_image, (screen_width, screen_height))

#Menus unique functions

def show_text_centred(text, x_pos, y_pos):
    text_width = text.get_width()
    text_height = text.get_height()
    x = screen_width // x_pos - text_width // 2
    y = screen_height // y_pos - text_height // 2
    screen.blit(text, (x, y))
    return x, y

def show_text_left(text, x_pos, y_pos):
     text_height = text.get_height()
     screen.blit(text, ((screen_width // x_pos), screen_height // y_pos - text_height // 2))

state = 'main_menu' #see if strings are the best way to do this

#want to make a function that takes current state as input and desplays the corresponding screen
def state_check():
    global state, run

    #Options on main menu page
    main_menu_text = "Bera and Tom's Epic Hangman!"
    main_menu_text = adelia.render(main_menu_text, True, text_colour)
    
    play_text = "Play"
    play_text = adelia.render(play_text, True, text_colour)
    
    settings_text = "Settings"
    settings_text = adelia.render(settings_text, True, text_colour)
    
    quit_text = "Quit Game"
    quit_text = adelia.render(quit_text, True, text_colour)

    #Options on settings menu page
    master_vol_text = "Master Volume: "
    master_vol_text = adelia.render(master_vol_text, True, text_colour)

    music_vol_text = "Music Volume: "
    music_vol_text = adelia.render(music_vol_text, True, text_colour)

    effects_vol_text = "Effects Volume: "
    effects_vol_text = adelia.render(effects_vol_text, True, text_colour)

    if state == 'main_menu':
        #Displaying main menu text
        show_text_centred(main_menu_text, 2, 7)
        play_x, play_y = show_text_centred(play_text, 2, 7 / 3)
        settings_x, settings_y = show_text_centred(settings_text, 2, 7 / 4)
        quit_x, quit_y = show_text_centred(quit_text, 2, 7 / 5)

        play_button = play_text.get_rect()
        play_button.topleft = (play_x, play_y)

        settings_button = settings_text.get_rect()
        settings_button.topleft = (settings_x, settings_y)

        quit_button = quit_text.get_rect()
        quit_button.topleft = (quit_x, quit_y)

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    if play_button.collidepoint(mouse_x, mouse_y):
                        state = 'play_game'
                    if settings_button.collidepoint(mouse_x, mouse_y):
                        state = 'settings_menu'
                    if quit_button.collidepoint(mouse_x, mouse_y):
                        run = False

    if state == 'settings_menu':
        #Displaying settings menu text
        show_text_left(master_vol_text, 20, 6 / 2)



        show_text_left(music_vol_text, 20, 6 / 3)



        show_text_left(effects_vol_text, 20, 6 / 4)


        

    if state == 'play_game':
        return state


run = True
    
while run:
#these if statements are responsible for making it full-screen and than checking if the user clicks ESCAPE allowing them to leave that screen
    for event in pg.event.get():
        if event.type == pg.QUIT:
                run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

    screen.blit(background_image, (0,0))

    state_check()

    pg.display.update()


pg.quit()

#Need 3 states: main menu (default), play (game), and settings (audio (master volume, music volume, effects volume))
#All should be nested under 'while run:' loop 