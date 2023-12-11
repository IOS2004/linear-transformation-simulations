# Final project

import pygame
import pygame_gui
import functions as mfun
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
    pygame.display.set_caption("Vesmos")
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
    # page bools
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
    cyclep7 = False # Checks whether Cycle is completed or not

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
    diagonal_img = pygame.image.load('images/menu/diagonal.png').convert_alpha()
    back_img = pygame.image.load('images/menu/back.png').convert_alpha()
    submit_img = pygame.image.load('images/menu/submit.png').convert_alpha()
    page2add_img = pygame.image.load('images/menu/page2/add.png').convert_alpha()
    page2sub_img = pygame.image.load('images/menu/page2/sub.png').convert_alpha()
    reset_img = pygame.image.load('images/menu/reset.png').convert_alpha()
    
    page4_do_img = pygame.image.load('images/menu/page4/draw_original.png').convert_alpha()
    page4_dt_img = pygame.image.load('images/menu/page4/draw_transformed.png').convert_alpha()
    
    # Fonts 
    font = pygame.font.Font("images/Gotham-Font/GothamMedium.ttf", 100)
    fontFront = font.render("Vesmos", True, "cyan")
    font = pygame.font.Font("images/Gotham-Font/GothamBook.ttf", 30)
    Frontdisc = font.render("A powerful tool to intuitively learn linear algebra's components", True, "cyan")
    font = pygame.font.Font("images/winterSong.ttf", 25)
    copyright = font.render("Made By Om Sahu", True, "White")
    pageFont = pygame.font.Font("images/Gotham-Font/GothamBook.ttf", 30)
    vect2 = pageFont.render("Vector 2", True, "White")
    vect1 = pageFont.render("Vector 1", True, "White")
    pageFont = pygame.font.Font(None, 20)
    invalid_input = pageFont.render("INVALID INPUT", True, "Red")  
    page2Font = pygame.font.Font("images/Gotham-Font/GothamBook.ttf", 20)
    page2Font_normal = pygame.font.Font(None, 30)
    
    page3Font = pygame.font.Font(None, 150)
    matrix_bracket = page3Font.render("[     ]", True, "white")
    page3Font = pygame.font.Font("images/Gotham-Font/GothamBook.ttf", 30)
    matrixA_text = page3Font.render("Matrix A", True, "white")
    eigen1_text = page2Font.render("Eigen Vectors", True, "White")
    eigen2_text = page2Font.render("Eigen Values", True, "White")
    font = pygame.font.Font("images/Gotham-Font/GothamBook.ttf", 15)
    madeby = font.render("MADE BY OM SAHU", True, "cyan")
    page2Font2 = pygame.font.Font("images/Gotham-Font/GothamBook.ttf", 100)
    
    # input vector fonts
    pageFont = pygame.font.Font(None, 40)
    b1 = pageFont.render("(        ,        )", True, "white")

    # Button instances 
    start_button = mfun.button( (main_width/2) - 125 , main_height/2, start_img, 0.24)
    toggle = mfun.button(main_width - 120, 50, toggle_img, 0.115)
    detoggle = mfun.button(main_width - 123, 42, detoggle_img, 0.15)
    home = mfun.button(50, 40, home_img, 0.12)
    
    add = mfun.button(main_width - 350, 100, add_img, 0.5)
    dot = mfun.button(main_width - 350, 200, dot_img, 0.5)
    linear = mfun.button(main_width - 350, 300, linear_img, 0.5)
    eigen = mfun.button(main_width - 350, 400, eigen_img, 0.5)
    determinant = mfun.button(main_width - 350, 500, determinant_img, 0.5)
    diagonal = mfun.button(main_width - 350, 600, diagonal_img, 0.5)
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
    
    # INPUT BOXES
    # MANAGER 2 Vector input boxes
    vector1x_input_rect = pygame.Rect(main_width/1.37, main_height/4, 50, 33)
    vector1y_input_rect = pygame.Rect(main_width/1.27, main_height/4, 50, 33)
    vector2x_input_rect = pygame.Rect(main_width/1.37, main_height/2.4, 50, 33)
    vector2y_input_rect = pygame.Rect(main_width/1.27, main_height/2.4, 50, 33)
    vector1x_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector1x_input_rect, manager=MANAGER, object_id='#vector1x') 
    vector1y_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector1y_input_rect, manager=MANAGER, object_id='#vector1y')
    vector2x_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector2x_input_rect, manager=MANAGER, object_id='#vector2x')
    vector2y_input = pygame_gui.elements.UITextEntryLine(relative_rect=vector2y_input_rect, manager=MANAGER, object_id='#vector2y')
    
    # MANAGER2 Matrix and a vector input box
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
    page5_heading = "EIGEN VALUES AND VECTORS"
    page6_heading = "DETERMINANT"
    page7_heading = "DIAGONALIZATION"
    matAbx = (1, 0)
    matAby = (0, 1)
    vector14 = (0,0)
    vector24 = (0,0)
    l1 = 1
    l2 = 1
    E1 = "(R1, R2)"
    E2 = "(R1, R2)"
    lamda1 = "1"
    lamda2 = "1"
    D_value = 1
    n = 0
    diagonalised = True
    diagonalizable = True
    last_action_time = pygame.time.get_ticks()
    
    # Dragging variables
    dragging = False
    offset_x, offset_y = 0, 0

    # Main loop
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[0] <= screen.get_width() and event.pos[1] <= screen.get_height():
                        dragging = True
                        offset_x = origin_pos[0] - event.pos[0]
                        offset_y = origin_pos[1] - event.pos[1]
                if event.button == 4:
                    spacing += (spacing*5)*dt  
                if event.button == 5:
                    if spacing > 10: # Maximum zoom out for memory reasons
                        spacing -= (spacing*5)*dt    
                        
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    origin_pos[0] = event.pos[0] + offset_x 
                    origin_pos[1] = event.pos[1] + offset_y  
                    
            MANAGER.process_events(event)
            MANAGER2.process_events(event)      

        MANAGER.update(dt)
        MANAGER2.update(dt)
        
        if start: # Implementing graph
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("black")
    
            # Standard grids 
            keys = pygame.key.get_pressed()
            grid_color = (95, 166, 195)  

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
                    mfun.draw_bvector(screen, origin_pos, vector4, transformx, transformy, spacing, "orange") 
                    
            # Page 3 OPERATIONS
            if page3:
                # Transform grid
                if invalid == False:
                    transformx = pygame.Vector2(vector13[0], vector13[1])
                    transformy = pygame.Vector2(0, 0)
                # Draw transformed vector 
                if invalid2 == False:
                    mfun.draw_bvector(screen, origin_pos, vector23, transformx, transformy, spacing, "orange") 
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
                        mfun.draw_bvector(screen, origin_pos, vector14, (1, 0), (0, 1), spacing, "green")
                    if dtbool:
                        mfun.draw_bvector(screen, origin_pos, vector24, transformx, transformy, spacing, "red")
            
            # Page 5 OPERATIONS
            if page5:
                if invalid3 == False:
                    # Transform grid
                    transformx = pygame.Vector2(matAbx[0], matAbx[1])
                    transformy = pygame.Vector2(matAby[0], matAby[1])
                
                    # Calculate Eigen values
                    lamda1, lamda2 = mfun.solve_quadratic(1, -(matAbx[0] + matAby[1]), (matAbx[0]*matAby[1] - matAby[0]*matAbx[1]))
                    if lamda1 == None:
                        lamda1 = "Complex"
                        lamda2 = "Complex"
                    else:
                        l1 = lamda1
                        l2 = lamda2
                        lamda1 = str(round(lamda1, 3))
                        lamda2 = str(round(lamda2, 3))
                    # Calculate Eigen vectors
                    if l1 == l2:
                        if matAby[0] == 0:
                           e1 = (0, 0) 
                        else:
                            e1 = ( 1, (l1 - matAbx[0])/matAby[0])
                        if matAby[1] - l1 == 0:
                            e2 = (0, 0)
                        else:    
                            e2 = ( 1, (-matAbx[1] / (matAby[1] - l1) ))
                            
                    if l1 != l2:
                        if matAby[0] == 0:
                            e1 = (0, 0)
                            e2 = e1
                        else:
                            e1 = ( 1, (l1 - matAbx[0])/matAby[0])
                            e2 = ( 1, (l2 - matAbx[0])/matAby[0])
                    e1 = (round(e1[0], 3), round(e1[1], 3))
                    e2 = (round(e2[0], 3), round(e2[1], 3))
                    
                    # Draw eigen vectors
                    if lamda1 != "Complex":
                        eigen1 = pygame.Vector2(e1[0], e1[1])
                        eigen2 = pygame.Vector2(e2[0], e2[1])
                        constante1 = math.sqrt( abs( h*h + w*w + 2*(o1*eigen1[0] + o2*eigen1[1]) - o1*o1 - o2*o2  ) / ( e1[0]*eigen1[0] + 1 + eigen1[1]*eigen1[1] ) ) 
                        constante2 = math.sqrt( abs( h*h + w*w + 2*(o1*eigen2[0] + o2*eigen2[1]) - o1*o1 - o2*o2  ) / ( e1[0]*eigen2[0] + 1 + eigen2[1]*eigen2[1] ) )
                        converte1 = eigen1*constante1
                        converte1n = eigen1*constante1*(-1)
                        converte2 = eigen2*constante2
                        converte2n = eigen2*constante2*(-1)
                    
                        # For e1 we have
                        draw_vector(screen, origin_pos, converte1, spacing, "green")
                        draw_vector(screen, origin_pos, converte1n, spacing, "green")
        
                        # e2 axis we have     
                        draw_vector(screen, origin_pos, converte2, spacing, "green")
                        draw_vector(screen, origin_pos, converte2n, spacing, "green")
                    
                    if lamda1 == "Complex":
                        E1 = "Complex"
                        E2 = "Complex"
                    elif matAby[0] == 0 and matAby[1] - l2 == 0:
                            E1 = "(R1, R2)"
                            E2 = "(R1, R2)"
                    else:
                        E1 = "k " + str(e1)
                        E2 = "k " + str(e2)
            
            # Page 6 OPERATIONS
            if page6:
                if invalid3 == False:
                    # Transform grid
                    transformx = pygame.Vector2(matAbx[0], matAbx[1])
                    transformy = pygame.Vector2(matAby[0], matAby[1])
                    D_value = matAbx[0]*matAby[1] - matAbx[1] * matAby[0]                    

                fourth = mfun.pgfourth_point((0,0), transformx, transformy, )
                pygame.draw.polygon(screen, "orange", [ origin_pos, mfun.convert(transformx, spacing, origin_pos), mfun.convert(fourth, spacing, origin_pos), mfun.convert(transformy, spacing, origin_pos) ])
                
            # Page 7 OPERATIONS
            if page7:
                if invalid3 == False:      
                    # Calculate Eigen values
                    lamda1, lamda2 = mfun.solve_quadratic(1, -(matAbx[0] + matAby[1]), (matAbx[0]*matAby[1] - matAby[0]*matAbx[1]))
                    if lamda1 == None:
                        diagonalizable = False
                        diagonalised = False
                    else:
                        l1 = lamda1
                        l2 = lamda2

                    # Calculate Eigen vectors
                    if l1 == l2:
                        if matAby[0] == 0 and matAby[1] - l2 == 0:
                            diagonalised = True
                            diagonalizable = True
                        else:
                            diagonalizable = False   
                            diagonalised = False
                    if l1 != l2:
                        if matAby[0] == 0:
                            e1 = (0, 0)
                            e2 = e1 
                            diagonalised = False
                            diagonalizable = False
                        elif matAby[0] == 0 and matAby[1] - l2 == 0:
                            diagonalised = True
                            diagonalizable = True
                        else:
                            e1 = ( 1, (l1 - matAbx[0])/matAby[0])
                            e2 = ( 1, (l2 - matAbx[0])/matAby[0])
                            diagonalised = False
                            diagonalizable = True
                    if diagonalizable and not diagonalised:
                        # A matrix
                        matrixA = mfun.matrix(matAbx[0], matAby[0], matAbx[1], matAby[1])
                        # Calculate P    
                        matrixP = mfun.matrix(e1[0], e2[0], e1[1], e2[1])
                        # Calculate P-1
                        matrixPn = matrixP.inverse()
                        # Calculate D
                        matrixD = mfun.matrix(l1, 0, 0, l2)

                        # Now one by one tranform grids
                        if n == 1:
                            transformx = pygame.Vector2(matrixP.a, matrixP.c)
                            transformy = pygame.Vector2(matrixP.b, matrixP.d)
                                
                        if n == 2: 
                            matrixB = matrixA.multiply(matrixP)
                            transformx = pygame.Vector2(matrixB.a, matrixB.c)
                            transformy = pygame.Vector2(matrixB.b, matrixB.d)
                                
                        if n == 3:
                            matrixB = matrixD
                            transformx = pygame.Vector2(matrixB.a, matrixB.c)
                            transformy = pygame.Vector2(matrixB.b, matrixB.d)
                            cyclep7 = True

            # (Make effects function of spacing, future implementation)
            # zoom effect
            if keys[pygame.K_z]:
                spacing += (spacing/3)*dt
            if keys[pygame.K_x]:
                if spacing > 10: # Maximum zoom out for memory reasons
                    spacing -= (spacing/3)*dt
            
            # drag effect 
            if keys[pygame.K_d]:
                origin_pos[0] += 300*dt
            if keys[pygame.K_a]:
                origin_pos[0] -= 300*dt
            if keys[pygame.K_w]:
                origin_pos[1] -= 300*dt
            if keys[pygame.K_s]:
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
        
        # Blits the front page Change hardcoded coordinates and sizes
        if frontPage:
            screen_main.blit(front, (0,0))
            screen_main.blit(fontFront, (main_width/2 - 200, main_height/2 - 200))
            screen_main.blit(Frontdisc, (main_width/2 - 450, main_height/2 - 100))
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
            screen_main.blit(madeby, (main_width - 300, 720))
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
                if diagonal.draw(screen_main, 170):
                    page1 = False
                    page7 = True
                    
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
                screen_main.blit(page2_head, (main_width/1.43, main_height/26) )  
                                                                 
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
                screen_main.blit(page3_head, (main_width/1.32, main_height/26) )  

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
                screen_main.blit(matrixA_text, (main_width/1.45, main_height/4.9))
                
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
                screen_main.blit(page4_head, (main_width/1.40, main_height/26) )
                
                if reset_p2.draw(screen_main, 200):
                    resetp4 = True

            if page5: # Eigen Values and Vectors of 2x2 Matrix 
                # Kill vector input space, we only need matrix input space
                vectorax_input.kill()
                vectoray_input.kill()
                # Matrix A input space
                screen_main.blit(matrix_bracket, (main_width/1.45, main_height/4.15))
                MANAGER2.draw_ui(screen_main)    
                matrixA_1 = matrixA_1_input.get_text()
                matrixA_2 = matrixA_2_input.get_text()
                matrixA_3 = matrixA_3_input.get_text()
                matrixA_4 = matrixA_4_input.get_text()
                screen_main.blit(matrixA_text, (main_width/1.45, main_height/4.9))   
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
                # Print values
                eigen_values = page2Font_normal.render("\u03BB1 = " + lamda1 + "           " + "\u03BB2 = " + lamda2, True, "white")
                eigen_vectors = page2Font.render("E1 = " + E1 + "    " + "E2 = " + E2, True, "white")
                screen_main.blit(eigen_values, (main_width/1.45, main_height/1.77))
                screen_main.blit(eigen_vectors, (main_width/1.45, main_height/1.5))
                screen_main.blit(eigen1_text, (main_width/1.45, main_height/1.6))
                screen_main.blit(eigen2_text, (main_width/1.45, main_height/1.9))
                
                page5_head = page2Font.render(page5_heading, True, "White")    
                screen_main.blit(page5_head, (main_width/1.43, main_height/26) )
                
                if reset_p2.draw(screen_main, 200):
                    resetp5 = True

            if page6: # Determinant of 2x2 Matrix 
                # Kill vector input space, we only need matrix input space
                vectorax_input.kill()
                vectoray_input.kill()
                # Matrix A input space
                screen_main.blit(matrix_bracket, (main_width/1.45, main_height/4.15))
                MANAGER2.draw_ui(screen_main)    
                matrixA_1 = matrixA_1_input.get_text()
                matrixA_2 = matrixA_2_input.get_text()
                matrixA_3 = matrixA_3_input.get_text()
                matrixA_4 = matrixA_4_input.get_text()
                screen_main.blit(matrixA_text, (main_width/1.45, main_height/4.9))   
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
                    
                D_text = page2Font.render(f"Determinant = {D_value}", True, "white")
                screen_main.blit( D_text, (main_width/1.45, main_height/1.77) )
                    
                page6_head = page2Font.render(page6_heading, True, "White")    
                screen_main.blit(page6_head, (main_width/1.35, main_height/26) )

                if reset_p2.draw(screen_main, 200):
                    resetp6 = True    
                 
            if page7: # Diagonalization of 2x2 Matrix 
                # Kill vector input space, we only need matrix input space
                vectorax_input.kill()
                vectoray_input.kill()
                # Input space of matrix A
                screen_main.blit(matrix_bracket, (main_width/1.45, main_height/4.15))
                MANAGER2.draw_ui(screen_main)    
                matrixA_1 = matrixA_1_input.get_text()
                matrixA_2 = matrixA_2_input.get_text()
                matrixA_3 = matrixA_3_input.get_text()
                matrixA_4 = matrixA_4_input.get_text()
                screen_main.blit(matrixA_text, (main_width/1.45, main_height/4.9))
                
                if submit3.draw(screen_main, 200):
                    submit_matA = True
                    cyclep7 = False

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
                    
                current_time = pygame.time.get_ticks()
                if current_time - last_action_time >= 1000:
                    last_action_time = current_time
                    
                    if diagonalizable and not diagonalised and cyclep7 == False:
                        n += 1
                    else:
                        n = 0
                 
                # Draw matrix
                matrix_bracketD = page2Font2.render("D [     ]", True, "white")
                screen_main.blit(matrix_bracketD, (main_width/1.46, main_height/2.2))
                if diagonalizable and not diagonalised:
                    mfun.draw_matrix(screen_main, matrixD, main_width/1.21, main_height/2.1 )  
                    
                if diagonalizable == False:
                    text_diagonal = page2Font.render('Not Diagonalizable', True, "red")
                    screen_main.blit(text_diagonal, (main_width/1.37, main_height/2.42)) 
                if diagonalizable == True and diagonalised == True or cyclep7 == True:
                    text_diagonalised = page2Font.render('Diagonalised', True, "green")
                    screen_main.blit(text_diagonalised, (main_width/1.37, main_height/2.42)) 
                    
                page7_head = page2Font.render(page7_heading, True, "White")    
                screen_main.blit(page7_head, (main_width/1.35, main_height/26) )
                
                if n == 0:
                    page7_D = page2Font.render("D = ", True, "White") 
                    page7_Pn = page2Font.render("P^-1 ", True, "White")
                    page7_A = page2Font.render("A", True, "White")
                    page7_P = page2Font.render("P", True, "White")
                
                if n == 1:
                    page7_P = page2Font.render("P", True, "green")
                    page7_D = page2Font.render("D = ", True, "White") 
                    page7_Pn = page2Font.render("P^-1", True, "White")
                    page7_A = page2Font.render("A", True, "White")
                    
                if n == 2:
                    page7_D = page2Font.render("D =", True, "White") 
                    page7_Pn = page2Font.render("P^-1", True, "White")
                    page7_A = page2Font.render("A", True, "green")
                    page7_P = page2Font.render("P", True, "green")
                    
                if n == 3 or cyclep7:
                    page7_D = page2Font.render("D =  ", True, "cyan") 
                    page7_Pn = page2Font.render("P^-1 ", True, "green")
                    page7_A = page2Font.render("A", True, "green")
                    page7_P = page2Font.render("P", True, "green")

                screen_main.blit(page7_D, (main_width - 350, main_height / 1.5))
                screen_main.blit(page7_P, (main_width - 215, main_height / 1.5))
                screen_main.blit(page7_A, (main_width - 250, main_height / 1.5))
                screen_main.blit(page7_Pn, (main_width - 305, main_height / 1.5))

                if reset_p2.draw(screen_main, 200):
                    resetp7 = True    
                
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

            if resetp5:
                resetp5 = False
                invalid3 = False
                submit_matA = False
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
                l1 = 1
                l2 = 1
                E1 = "(R1, R2)"
                E2 = "(R1, R2)"
                lamda1 = "1"
                lamda2 = "1"
                
            if resetp6:
                resetp6 = False
                invalid3 = False
                submit_matA = False
                D_value = 1
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
             
            if resetp7: 
                resetp7 = False
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
                cyclep7 = False
                n = 0
                diagonalised = True
                diagonalizable = True
                transformx = pygame.Vector2(1,0)
                transformy = pygame.Vector2(0,1)

            if page1 == False:
                if back.draw(screen_main, 230):
                    page1 = True
                    page2 = False
                    page3 = False
                    page4 = False
                    page5 = False
                    page6 = False
                    page7 = False
                    
                    # reset page variables to be recycled again
                    transformx = pygame.Vector2(1,0)
                    transformy = pygame.Vector2(0,1)
                    resetp2 = True
                    resetp3 = True
                    resetp4 = True
                    resetp5 = True
                    resetp6 = True
                    resetp7 = True                    
                
        # flip() the display to put your work on screen
        pygame.display.flip()

        # dt is delta time in seconds since last frame, used for framerate-
        dt = clock.tick(60) / 1000

    pygame.quit()

def draw_vector(screen, origin, vector, spacing, color, width = 3):
    # draw vector from origin in original basis 
    vector = (vector[0]*spacing + origin[0], (origin[1] - vector[1]*spacing))
    pygame.draw.aaline(screen, color, origin, vector)
    
main()