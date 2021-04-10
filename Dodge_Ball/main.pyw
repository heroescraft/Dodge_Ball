import pygame
from random import randint


pygame.init()


if __name__ == '__main__':

    #func
    def move_with_arrows(x, speed):
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_LEFT]:
            x -= speed

        return x

    playerIMG = pygame.image.load('img\\player.png')
    objectIMG = pygame.image.load('img\\object.png')
    grassIMG = pygame.image.load('img\\grass.png')
    icon = pygame.image.load('img\\icon.ico')

    
        

    def player(x, y, size):
        screen.blit(playerIMG,(x,y))
        #pygame.draw.rect(screen, BLUE, [x, y, size, size],0)

    def Object(x, y, size):
        screen.blit(objectIMG,(x,y))
        #pygame.draw.rect(screen, RED, [x, y, size, size],0)

    def draw_text(text, font_name, size, color, x, y):
        '''This is an edited function from:
https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame

It is used to make text appear on the screen.
'''
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, dest=(x,y))



    
    # Define some colors
    BLACK = ( 0, 0, 0)
    WHITE = ( 255, 255, 255)
    GREEN = ( 0, 255, 0)
    RED = ( 255, 0, 0)
    GRAY = (100, 100, 100)
    BLUE = (0, 0, 255)
    LIGHTBLUE = (130, 182, 236)


    # Open a new window
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Dodge Ball! 1.0")
    pygame.display.set_icon(icon)

    
    psize = 50
    default_pspeed = 5
    pspeed = default_pspeed
    player_speed_increase = True
    px = size[0]/2

    allow_movement = True


    osize = 50
    rx = randint(0, size[0]-osize)
    ry = randint(osize, size[1]/3)

    i=0
    speeduprate=10
    sur=speeduprate
    default_speed = 5
    speed=default_speed

    object_player_collisions=True

    debug = False
    collision=False
    

    
    carryOn = True
    clock = pygame.time.Clock()

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                  carryOn = False
            key_input = pygame.key.get_pressed()   
            if key_input[pygame.K_F3]:
                if debug == False:
                    debug = True
                    print('debug=True')
                else:
                    debug = False
                    print('debug=False')

                    


        screen.fill(LIGHTBLUE)
        screen.blit(grassIMG,(0,size[1]-50))

        #pygame.draw.rect(screen, RED, [55, 200, 100, 70],0)
        #pygame.draw.line(screen, WHITE, [0, 0], [100, 100], 1)
        #pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)


        #Wall collisions
        if px <= 0:
            px = 1
        elif px+psize >= size[0]:
            px = size[0]-1-psize
            
        #movement and player func
        if allow_movement:
            px = move_with_arrows(px, pspeed)
        player(px, size[1]-(psize*2), psize)
        if debug:
            pygame.draw.line(screen, RED, [px, size[1]-(psize*2)], [px+psize, size[1]-psize], 5)

        #objects

        Object(rx, ry, osize)
        if debug:
            pygame.draw.line(screen, BLUE, [rx, ry], [rx+osize, ry+osize], 5)
        i+=1
        updatepersec = 1
        if allow_movement:
            if i == updatepersec:
                i=0
                ry+=speed
            #when hit ground
        if ry >= size[1]-osize:
            rx = randint(0, size[0]-osize)
            ry = randint(osize, size[1]/3)
            sur-=1
    
        if sur == 0:
            sur=speeduprate
            speed+=1
            if player_speed_increase:
                pspeed+=1


        #object vs player collisions
        if object_player_collisions:
            #if object has the same y level as player
            if ry in range(size[1]-(psize*2), size[1]-psize) or ry+osize in range(size[1]-(psize*2), size[1]-psize):
                #if object is touching player
                if rx in range(int(px), int(px+psize)) or rx+osize in range(int(px), int(px+psize)):
                    allow_movement=False
                    collision=True
                    draw_text('GAME OVER', 'fonts\\Press_Start_2P\\PressStart2P-Regular.ttf', 50, BLACK, (size[0]/2)-220, (size[1]/2)-50)
                    draw_text('PRESS SPACE TO CONTINUE', 'fonts\\Press_Start_2P\\PressStart2P-Regular.ttf', 20, BLACK, (size[0]/2)-220, (size[1]/2))
                    keys = pygame.key.get_pressed()  #checking pressed keys
                    if keys[pygame.K_SPACE]:
                        rx = randint(0, size[0]-osize)
                        ry = randint(osize, size[1]/3)
                        allow_movement=True
                        speed=default_speed
                        pspeed = default_pspeed
                        sur=speeduprate
                        i=0
                        collision=False

        #debug screen
        if debug:
            Roboto = 'fonts\\Roboto\\Roboto-Regular.ttf'
            fs = 15
            draw_text('debug='+str(debug), Roboto, fs, WHITE, 10, 10)

            draw_text('player=('+str(px)+', '+str(size[1]-(psize*2))+')', Roboto, fs, WHITE, 10, 25)

            draw_text('object=('+str(rx)+', '+str(ry)+')', Roboto, fs, WHITE, 10, 40)

            draw_text('player_speed='+str(pspeed), Roboto, fs, WHITE, 10, 55)

            draw_text('object_speed='+str(speed), Roboto, fs, WHITE, 10, 70)

            

            draw_text('collision='+str(collision), Roboto, fs, WHITE, 10, 85)
                

        
        
        
    
        pygame.mouse.set_visible(False)

        pygame.display.flip()
        clock.tick(60)
        
 

    pygame.quit()
