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

run = True
main_menu = True
play_game = False
settings_menu = False
    
while run:
    while main_menu:
         #these if statements are responsible for making it full-screen and than checking if the user clicks ESCAPE allowing them to leave that screen
         for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                    main_menu = False
            screen.blit(background_image, (0,0))

        #Rendering menus text

            main_menu_text = "Bera and Tom's Epic Hangman!"
            play_text = "Play"
            settings_text = "Settings"
            main_menu_text = adelia.render(main_menu_text, True, text_colour)
            play_text = adelia.render(play_text, True, text_colour)
            settings_text = adelia.render(settings_text, True, text_colour)

            screen.blit(main_menu_text, ((screen_width - main_menu_text.get_width()) // 2, 300))
            screen.blit(play_text, ((screen_width - play_text.get_width()) // 2, 500))
            screen.blit(settings_text, ((screen_width - settings_text.get_width()) // 2, 700))
            pg.display.update()


pg.quit()



#Need 3 states: main menu (default), play (game), and settings (audio (master volume, music volume, effects volume))
#All should be nested under 'while run:' loop 