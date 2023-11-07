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

#Menus unique variables

def show_text_centred(text, x_pos, y_pos):
    text_rendered = adelia.render(text, True, text_colour)
    text_width = text_rendered.get_width()
    text_height = text_rendered.get_height()
    screen.blit(text_rendered, (screen_width // x_pos - text_width // 2, screen_height // y_pos - text_height // 2))

def show_text_left(text, x_pos, y_pos):
     text_rendered = adelia.render(text, True, text_colour)
     text_height = text_rendered.get_height()
     screen.blit(text_rendered, ((screen_width // x_pos), screen_height // y_pos - text_height // 2))

main_menu = True
play_game = False
settings_menu = False

#Options on main menu page
main_menu_text = "Bera and Tom's Epic Hangman!"

play_text = "Play"

settings_text = "Settings"

quit_text = "Quit Game"

#Options on settings menu page
master_vol_text = "Master Volume: "

music_vol_text = "Music Volume: "

effects_vol_text = "Effects Volume: "


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

    if main_menu:
        #Displaying main menu text
        show_text_centred(main_menu_text, 2, 7)
        show_text_centred(play_text, 2, 7 / 3)
        show_text_centred(settings_text, 2, 7 / 4)
        show_text_centred(quit_text, 2, 7 / 5)

    if settings_menu:
        #Displaying settings menu text
        show_text_left(master_vol_text, 20, 6 / 2)
        show_text_left(music_vol_text, 20, 6 / 3)
        show_text_left(effects_vol_text, 20, 6 / 4)

    pg.display.update()


pg.quit()

#Need 3 states: main menu (default), play (game), and settings (audio (master volume, music volume, effects volume))
#All should be nested under 'while run:' loop 