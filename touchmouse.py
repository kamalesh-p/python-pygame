'''
 In Mobile( touch phone ) FINGER TOUCH is considered as mouse position
'''

try:
    # used in mobile phone in pydroid3 application
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
    import pygame as pg
except:
    # used in system applications
    import pygame as pg

# initialise  
pg.init(  )
scrx = int( 640 )
scry = scrx
screen = pg.display.set_mode( ( scrx , scry ) )

# Get screen width and height
width = screen.get_width(  )
height = screen.get_height(  )

computer = False
if ( scrx == width and scry == height ) or ( scry == width and scrx == height ):
    computer = True

image_location = "image/"

def mousecontrol( keyboard ):
    # keyboard is True displays all the keys 
    # False displays only useful keys
    keys = 0
    mousepos = [ 0 , 0 ]
    # get mouse position 
    for event in pg.event.get(  ):
        mousepos = pg.mouse.get_pos(  )
        if event.type == pg.QUIT:
            return [ mousepos[ 0 ] , mousepos[ 1 ] , "quit" ]
        # if computer these keys will work
        if event.type == pg.KEYDOWN and computer:    
            if event.key == pg.K_UP:
                keys = "up"
            elif event.key == pg.K_RIGHT:
                keys = "right"
            elif event.key == pg.K_DOWN:
                keys = "down" 
            elif event.key == pg.K_LEFT:
                keys = "left"
            elif event.key == pg.K_SPACE:
                keys = "space"
            elif event.key == pg.K_a:
                keys = 'a'
            elif event.key == pg.K_w:
                keys = 'w'
            elif event.key == pg.K_d:
                keys = 'd'
            elif event.key == pg.K_x:
                keys = 'x'
            elif event.key == pg.K_j:
                keys = 'j'
            elif event.key == pg.K_f:
                keys = 'f'
            elif event.key == pg.K_END:
                keys = 'end'
            elif event.key == pg.K_HOME:
                keys = 'home'
            elif event.key == pg.K_BACKSPACE:
                keys = 'backspace'
            elif event.key == pg.K_DELETE:
                keys = 'delete'
            elif event.key == pg.K_RETURN:
                keys = 'return'
            elif event.key == pg.K_ESCAPE:
                keys = 'esc'
            if not keyboard:
                break
            elif event.key == pg.K_b:
                keys = 'b'
            elif event.key == pg.K_c:
                keys = 'c'
            elif event.key == pg.K_e:
                keys = 'e'
            elif event.key == pg.K_g:
                keys = 'g'
            elif event.key == pg.K_h:
                keys = 'h'
            elif event.key == pg.K_i:
                keys = 'i'
            elif event.key == pg.K_k:
                keys = 'k'
            elif event.key == pg.K_l:
                keys = 'l'
            elif event.key == pg.K_m:
                keys = 'm'
            elif event.key == pg.K_n:
                keys = 'n'
            elif event.key == pg.K_o:
                keys = 'o'
            elif event.key == pg.K_p:
                keys = 'p'
            elif event.key == pg.K_q:
                keys = 'q'
            elif event.key == pg.K_r:
                keys = 'r'
            elif event.key == pg.K_s:
                keys = 's'
            elif event.key == pg.K_t:
                keys = 't'
            elif event.key == pg.K_u:
                keys = 'u'
            elif event.key == pg.K_v:
                keys = 'v'
            elif event.key == pg.K_y:
                keys = 'y'
            elif event.key == pg.K_z:
                keys = 'z'
    return [ mousepos[ 0 ] , mousepos[ 1 ] , keys ]

def loop( ):
    done = True
    mousex = 0 ; mousey = 0 ; keys = 0 
    x = 0 ; y = 0
    while done:
        # fill screen
        screen.fill( ( 0 , 0 , 0 ) )
        # mousecontrol( keyboard )
        mousedetail = mousecontrol( False )
        # if the mouse is inactive it returns mousex = 0 and mousey = 0 
        if mousedetail[ 0 ] and mousedetail[ 1 ]:
            mousex = mousedetail[ 0 ]
            mousey = mousedetail[ 1 ]
        keys = mousedetail[ 2 ]
        if keys == "quit":
            done = False
            break
        # rectangle tracing mouse path
        pg.draw.rect( screen , ( 255 , 255 , 255 ) , pg.Rect( mousex , mousey , 100 , 100 ) , 0 )
        if computer:
            if keys == "up":
                y -= 10
            elif keys == "left":
                x -= 10
            elif keys == "right":
                x += 10
            elif keys == "down":
                y += 10
            pg.draw.rect( screen , ( 115 , 115 , 115 ) , pg.Rect( x , y , 100 , 100 ) , 0 )
        # screen update
        pg.display.flip(  )

loop(  )
