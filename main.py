# Final project

import pygame
import pygame_gui
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
    MANAGER = pygame_gui.UIManager((main_width, main_height)) # used for vector input boxes
    MANAGER2 = pygame_gui.UIManager((main_width, main_height)) # used for matrix input boxes

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
    resetp2 = False
    resetp3 = False
    resetp4 = False
    resetp5 = False
    resetp6 = False
    resetp7 = False
    resetp8 = False
    # page
    submit_vect1 = False
    invalid = False
    submit_vect2 = False
    invalid2 = False
    addition = False
    subtraction = False
    submit_matA = False
    invalid3 = False
    dobool = False
    dtbool = False

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
    
    add_img = pygame.image.load('images/menu/add.png').convert_alpha()
    dot_img = pygame.image.load('images/menu/dot.png').convert_alpha()
    linear_img = pygame.image.load('images/menu/linear.png').convert_alpha()
    eigen_img = pygame.image.load('images/menu/eigen.png').convert_alpha()
    determinant_img = pygame.image.load('images/menu/determinant.png').convert_alpha()
    matrix_img = pygame.image.load('images/menu/matrix.png').convert_alpha()
    diagonal_img = pygame.image.load('images/menu/diagonal.png').convert_alpha()
    back_img = pygame.image.load('images/menu/back.png').convert_alpha()
    submit_img = pygame.image.load('images/menu/submit.png').convert_alpha()
    page2add_img = pygame.image.load('images/menu/page2/add.png').convert_alpha()
    page2sub_img = pygame.image.load('images/menu/page2/sub.png').convert_alpha()
    reset_img = pygame.image.load('images/menu/reset.png').convert_alpha()
    
    page4_do_img = pygame.image.load('images/menu/page4/draw_original.png').convert_alpha()
    page4_dt_img = pygame.image.load('images/menu/page4/draw_transformed.png').convert_alpha()
    
    # Fonts Change hardcoded coordinates and sizes
    font = pygame.font.Font(None, 100)
    fontFront = font.render("Vector Vista", True, "White")
    font = pygame.font.Font(None, 30)
    Frontdisc = font.render("A powerful tool to intuitively learn linear algebra's components", True, "cyan")
    font = pygame.font.Font(None, 25)
    copyright = font.render("\u00A9OmSahu2023", True, "White")
    pageFont = pygame.font.Font(None, 30)
    vect2 = pageFont.render("Vector 2", True, "White")
    vect1 = pageFont.render("Vector 1", True, "White")
    pageFont = pygame.font.Font(None, 20)
    invalid_input = pageFont.render("INVALID INPUT", True, "Red")  
    page2Font = pygame.font.Font(None, 25)
    
    page3Font = pygame.font.Font(None, 150)
    matrix_bracket = page3Font.render("[     ]", True, "white")
    page3Font = pygame.font.Font(None, 30)
    matrixA_text = page3Font.render("Matrix A", True, "white")
    
    # input vector fonts
    pageFont = pygame.font.Font(None, 40)
    b1 = pageFont.render("(        ,        )", True, "white")

    # Button instances change hardcoded coordinates and sizes
    start_button = mfun.button( (main_width/2) - 150 , main_height/2, start_img, 0.24)
    toggle = mfun.button(main_width - 120, 50, toggle_img, 0.115)
    detoggle = mfun.button(main_width - 123, 42, detoggle_img, 0.15)
    home = mfun.button(50, 40, home_img, 0.12)
    
    add = mfun.button(main_width - 350, 100, add_img, 0.5)
    dot = mfun.button(main_width - 350, 200, dot_img, 0.5)
    linear = mfun.button(main_width - 350, 300, linear_img, 0.5)
    eigen = mfun.button(main_width - 350, 400, eigen_img, 0.5)
    determinant = mfun.button(main_width - 350, 500, determinant_img, 0.5)
    matrix = mfun.button(main_width - 350, 600, matrix_img, 0.5)
    diagonal = mfun.button(main_width - 350, 700, diagonal_img, 0.5)
    back = mfun.button(main_width - 400, 40, back_img, 0.08)
    submit = mfun.button(main_width/1.1, main_height/4, submit_img, 0.3 )
    submit2 = mfun.button(main_width/1.1, main_height/2.4, submit_img, 0.3 )
    submit3 = mfun.button(main_width/1.1, main_height/3.5, submit_img, 0.3 )
    
    # page2 buttons
    add_p2 = mfun.button(main_width/1.4, main_height/1.7, page2add_img, 0.3)
    sub_p2 = mfun.button(main_width/1.4, main_height/1.5, page2sub_img, 0.3)
    reset_p2 = mfun.button(main_width/1.4, main_height/1.3, reset_img, 0.3 )
    
    # page4 buttons
    do_p4 = mfun.button(main_width/1.4, main_height/1.8, page4_do_img, 0.4)
    dt_p4 = mfun.button(main_width/1.2, main_height/1.8, page4_dt_img, 0.4)

    
    # side menu pages
    page1 = True
    page2 = False
    page3 = False
    page4 = False
    page5 = False
    page6 = False
    page7 = False
    page8 = False
    
    # INPUT BOXES
    # MANAGER
    vector1x_input_rect = pygame.Rect(main_width/1.37, main_height/4, 50, 33)
    vector1y_input_rect = pygame.Rect(main_width/1.27, main_height/4, 50, 33)
    vector2x_input_rect = pygame.Rect(main_width/1.37, main_height/2.4, 50, 33)
    vector2y_input_rect = pygame.Rect(main_width/1.27, main_height/2.4, 50, 33)
    vector1x_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector1x_input_rect, manager=MANAGER, object_id='#vector1x') 
    vector1y_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector1y_input_rect, manager=MANAGER, object_id='#vector1y')
    vector2x_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector2x_input_rect, manager=MANAGER, object_id='#vector2x')
    vector2y_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector2y_input_rect, manager=MANAGER, object_id='#vector2y')
    # MANAGER2
    matrix1x = pygame.Rect(main_width/1.37, main_height/4, 50, 33)
    matrix1y = pygame.Rect(main_width/1.27, main_height/4, 50, 33)
    matrix2x = pygame.Rect(main_width/1.37, main_height/3, 50, 33)
    matrix2y = pygame.Rect(main_width/1.27, main_height/3, 50, 33)
    matrixA_1_input = pygame_gui.elements.UITextEntryLine(relative_rect=matrix1x, manager=MANAGER2, object_id='#matrixA1')
    matrixA_2_input = pygame_gui.elements.UITextEntryLine(relative_rect=matrix1y, manager=MANAGER2, object_id='#matrixA2')
    matrixA_3_input = pygame_gui.elements.UITextEntryLine(relative_rect=matrix2x, manager=MANAGER2, object_id='#matrixA3')
    matrixA_4_input = pygame_gui.elements.UITextEntryLine(relative_rect=matrix2y, manager=MANAGER2, object_id='#matrixA4')
    
    vectorax_input_rect = pygame.Rect(main_width/1.37, main_height/2.2, 50, 33)
    vectoray_input_rect = pygame.Rect(main_width/1.27, main_height/2.2, 50, 33)
    vectorax_input = pygame_gui.elements.UITextEntryLine(relative_rect=vectorax_input_rect, manager=MANAGER2, object_id='#vectorax')
    vectoray_input = pygame_gui.elements.UITextEntryLine(relative_rect=vectoray_input_rect, manager=MANAGER2, object_id='#vectoray')
    
    # pages variable initialization
    vector1 = (0,0)
    vector2 = (0,0)
    add_text = "Addition"
    sub_text = "Subtraction"
    vector13 = (1,0)
    vector23 = (0,0) 
    dot_product = "Dot Product"
    page2_heading = "ADDITION AND SUBTRACTION"
    page3_heading = "DOT PRODUCT"
    page4_heading = "LINEAR TRANSFORMATION"
    matAbx = (1, 0)
    matAby = (0, 1)
    vector14 = (0,0)
    vector24 = (0,0)

    # Main loop
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            MANAGER.process_events(event)
            MANAGER2.process_events(event)

        MANAGER.update(dt)
        MANAGER2.update(dt)
        
        

        if start: # Implementing graph
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("black")
    
            # Standard grids 
            keys = pygame.key.get_pressed()
            grid_color = (65, 136, 165)  

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
            constantx = math.sqrt( abs( h*h + w*w + 2*(o1*transformx[0] + o2*transformx[1]) - o1*o1 - o2*o2  ) / ( transformx[0]*transformx[0] + 1 + transformx[1]*transformx[1] ) ) 
            constanty = math.sqrt( abs( h*h + w*w + 2*(o1*transformy[0] + o2*transformy[1]) - o1*o1 - o2*o2 ) / ( transformy[0]*transformy[0] + 1 + transformy[1]*transformy[1] ) )
        
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


            # PAGES OPERATIONS IMPLEMENTATION

            # Page 2 OPERATIONS
            if page2:
                if invalid == False:
                    mfun.draw_bvector(screen, origin_pos, vector1, transformx, transformy, spacing, (0, 255, 0)) 
                if invalid2 == False:
                    mfun.draw_bvector(screen, origin_pos, vector2, transformx, transformy, spacing, (0, 0, 255)) 
                if addition and not invalid and not invalid2:
                    vector3 = (vector1[0] + vector2[0], vector1[1] + vector2[1])
                    add_text = str(vector3)
                    mfun.draw_bvector(screen, origin_pos, vector3, transformx, transformy, spacing, (255, 0, 255)) 
                if subtraction and not invalid and not invalid2:
                    vector4 = (vector1[0] - vector2[0], vector1[1] - vector2[1])
                    sub_text = str(vector4)
                    mfun.draw_bvector(screen, origin_pos, vector4, transformx, transformy, spacing, (255, 0, 0)) 
                    
            # Page 3 OPERATIONS
            if page3:
                # Transform grid
                if invalid == False:
                    transformx = pygame.Vector2(vector13[0], vector13[1])
                    transformy = pygame.Vector2(0, 0)
                # Draw transformed vector 
                if invalid2 == False:
                    mfun.draw_bvector(screen, origin_pos, vector23, transformx, transformy, spacing, (255, 0, 0)) 
                if not invalid2 and not invalid:
                    dot_product = "Dot product = " + str(vector13[0]*vector23[0] + vector13[1]*vector23[1])
                    
            # Page 4 OPERATIONS
            if page4:
                # Transform grid
                if invalid3 == False:
                    transformx = pygame.Vector2(matAbx[0], matAbx[1])
                    transformy = pygame.Vector2(matAby[0], matAby[1])
                if invalid2 == False:
                    if dobool:
                        draw_vector(screen, origin_pos, vector14, spacing, "green")
                    if dtbool:
                        mfun.draw_bvector(screen, origin_pos, vector24, transformx, transformy, spacing, "red")
                
                

            # (Make effects function of spacing, future implementation)
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
                                                 
            if page1: # Front page of menu 
                if add.draw(screen_main, 170):
                    page1 = False
                    page2 = True
                if dot.draw(screen_main, 170):
                    page1 = False
                    page3 = True
                if linear.draw(screen_main, 170):
                    page1 = False
                    page4 = True
                if eigen.draw(screen_main, 170):
                    page1 = False
                    page5 = True
                if determinant.draw(screen_main, 170):
                    page1 = False
                    page6 = True
                if matrix.draw(screen_main, 170):
                    page1 = False
                    page7 = True
                if diagonal.draw(screen_main, 170):
                    page1 = False
                    page8 = True
                    
            if page2: # Vector addition and subtraction 
                # Take input Vector 1 and 2
                screen_main.blit(vect1, (main_width/1.4, main_height/4.7))
                MANAGER.draw_ui(screen_main)
                vector1x = vector1x_input.get_text()
                vector1y = vector1y_input.get_text()
                vector2x = vector2x_input.get_text()
                vector2y = vector2y_input.get_text()
                
                screen_main.blit(b1, (main_width/1.4, main_height/4))
                screen_main.blit(b1, (main_width/1.4, main_height/2.4))
                if invalid:
                    screen_main.blit(invalid_input, (main_width/1.398, main_height/3.2))
                if submit.draw(screen_main, 200):
                    submit_vect1 = True
                if submit_vect1:    
                    vector1 = mfun.float_convert((vector1x, vector1y))
                    if vector1 == "invalid":
                        submit_vect1 = False
                        invalid = True 
                        addition = False
                        subtraction = False
                    else: 
                        invalid = False
                        submit_vect1 = False
                        
                screen_main.blit(vect2, (main_width/1.4, main_height/2.7))
                if invalid2:
                    screen_main.blit(invalid_input, (main_width/1.398, main_height/2))
                if submit2.draw(screen_main, 200):
                    submit_vect2 = True
                if submit_vect2:
                    vector2 = mfun.float_convert((vector2x, vector2y))
                    if vector2 == "invalid":
                        submit_vect2 = False
                        invalid2 = True
                        addition = False
                        subtraction = False
                    else:
                        invalid2 = False
                        submit_vect2 = False
                if add_p2.draw(screen_main, 200):
                    addition = True
                    
                if sub_p2.draw(screen_main, 200):
                    subtraction = True
                    
                if reset_p2.draw(screen_main, 200):
                    resetp2 = True
                    
                page2_head = page2Font.render(page2_heading, True, "White")
                addp2 = page2Font.render(add_text, True, "White")
                subp2 = page2Font.render(sub_text, True, "White")
                screen_main.blit(addp2, (main_width/1.2, main_height/1.65) )
                screen_main.blit(subp2, (main_width/1.2, main_height/1.45) )  
                screen_main.blit(page2_head, (main_width/1.39, main_height/24) )  
                                                                 
            if page3: # Dot product of two vectors
                # Input space of two vectors
                screen_main.blit(vect1, (main_width/1.4, main_height/4.7))
                MANAGER.draw_ui(screen_main)
                vector1x = vector1x_input.get_text()
                vector1y = vector1y_input.get_text()
                vector2x = vector2x_input.get_text()
                vector2y = vector2y_input.get_text()
                
                screen_main.blit(b1, (main_width/1.4, main_height/4))
                screen_main.blit(b1, (main_width/1.4, main_height/2.4))
                if invalid:
                    screen_main.blit(invalid_input, (main_width/1.398, main_height/3.2))
                if submit.draw(screen_main, 200):
                    submit_vect1 = True
                if submit_vect1:    
                    vector13 = mfun.float_convert((vector1x, vector1y))
                    if vector13 == "invalid":
                        submit_vect1 = False
                        invalid = True 
                    else: 
                        invalid = False
                        submit_vect1 = False
                        
                screen_main.blit(vect2, (main_width/1.4, main_height/2.7))
                if invalid2:
                    screen_main.blit(invalid_input, (main_width/1.398, main_height/2))
                if submit2.draw(screen_main, 200):
                    submit_vect2 = True
                if submit_vect2:
                    vector23 = mfun.float_convert((vector2x, vector2y))
                    if vector23 == "invalid":
                        submit_vect2 = False
                        invalid2 = True
                    else:
                        invalid2 = False
                        submit_vect2 = False
                        
                dot_text = page2Font.render(dot_product, True, "white")
                screen_main.blit(dot_text, (main_width/1.4, main_height/1.65))
                page3_head = page2Font.render(page3_heading, True, "White") 
                screen_main.blit(page3_head, (main_width/1.3, main_height/24) )  

                if reset_p2.draw(screen_main, 200):
                    resetp3 = True
    
            if page4: # Linear transformation and transformed vectors 
                # Input space of matrix A
                screen_main.blit(matrix_bracket, (main_width/1.45, main_height/4.15))
                MANAGER2.draw_ui(screen_main)    
                matrixA_1 = matrixA_1_input.get_text()
                matrixA_2 = matrixA_2_input.get_text()
                matrixA_3 = matrixA_3_input.get_text()
                matrixA_4 = matrixA_4_input.get_text()
                screen_main.blit(matrixA_text, (main_width/1.45, main_height/4.7))
                
                if submit3.draw(screen_main, 200):
                    submit_matA = True

                if submit_matA:
                    matAbx = mfun.float_convert((matrixA_1, matrixA_3))
                    matAby = mfun.float_convert((matrixA_2, matrixA_4))
                    if matAbx == "invalid" or matAby == "invalid":
                        invalid3 = True
                        submit_matA = False
                    else:
                        invalid3 = False
                        submit_matA = False
                if invalid3:
                    screen_main.blit(invalid_input, (main_width/1.3, main_height/2.6))   
                    
                # Vector input space
                vectorax = vectorax_input.get_text()
                vectoray = vectoray_input.get_text()
                screen_main.blit(b1, (main_width/1.4, main_height/2.2))
                
                screen_main.blit(vect1, (main_width/1.45, main_height/2.5))
                if invalid2:
                    screen_main.blit(invalid_input, (main_width/1.398, main_height/2))
                if do_p4.draw(screen_main, 200):
                    submit_vect2 = True
                    dobool = True
                if submit_vect2:
                    vector14 = mfun.float_convert((vectorax, vectoray))
                    vector24 = mfun.float_convert((vectorax, vectoray))
                    if vector14 == "invalid":
                        submit_vect2 = False
                        invalid2 = True
                        dobool = False
                        dtbool = False
                    else:
                        invalid2 = False
                        submit_vect2 = False

                if dt_p4.draw(screen_main, 200):
                    submit_vect2 = True
                    dtbool = True
                 
                page4_head = page2Font.render(page4_heading, True, "White")    
                screen_main.blit(page4_head, (main_width/1.37, main_height/24) )
                
                if reset_p2.draw(screen_main, 200):
                    resetp4 = True

            if page5:
                x=0
            if page6:
                x=0    
            if page7:
                x=0
                
            # PAGE RESETS
            if resetp2:
                resetp2 = False
                invalid = False
                invalid2 = False
                submit_vect1 = False
                submit_vect2 = False
                vector1x_input.kill()
                vector1y_input.kill()
                vector2x_input.kill()
                vector2y_input.kill()
                vector1x_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector1x_input_rect, manager=MANAGER, object_id='#vector1x') 
                vector1y_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector1y_input_rect, manager=MANAGER, object_id='#vector1y')
                vector2x_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector2x_input_rect, manager=MANAGER, object_id='#vector2x')
                vector2y_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector2y_input_rect, manager=MANAGER, object_id='#vector2y')
                vector1 = (0,0)
                vector2 = (0,0)
                addition = False
                subtraction = False
                add_text = "Addition"
                sub_text = "Subtraction"
                
            if resetp3:
                resetp3 = False
                vector13 = (1, 0)
                vector23 = (0, 0)
                invalid = False
                invalid2 = False
                submit_vect1 = False
                submit_vect2 = False
                vector1x_input.kill()
                vector1y_input.kill()
                vector2x_input.kill()
                vector2y_input.kill()
                vector1x_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector1x_input_rect, manager=MANAGER, object_id='#vector1x') 
                vector1y_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector1y_input_rect, manager=MANAGER, object_id='#vector1y')
                vector2x_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector2x_input_rect, manager=MANAGER, object_id='#vector2x')
                vector2y_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector2y_input_rect, manager=MANAGER, object_id='#vector2y')
                
            if resetp4:
                resetp4 = False
                submit_matA = False
                invalid3 = False
                matAbx = (1, 0)
                matAby = (0, 1)
                matrixA_1_input.kill()    
                matrixA_2_input.kill()    
                matrixA_3_input.kill()    
                matrixA_4_input.kill() 
                matrixA_1_input = pygame_gui.elements.UITextEntryLine(relative_rect=matrix1x, manager=MANAGER2, object_id='#matrixA1')
                matrixA_2_input = pygame_gui.elements.UITextEntryLine(relative_rect=matrix1y, manager=MANAGER2, object_id='#matrixA2')
                matrixA_3_input = pygame_gui.elements.UITextEntryLine(relative_rect=matrix2x, manager=MANAGER2, object_id='#matrixA3')
                matrixA_4_input = pygame_gui.elements.UITextEntryLine(relative_rect=matrix2y, manager=MANAGER2, object_id='#matrixA4')
                dobool = False
                dtbool = False
                invalid2 = False
                vector14 = (0,0)
                vector24 = (0,0)
                vectorax_input.kill()
                vectoray_input.kill()
                vectorax_input = pygame_gui.elements.UITextEntryLine(relative_rect=vectorax_input_rect, manager=MANAGER2, object_id='#vectorax')
                vectoray_input = pygame_gui.elements.UITextEntryLine(relative_rect=vectoray_input_rect, manager=MANAGER2, object_id='#vectoray')
                
            if page1 == False:
                if back.draw(screen_main, 230):
                    page1 = True
                    page2 = False
                    page3 = False
                    page4 = False
                    page5 = False
                    page6 = False
                    page7 = False
                    page8 = False
                    
                    # reset page variables to be recycled again
                    transformx = pygame.Vector2(1,0)
                    transformy = pygame.Vector2(0,1)
                    resetp2 = True
                    resetp3 = True
                    resetp4 = True
                    
                
        # flip() the display to put your work on screen
        pygame.display.flip()

        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(30) / 1000

    pygame.quit()


def draw_vector(screen, origin, vector, spacing, color, width = 3):
    # draw vector from origin in original basis 
    vector = (vector[0]*spacing + origin[0], (origin[1] - vector[1]*spacing))
    pygame.draw.line(screen, color, origin, vector, width)
    
    

main()