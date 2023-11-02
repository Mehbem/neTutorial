import pygame as pg


pg.init()


screen_info = pg.display.Info() #takes the info of the users screen
screen_width = screen_info.current_w #makes the pop-up screens width based on user's screen info
screen_height = screen_info.current_h #makes the pop-up screens height based on user's screen info

screen = pg.display.set_mode((screen_width, screen_height), pg.FULLSCREEN) #creates the display

run = True

#each variable is responsible for its respective visuals coordinates and size
bottom_gibbet = pg.Rect((60, 800, 300, 50)) 

body_gibbet = pg.Rect((180, 200, 50, 650))

hanger_gibbet = pg.Rect((180, 200, 300, 50))

rope_gibbet = pg.Rect((450, 250, 10, 80))


while run:
#this portion is responsible for actually displaying the the previously defined shapes on the op-up screen
    pg.draw.rect(screen, (106, 59, 43), bottom_gibbet)
    pg.draw.rect(screen, (106, 59, 43), body_gibbet)
    pg.draw.rect(screen, (106, 59, 43), hanger_gibbet)
    pg.draw.rect(screen, (210, 175, 135), rope_gibbet)
    
#these if statements are responsible for making it full-screen and than checking if the user clicks ESCAPE allowing them to leave that screen
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                fullscreen = not fullscreen
                
    #if event.key == pg.K_a
        #if str(pg.K_a)
           # p
                #pg.display.flip()
            
    pg.display.update()
    
pg.quit()
        

