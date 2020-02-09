from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #pass
    if x0 == x1 and y1 > y0: #vertical lines
        y = y0
        while y <= y1:
            plot(screen,color,x0,y)
            y += 1
    elif x0 == x1 and y1 < y0:
        draw_line(x1,y1,x0,y0,screen,color)

    elif x0 > x1:
        draw_line(x1,y1,x0,y0,screen,color) #takes care of octants 3,4,5,6
    else:
        if y1 - y0 >=0 and y1 - y0 <= x1 - x0: #octant 1
            x = x0
            y = y0
            A = y1 - y0
            B = x0 - x1
            d = 2*A+B
            while x <= x1:
                plot(screen, color, x,y)
                if d > 0:
                    y += 1
                    d += 2*B
                x += 1
                d += 2*A

        elif y1 - y0 > x1 - x0: #octant 2
            x = y0
            y = x0
            A = x1 - x0
            B = y0 - y1
            d = 2*A+B
            while x <= y1:
                plot(screen, color, y,x)
                if d > 0:
                    y += 1
                    d += 2*B
                x += 1
                d += 2*A

        elif y1 - y0 < 0 and y0 - y1 <= x1 - x0:  #octant 8
            x = x0
            y = y1
            A = y0 - y1
            B = x0 - x1
            d = 2*A+B
            while x <= x1:
                plot(screen, color, x, y0 + y1 - y)
                if d > 0:
                    y += 1
                    d += 2*B
                x += 1
                d += 2*A

        else:
            x = y1
            y = x0
            A = x1 - x0
            B = y1 - y0
            d = 2*A+B
            while x <= y0: #octant 1
                plot(screen, color, y, y0 + y1 - x)
                if d > 0:
                    y += 1
                    d += 2*B
                x += 1
                d += 2*A
