# Final project

import pygame
import mfun

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    pygame.display.set_caption("Vectors")
    pygame.display.set_icon(screen)
    
    # Default parameters
    spacing = 70 # spacing between grid lines
    origin_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2 ) # Position of origin in screen

    # Key state booleans
    grid = True # Grid is enabled by default
    grid_hold = False # If user is holding that key it still consider as one input
    addition = False
    subtraction = False
    reset = False
    refgrid = True # Reference grids
    ref_hold = False
    
    # Basis of vector space
    transformx = pygame.Vector2(1, 0)
    transformy = pygame.Vector2(0, 1)
    
    # Main loop
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
    
        # Standard grids 
        keys = pygame.key.get_pressed()
        grid_color = (135, 206, 235)  

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
                
        # Reference grid turn on off button (bad design)
        if ref_hold: 
            if keys[pygame.K_v]:
                ref_hold = True
            else: 
                ref_hold = False
        if ref_hold == False:
            if keys[pygame.K_v]:
                refgrid = not refgrid
                ref_hold = True
            
        # Draw x and y axis of given basis
        constant = max(screen.get_height(), screen.get_width()) # Change this buggy magic number  
        convertx = transformx*constant
        convertxn = transformx*constant*(-1)
        converty = transformy*constant
        convertyn = transformy*constant*(-1)
        
        # Reference grids and axis
        if refgrid:
            mfun.reference_grids(screen, origin_pos, (25, 25, 25), (100, 100, 100), spacing)
        # Basis dependent grids aka tranformed grids
        if grid:
            mfun.vector_grids(screen, origin_pos, convertx, convertxn, converty, convertyn, transformx, transformy, spacing, grid_color, 2)                
                    
        # For y we have
       
        draw_vector(screen, origin_pos, converty, spacing, "white", 2)
        draw_vector(screen, origin_pos, convertyn, spacing, "white", 2)
        
        # x axis we have
        
        draw_vector(screen, origin_pos, convertx, spacing, "white", 2)
        draw_vector(screen, origin_pos, convertxn, spacing, "white", 2)

       

        # Implement vector logic

        # Take user input (Future implementation)

        # draw vectors
        vector1 = (1, 1)
        vector2 = (1, 3)
        mfun.draw_bvector(screen, origin_pos, vector1, transformx, transformy, spacing, (0, 255, 0)) 
        mfun.draw_bvector(screen, origin_pos, vector2, transformx, transformy, spacing, "purple")
        
        # vector addition and subtraction (future implement output vectors as transparent 50 % and transparent)

        if keys[pygame.K_a]:
            addition = True
            
        if addition: 
            vector3 =  (vector1[0] + vector2[0], vector2[1] + vector1[1])
            mfun.draw_bvector(screen, origin_pos, vector3, transformx, transformy, spacing, "red")
            
        if keys[pygame.K_s]:
            subtraction = True
            
        if subtraction:
            vector4 = (vector1[0] - vector2[0], vector1[1] - vector2[1])
            mfun.draw_bvector(screen, origin_pos, vector4, transformx, transformy, spacing, "yellow")
         

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

        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(120) / 1000

    pygame.quit()


def draw_vector(screen, origin, vector, spacing, color, width = 3):
    # draw vector from origin in original basis 
    vector = (vector[0]*spacing + origin[0], (origin[1] - vector[1]*spacing))
    pygame.draw.line(screen, color, origin, vector, width)


    

main()