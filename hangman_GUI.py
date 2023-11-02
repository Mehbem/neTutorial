import pygame as pg


pg.init()


screen_info = pg.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN)

run = True

bottom_gibbet = pg.Rect((60, 800, 300, 50))

body_gibbet = pg.Rect((180, 200, 50, 650))

hanger_gibbet = pg.Rect((180, 200, 300, 50))

rope_gibbet = pg.Rect((450, 250, 10, 80))

head_hangman = 

while run:
    
    pg.draw.rect(screen, (106, 59, 43), bottom_gibbet)
    pg.draw.rect(screen, (106, 59, 43), body_gibbet)
    pg.draw.rect(screen, (106, 59, 43), hanger_gibbet)
    pg.draw.rect(screen, (210, 175, 135), rope_gibbet)
    
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN)
                else:
                    screen = pg.display.set_mode((800, 600))  # Set to a non-fullscreen size
                pg.display.flip()
            
    pg.display.update()
    
pg.quit()
        

