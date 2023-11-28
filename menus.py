import pygame as pg
pg.init()

screen_info = pg.display.Info() #takes the info of the users screen
screen_width = screen_info.current_w #makes the pop-up screens width based on user's screen info
screen_height = screen_info.current_h #makes the pop-up screens height based on user's screen info     
    
#Adding in font for menus text

font_size = screen_width // 25
adelia = pg.font.Font('ADELIA.otf', font_size)
text_colour = (255, 255, 255) #white, can change later


screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN) #creates the display

#Menus unique functions

def show_text_centred(text, x_pos, y_pos):
    text_width = text.get_width()
    text_height = text.get_height()
    x = screen_width // x_pos - text_width // 2
    y = screen_height // y_pos - text_height // 2
    screen.blit(text, (x, y))
    return x, y

def settings_text_and_slider(text, x_pos, y_pos):
    text_height = text.get_height()
    text_width = text.get_width()
    x = screen_width // x_pos
    slider_width = screen_width // 3

    # Display the text
    screen.blit(text, (x, screen_height // y_pos - text_height // 2))

    # Draw the slider track
    track = pg.Rect(screen_width // 2, screen_height // y_pos - text_height // 2 + screen_height // 36, slider_width, screen_height // 36)
    pg.draw.rect(screen, (255, 255, 255), track)
    return



#want to make a function that takes current state as input and desplays the corresponding screen
def main_menu(state):

    #Options on main menu page
    main_menu_text = "Bera and Tom's Epic Hangman!"
    main_menu_text = adelia.render(main_menu_text, True, text_colour)
    
    play_text = "Play"
    play_text = adelia.render(play_text, True, text_colour)
    
    settings_text = "Settings"
    settings_text = adelia.render(settings_text, True, text_colour)
  
    
    quit_text = "Quit Game"
    quit_text = adelia.render(quit_text, True, text_colour)

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
                    state = 'quit'
    pg.display.update()
    return state
    
def settings_menu():

    #Options on settings menu page
    master_vol_text = "Master Volume: "
    master_vol_text = adelia.render(master_vol_text, True, text_colour)
    master_vol_dragging = False

    music_vol_text = "Music Volume: "
    music_vol_text = adelia.render(music_vol_text, True, text_colour)
    music_vol_dragging = False

    effects_vol_text = "Effects Volume: "
    effects_vol_text = adelia.render(effects_vol_text, True, text_colour)
    effects_vol_dragging = False
    #Displaying settings menu text
    settings_text_and_slider(master_vol_text, 20, 6 / 2)
    settings_text_and_slider(music_vol_text, 20, 6 / 3)
    settings_text_and_slider(effects_vol_text, 20, 6 / 4)
    



    pg.display.update()