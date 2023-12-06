import math
import pygame

def convert(vector, spacing, origin):
    # convert point back to original coordinate system
    vector = (vector[0]*spacing + origin[0], (origin[1] - vector[1]*spacing))
    return vector

def convert_reverse(vector, spacing, origin):
    # convert coordinate point to our coordinate system
    vector = ((vector[0] - origin[0]) / spacing, (origin[1] - vector[1]) / spacing)
    return vector

def find(x1, y1, slope, magnitude):
    # Finds the end point helper function for parallel line
    x = x1 + magnitude * (1 / math.sqrt(1 + slope**2))
    y = y1 + slope * magnitude * (1 / math.sqrt(1 + slope**2))
    end = (x, y)
    return end

def findn(x1, y1, slope, magnitude):
    # Finds the end point helper function for parallel line (Produce alternate end point as equation has two solutions)
    x = x1 - magnitude * (1 / math.sqrt(1 + slope**2))
    y = y1 - slope * magnitude * (1 / math.sqrt(1 + slope**2))
    end = (x, y)
    return end

def angle_lines(m1, m2): # Angle between two lines of slope m1 & m2 in radians
    if (m1*m2 == -1):
        return math.radians(90)
    angle = math.atan(abs( (m1 - m2) / (1 + m1*m2) ))
    return angle
    
def draw_line(screen, origin, start, end, spacing, color, width = 3):
    # Draw any line with converted coordinate system points
    start = convert(start, spacing, origin)
    end = convert(end, spacing, origin)
    pygame.draw.line(screen, color, start, end, width)

def parallel_line(p1, p2, start_point, screen, spacing, origin, color, width = 1, grid = False):
    # Draws parallel line to given line with color specified and start point specified of same magnitude and same direction

    # Calculate magnitude of line
    mag = math.sqrt( (p2[0] - p1[0])*(p2[0] - p1[0]) + (p2[1] - p1[1])*(p2[1] - p1[1]) ) 

    # If Slope is infinite then
    if p2[0] == p1[0]:       
        if p2[1] > p1[1]:
            end = (start_point[0], start_point[1] + mag)
        else:
            end = (start_point[0], start_point[1] - mag)
        draw_line(screen, origin, start_point, end, spacing, color, width)
        return
        
    # calculate slope
    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
     
    end = find(start_point[0], start_point[1], slope, mag)
    
    # Dealing with problem of slope
    if ((p2[0] - p1[0]) < 0 and (p2[1] - p1[1]) < 0): # Third quadrant
        end = (2*start_point[0] - end[0], 2*start_point[1] - end[1])
    if ((p2[0] - p1[0]) < 0 and (p2[1] - p1[1]) > 0): # Second quadrant
        end = (2*start_point[0] - end[0], 2*start_point[1] - end[1])

    draw_line(screen, origin, start_point, end, spacing, color, width)

    if grid: # Fixes The Problem with negative x axis grids || Temporarily, may commit changes in future if required
        endn = findn(start_point[0], start_point[1], slope, mag)
        draw_line(screen, origin, start_point, endn, spacing, color, width)
    
def vector_grids(screen, origin, convertx, convertxn, converty, convertyn, transformx, transformy, spacing, grid_color, width = 1):
   # Magnitude of basis vectors
   magx = math.sqrt(transformx[0]*transformx[0] + transformx[1]*transformx[1])
   magy = math.sqrt(transformy[0]*transformy[0] + transformy[1]*transformy[1])
   
   # grids future implemtation change range
   x = magy
   if converty[0] != 0:
       my = converty[1]/ converty[0]
       for i in range(100):
            startx = ( (x/math.sqrt(1 + my*my)), (my*x/math.sqrt(1 + my*my)) )
            parallel_line((0, 0), convertx, startx, screen, spacing, origin, grid_color, width, True)
            parallel_line((0, 0), convertxn, startx, screen, spacing, origin, grid_color, width, True)
            x += magy
       x = magy
       for i in range(100):
            startxn = ( ((-1)*x/math.sqrt(1 + my*my)), ((-1)*my*x/math.sqrt(1 + my*my)) )
            parallel_line((0, 0), convertx, startxn, screen, spacing, origin, grid_color, width, True)
            parallel_line((0, 0), convertxn, startxn, screen, spacing, origin, grid_color, width, True)
            x += magy
   else:
       x = magy 
       for i in range(100):
            startx = ( 0, x )
            parallel_line((0, 0), convertx, startx, screen, spacing, origin, grid_color, width, True)
            parallel_line((0, 0), convertxn, startx, screen, spacing, origin, grid_color, width, True)
            x += magy
       x = magy
       for i in range(100):
            startxn = ( 0, (-1)*x )
            parallel_line((0, 0), convertx, startxn, screen, spacing, origin, grid_color, width, True)
            parallel_line((0, 0), convertxn, startxn, screen, spacing, origin, grid_color, width, True)
            x += magy
       
        
   x = magx
   if convertx[0] != 0:
       mx = convertx[1] / convertx[0]
       for i in range(100):
           starty = ( (x/math.sqrt(1 + mx*mx)), (mx*x/math.sqrt(1 + mx*mx)) )
           parallel_line((0, 0), converty, starty, screen, spacing, origin, grid_color, width, True)
           parallel_line((0, 0), convertyn, starty, screen, spacing, origin, grid_color, width)
           x += magx
       x = magx
       for i in range(100):         
           startyn = ( ((-1)*x/math.sqrt(1 + mx*mx)), ((-1)*mx*x/math.sqrt(1 + mx*mx)) )
           parallel_line((0, 0), converty, startyn, screen, spacing, origin, grid_color, width, True)
           parallel_line((0, 0), convertyn, startyn, screen, spacing, origin, grid_color, width, True)
           x += magx
   else:
       x = magx
       for i in range(100):
           starty = ( 0, x )
           parallel_line((0, 0), converty, starty, screen, spacing, origin, grid_color, width, True)
           parallel_line((0, 0), convertyn, starty, screen, spacing, origin, grid_color, width, True)
           x += magx
       x = magx
       for i in range(100):         
           startyn = ( 0, (-1)*x )
           parallel_line((0, 0), converty, startyn, screen, spacing, origin, grid_color, width, True)
           parallel_line((0, 0), convertyn, startyn, screen, spacing, origin, grid_color, width, True)
           x += magx
       
def draw_bvector(screen, origin, vector, transformx, transformy, spacing, color, width = 3):
    # Convert vector to new coordinate system according to given vector by matrix transformation
    vector = ((vector[0]*transformx[0] + vector[1]*transformy[0]), (vector[0]*transformx[1] + vector[1]*transformy[1]))
    draw_line(screen, origin, (0,0), vector, spacing, color, width)
    # Draw arrowhead

def reference_grids(screen, origin_pos, semigrid_color, grid_color, spacing):
    # Y axis semi grids
    width_start = origin_pos[0]
    y = spacing / 2 # Used to show semi grid for better precision
    for i in range (int((screen.get_width() - width_start) / spacing)*2 ): # draw no. of grid lines
        pygame.draw.line(screen, semigrid_color, (width_start + y, 0), (width_start + y, screen.get_height()))
        y += spacing / 2
    y = spacing / 2
    for i in range (int(width_start / spacing)*2 ): # draw no. of grid lines
        pygame.draw.line(screen, semigrid_color, (width_start - y, 0), (width_start - y, screen.get_height()))
        y += spacing / 2
    
    # X axis semi grids       
    height_start = origin_pos[1]
    y = spacing / 2
    for i in range (int((screen.get_height() - height_start) / spacing)*2 ): # draw no. of grid lines
        pygame.draw.line(screen, semigrid_color, (0, height_start + y), (screen.get_width(), height_start + y))
        y += spacing / 2
    y = spacing / 2
    for i in range (int(height_start / spacing)*2 ): # draw no. of grid lines
        pygame.draw.line(screen, semigrid_color, (0, height_start - y), (screen.get_width(), height_start - y))
        y += spacing / 2

    # Y axis grids
    width_start = origin_pos[0]
    x = 0
    for i in range (int((screen.get_width() - width_start)*2 / spacing) ): # draw no. of grid lines
        pygame.draw.line(screen, grid_color, (width_start + x, 0), (width_start + x, screen.get_height()))
        x += spacing
    x = 0
    for i in range (int(width_start / spacing)*2 ): # draw no. of grid lines
        pygame.draw.line(screen, grid_color, (width_start - x, 0), (width_start - x, screen.get_height()))
        x += spacing
    # X axis grids
    height_start = origin_pos[1]
    x = 0
    for i in range (int((screen.get_height() - height_start)*2 / spacing) ): # draw no. of grid lines
        pygame.draw.line(screen, grid_color, (0, height_start + x), (screen.get_width(), height_start + x))
        x += spacing
    x = 0
    for i in range (int(height_start / spacing)*2 ): # draw no. of grid lines
        pygame.draw.line(screen, grid_color, (0, height_start - x), (screen.get_width(), height_start - x))
        x += spacing
    
    
   