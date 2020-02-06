from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #pass
    if x0 > x1:
        draw_line(x1,y1,x0,y0,screen,color) #takes care of octants 3,4,5,6
    else:
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = 2*A+B
        while x <= x1: #octant 1
            plot(screen, color, x,y)
            if d > 0:
                y += 1
                d += 2*B
            x += 1
            d += 2*A
