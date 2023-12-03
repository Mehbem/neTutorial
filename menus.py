import pygame as pg
import time
pg.init()

screen_info = pg.display.Info() #takes the info of the users screen
screen_width = screen_info.current_w #makes the pop-up screens width based on user's screen info
screen_height = screen_info.current_h #makes the pop-up screens height based on user's screen info     
    
#Adding in font for menus text

font_size = screen_width // 25
adelia = pg.font.Font('ADELIA.otf', font_size)
adelia_2 = pg.font.Font('ADELIA.otf', screen_width // 15)
text_colour = (255, 255, 255) #white, can change later
play_text_colour = (255, 255, 255)
settings_text_colour = (255, 255, 255)
quit_text_colour = (255, 255, 255)

screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN) #creates the display
background_image = pg.image.load("game visuals/2102.i518.009_sky_cloud_evening_illustration.jpg")
background_image = pg.transform.scale(background_image, (screen_width, screen_height))



#defines the grass terrain below the gibbet and draws it
grass_terrain = pg.image.load("game visuals/pngimg.com - grass_PNG401.png")
grass_resized = pg.transform.scale(grass_terrain,(screen_width, 200))

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
    return track

def draw_thumb(track, pos):
    pos_y = track.y - track.height
    pos_x = track.x + pos * track.width

    thumb = pg.Rect(pos_x, pos_y, track.height, 3 * track.height)
    pg.draw.rect(screen, (255, 255, 255), thumb)
    return thumb


#want to make a function that takes current state as input and desplays the corresponding screen
def main_menu(state):
    global play_text_colour, settings_text_colour, quit_text_colour
    #Options on main menu page
    main_menu_text = "Bera and Tom's Epic Hangman!"
    main_menu_text = adelia.render(main_menu_text, True, text_colour)
    
    play_text = "Play"
    play_text = adelia.render(play_text, True, play_text_colour)
    
    settings_text = "Settings"
    settings_text = adelia.render(settings_text, True, settings_text_colour)
    
    quit_text = "Quit Game"
    quit_text = adelia.render(quit_text, True, quit_text_colour)

    pregame_text = "Guess the Animal!"
    pregame_text = adelia_2.render(pregame_text, True, (247, 117, 143))

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
        mouse_x, mouse_y = pg.mouse.get_pos()
        if play_button.collidepoint(mouse_x, mouse_y):
            play_text_colour = (46, 155,87)
        else:
            play_text_colour = (255, 255, 255)
        if settings_button.collidepoint(mouse_x, mouse_y):
            settings_text_colour = (46, 155,87)
        else:
            settings_text_colour = (255, 255, 255)
        if quit_button.collidepoint(mouse_x, mouse_y):
            quit_text_colour = (136, 8 ,8)
        else:
            quit_text_colour = (255, 255, 255)    
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pg.mouse.get_pos()
                if play_button.collidepoint(mouse_x, mouse_y):
                    screen.blit(background_image, (0,0))
                    screen.blit(grass_resized, (0,screen_height-200))
                    show_text_centred(pregame_text, 2, 2)
                    pg.display.update()
                    time.sleep(2)
                    screen.blit(background_image, (0,0))
                    screen.blit(grass_resized, (0,screen_height-200))
                    state = 'play_game'
                if settings_button.collidepoint(mouse_x, mouse_y):
                    state = 'settings_menu'
                    screen.blit(background_image, (0,0))
                    screen.blit(grass_resized, (0,screen_height-200))
                if quit_button.collidepoint(mouse_x, mouse_y):
                    state = 'quit'
    pg.display.update()
    return state
    
def settings_menu(state, master_vol, music_vol, effects_vol):

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
    master_track = settings_text_and_slider(master_vol_text, 20, 6 / 2)
    music_track = settings_text_and_slider(music_vol_text, 20, 6 / 3)
    effects_track = settings_text_and_slider(effects_vol_text, 20, 6 / 4)

    master_thumb = draw_thumb(master_track, master_vol)
    music_thumb = draw_thumb(music_track, music_vol)
    effects_thumb = draw_thumb(effects_track, effects_vol)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                state = 'main_menu'
                screen.blit(background_image, (0,0))
                screen.blit(grass_resized, (0,screen_height-200))
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pg.mouse.get_pos()
                if master_thumb.collidepoint(mouse_x, mouse_y):
                    # If the user clicked on the thumb, enable dragging
                    master_vol_dragging = True
                if music_thumb.collidepoint(mouse_x, mouse_y):
                    # If the user clicked on the thumb, enable dragging
                    music_vol_dragging = True
                if effects_thumb.collidepoint(mouse_x, mouse_y):
                    # If the user clicked on the thumb, enable dragging
                    effects_vol_dragging = True

        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                master_vol_dragging = False
                music_vol_dragging = False
                effects_vol_dragging = False
    if master_vol_dragging:
        mouse_x, mouse_y = pg.mouse.get_pos()
        
    return state, master_vol, music_vol, effects_vol



    pg.display.update()