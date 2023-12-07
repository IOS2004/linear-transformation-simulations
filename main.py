# Final project

import pygame
import mfun
import math

def main():
    # pygame setup
    pygame.init()
    
    main_width = 1200
    main_height = 800
    screen_main = pygame.display.set_mode((main_width, main_height), pygame.HWSURFACE | pygame.DOUBLEBUF)
    
    clock = pygame.time.Clock()
    running = True
    dt = 0
    pygame.display.set_caption("Vectors")

    # Surface to draw main interactive graph on
    graphCoord = (screen_main.get_width()/1.5, screen_main.get_height())
    screen = pygame.Surface(graphCoord, pygame.HWSURFACE)
    # Surface for menu
    menu = pygame.Surface((main_width/3, main_height))
    
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
    
    # Button state booleans
    start = False # Turns on the graph page
    frontPage = True # Front page of software
    sideMenu = False # Displays side menu
    
    # Basis of vector space
    transformx = pygame.Vector2(1, 0)
    transformy = pygame.Vector2(0, 1)
    
    # Image surfaces
    logo = pygame.image.load('images/Logo.png')
    pygame.display.set_icon(logo) # Icon of software
    
    front = pygame.image.load('images/Front.jpg') # Front page of software
    front = pygame.transform.smoothscale(front, (main_width, main_height))

    start_img = pygame.image.load('images/start.png').convert_alpha()  
    toggle_img = pygame.image.load('images/left.png').convert_alpha()
    detoggle_img = pygame.image.load('images/right.png').convert_alpha()
    home_img = pygame.image.load('images/home.png').convert_alpha()
    
    
    # Fonts Change hardcoded coordinates and sizes
    font = pygame.font.Font(None, 100)
    fontFront = font.render("Vector Vista", True, "White")
    font = pygame.font.Font(None, 30)
    Frontdisc = font.render("A powerful tool to intuitively learn linear algebra's components", True, "cyan")
    font = pygame.font.Font(None, 25)
    copyright = font.render("\u00A9OmSahu2023", True, "White")
    
    
    # Button instances change hardcoded coordinates and sizes
    start_button = mfun.button( (main_width/2) - 150 , main_height/2, start_img, 0.24)
    toggle = mfun.button(main_width - 120, 50, toggle_img, 0.115)
    detoggle = mfun.button(main_width - 123, 42, detoggle_img, 0.15)
    home = mfun.button(50, 40, home_img, 0.12)
        
    # Main loop
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if start: # Implementing graph
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
            h = screen.get_height()
            w = screen.get_width()
            o1 = origin_pos[0]
            o2 = origin_pos[1]
            constantx = math.sqrt( abs( h*h + w*w + 2*(o1*transformx[0] + o2*transformx[1]) - o1*o1 - o2*o2  ) / ( transformx[0]*transformx[0] + transformx[1]*transformx[1] ) ) 
            constanty = math.sqrt( abs( h*h + w*w + 2*(o1*transformy[0] + o2*transformy[1]) - o1*o1 - o2*o2 ) / ( transformy[0]*transformy[0] + transformy[1]*transformy[1] ) )
        
            convertx = transformx*constantx
            convertxn = transformx*constantx*(-1)
            converty = transformy*constanty
            convertyn = transformy*constanty*(-1)
        
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
                spacing += (spacing/3)*dt
            if keys[pygame.K_x]:
                if spacing > 10: # Maximum zoom out for memory reasons
                    spacing -= (spacing/3)*dt
            
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
                
            # toggle side screen
         
            if sideMenu == False:
                if toggle.draw(screen, 230):
                    graphCoord = (screen_main.get_width()/1.5, screen_main.get_height())
                    screen = pygame.transform.smoothscale(screen, graphCoord)
                    sideMenu = True
                    reset = True
                                    
            # Toggle home screen
            if home.draw(screen, 230):
                frontPage = True
                start = False
                sideMenu = False
            
                
         
        # Implementing Front page
        if frontPage:
            if start_button.draw(front, 5):
                screen_main.fill('black')
                sideMenu = True
                start = True
                frontPage = False
                reset = True
        

        # Screen pages 

        # Blits the front page Change hardcoded coordinates and sizes
        if frontPage:
            screen_main.blit(front, (0,0))
            screen_main.blit(fontFront, (main_width/2 - 200, main_height/2 - 200))
            screen_main.blit(Frontdisc, (main_width/2 - 300, main_height/2 - 100))
            screen_main.blit(copyright, (main_width/1.5, main_height/1.2))

        # Blits the graph
        if start:  
            screen_main.blit(screen, (0,0))
            
        # Blits the side section
        if sideMenu:
            screen_main.blit(menu, (screen.get_width(),0))
            
        # Implementing Side menu
        if sideMenu:   
            menu.fill((0,0,20))
            if detoggle.draw(screen_main, 230):
                graphCoord = (screen_main.get_width(), screen_main.get_height())
                screen = pygame.transform.smoothscale(screen, graphCoord)
                sideMenu = False
                reset = True

            
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