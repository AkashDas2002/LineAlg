from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, YRES / 2, s, c)
#
# # draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)
# draw_line(XRES-1, YRES-1, 0, 250, s, c)
#
# #octants 8 and 4
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES-1, 0, s, c);
#
# # draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
# draw_line(0, YRES-1, XRES-1, 250, s, c);
#
# # draw_line(XRES-1, 0, 0, YRES/2, s, c);
# draw_line(XRES-1, 0, 0, 250, s, c);
#
# #octants 2 and 6
# c[RED] = 255;
# c[GREEN] = 0;
# c[BLUE] = 0;
# draw_line(0, 0, XRES/2, YRES-1, s, c);
#
# # draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);
# draw_line(XRES-1, YRES-1, 250, 0, s, c);
#
# #octants 7 and 3
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES/2, 0, s, c);
#
# # draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);
# draw_line(XRES-1, 0, 250, YRES-1, s, c);
#
# # #horizontal and vertical
# c[BLUE] = 0;
# c[GREEN] = 255;
# # draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
# draw_line(0, 250, XRES-1, 250, s, c);
# # draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);
# draw_line(250, 0, 250, YRES-1, s, c);

draw_line(25,25,475,25,s,c) #horizontal line
draw_line(475,25,200,480,s,c) #octant 3
draw_line(200,480,25,25,s,c) #octant 6

c[RED]=255
draw_line(25,25,230,112,s,c) #octant 1
draw_line(25,25,305,305,s,c) # slope 1
draw_line(230,112,475,25,s,c) #octant 8
draw_line(475,25,289,177,s,c) #octant 4
draw_line(200,480,200,200,s,c) #vertical line
draw_line(200,480,289,177,s,c) #octant 7

c[BLUE]=255
c[RED]=0
draw_line(200,200,289,177,s,c)
draw_line(200,200,230,112,s,c)
draw_line(289,177,230,112,s,c) #octant 5

c[BLUE] = 0
c[GREEN] = 0
draw_line(305,305,200,200,s,c) # slope -1

c[RED]=255
draw_line(300,400,320,480,s,c) #octant 2
draw_line(340,400,320,480,s,c) #octant  7
draw_line(310,440,330,440,s,c) #horizontal
draw_line(370,424,370,460,s,c) #vertical
draw_line(352,442,388,442,s,c) #horizontal

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
