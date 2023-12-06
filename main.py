# Final project

import pygame
import math
import mfun

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    pygame.display.set_caption("Vectors")
    
    # Default parameters
    spacing = 70 # spacing between grid lines
    origin_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2 ) # Position of origin in screen

    # Key state booleans
    grid = True # Grid is enabled by default
    grid_hold = False # If user is holding that key it still consider as one input
    addition = False
    subtraction = False
    reset = False
     
    stdx = True
    stdy = True

    # Basis of vector space
    transformx = pygame.Vector2(7, 0)
    transformy = pygame.Vector2(2, 3)
    
    # Main loop
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
    
        # Standard grids with scaling factors (Change numbers in range to correct spacing)
        keys = pygame.key.get_pressed()
        grid_color = (135, 206, 235)
        semigrid_color = (30, 30, 30)
        if False:
            
            # Y axis semi grids
            if stdy:
                width_start = origin_pos[0]
                y = spacing*abs(transformx[0]) / 2 # Used to show semi grid for better precision
                for i in range (int((screen.get_width() - width_start) / spacing)*2 ): # draw no. of grid lines
                    pygame.draw.line(screen, semigrid_color, (width_start + y, 0), (width_start + y, screen.get_height()))
                    y += spacing*abs(transformx[0]) / 2
                y = spacing*abs(transformx[0]) / 2
                for i in range (int(width_start / spacing)*2 ): # draw no. of grid lines
                    pygame.draw.line(screen, semigrid_color, (width_start - y, 0), (width_start - y, screen.get_height()))
                    y += spacing*abs(transformx[0]) / 2
            # X axis semi grids
            if stdx:
                height_start = origin_pos[1]
                y = spacing*abs(transformy[1]) / 2
                for i in range (int((screen.get_height() - height_start) / spacing)*2 ): # draw no. of grid lines
                    pygame.draw.line(screen, semigrid_color, (0, height_start + y), (screen.get_width(), height_start + y))
                    y += spacing*abs(transformy[1]) / 2
                y = spacing*abs(transformy[1]) / 2
                for i in range (int(height_start / spacing)*2 ): # draw no. of grid lines
                    pygame.draw.line(screen, semigrid_color, (0, height_start - y), (screen.get_width(), height_start - y))
                    y += spacing*abs(transformy[1]) / 2

            # Y axis grids
            if stdy:
                width_start = origin_pos[0]
                x = spacing*abs(transformx[0])
                for i in range (int((screen.get_width() - width_start) / spacing) ): # draw no. of grid lines
                    pygame.draw.line(screen, grid_color, (width_start + x, 0), (width_start + x, screen.get_height()))
                    x += spacing*abs(transformx[0])
                x = spacing*abs(transformx[0])
                for i in range (int(width_start / spacing) ): # draw no. of grid lines
                    pygame.draw.line(screen, grid_color, (width_start - x, 0), (width_start - x, screen.get_height()))
                    x += spacing*abs(transformx[0])
            # X axis grids
            if stdx:
                height_start = origin_pos[1]
                x = spacing*abs(transformy[1])
                for i in range (int((screen.get_height() - height_start) / spacing) ): # draw no. of grid lines
                    pygame.draw.line(screen, grid_color, (0, height_start + x), (screen.get_width(), height_start + x))
                    x += spacing*abs(transformy[1])
                x = spacing*abs(transformy[1])
                for i in range (int(height_start / spacing) ): # draw no. of grid lines
                    pygame.draw.line(screen, grid_color, (0, height_start - x), (screen.get_width(), height_start - x))
                    x += spacing*abs(transformy[1])

        # Grids turn off/on button
        if grid_hold: # if user is still holding the key then do nothing
            if keys[pygame.K_g]:
                grid_hold = True
            else:
                grid_hold = False
            
        if grid_hold == False: # if user is pressing g freshly change state of grid
            if keys[pygame.K_g]:
                grid = not grid
                grid_hold = True
              
        # bool for transformed grids  
        if transformx[1] != 0 or transformx == (0, 0):
            stdx = False
        if transformy[0] != 0 or transformy == (0, 0):
            stdy = False
            
        # Draw x and y axis of given basis
        constant = max(screen.get_height(), screen.get_width()) # Change this buggy magic number  
        convertx = transformx*constant
        convertxn = transformx*constant*(-1)
        converty = transformy*constant
        convertyn = transformy*constant*(-1)
        
        # Basis dependent grids aka tranformed grids
        if grid:
            mfun.vector_grids(screen, origin_pos, convertx, convertxn, converty, convertyn, transformx, transformy, spacing, grid_color)
                    
        # For y we have
       
        draw_vector(screen, origin_pos, converty, spacing, "white", 1)
        draw_vector(screen, origin_pos, convertyn, spacing, "white", 1)
        
        # x axis we have
        
        draw_vector(screen, origin_pos, convertx, spacing, "white", 1)
        draw_vector(screen, origin_pos, convertxn, spacing, "white", 1)

       

        # Implement vector logic

        # Take user input (Future implementation)

        # draw vectors
        vector1 = (1, 1)
        vector2 = (1, 3)
        mfun.draw_bvector(screen, origin_pos, vector1, transformx, transformy, spacing, (0, 255, 0)) 
        draw_vector(screen, origin_pos, vector2, spacing, (0, 0, 255))
        
        '''mfun.parallel_line((0,0), vector2, vector1, screen, spacing, origin_pos, "blue", 3)
        mfun.parallel_line((0,0), vector1, vector2, screen, spacing, origin_pos, "green", 3)'''
        
        # vector addition and subtraction (future implement output vectors as transparent 50 % and transparent)

        if keys[pygame.K_a]:
            addition = True
            
        if addition: 
            vector3 =  (vector1[0] + vector2[0], vector2[1] + vector1[1])
            draw_vector(screen, origin_pos, vector3, spacing, (255, 0, 0))
            
        if keys[pygame.K_s]:
            subtraction = True
            
        if subtraction:
            draw_vector(screen, origin_pos, (vector1[0] - vector2[0], vector1[1] - vector2[1]), spacing, (255, 0, 255))
         

        # TEST AREA ! (Make effects function of spacing, future implementation)
        # zoom effect
        if keys[pygame.K_z]:
            spacing += 50*dt
        if keys[pygame.K_x]:
            spacing -= 50*dt
            
        # drag effect 
        if keys[pygame.K_RIGHT]:
            origin_pos[0] += 300*dt
        if keys[pygame.K_LEFT]:
            origin_pos[0] -= 300*dt
        if keys[pygame.K_UP]:
            origin_pos[1] -= 300*dt
        if keys[pygame.K_DOWN]:
            origin_pos[1] += 300*dt
          
        # Reset button (Undo all of the effect)
           
        if keys[pygame.K_r]:
            reset = True
        if reset:
            spacing = 70
            origin_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2 )
            reset = False
            
            
            
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 300
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(300) / 1000

    pygame.quit()


def draw_vector(screen, origin, vector, spacing, color, width = 3):
    # draw vector from origin in original basis 
    vector = (vector[0]*spacing + origin[0], (origin[1] - vector[1]*spacing))
    pygame.draw.line(screen, color, origin, vector, width)


    

main()