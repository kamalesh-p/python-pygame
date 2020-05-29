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

# colors 
SHADOW  =  ( 192 ,  192 ,  192 )
WHITE  =  ( 255 ,  255 ,  255 )
GREY = ( 110 , 110 , 110 )
BLACK = ( 0 , 0 , 0 )
BROWN = ( 100 , 40 , 0 )
YELLOW = ( 255 , 255 , 0 )
CYAN = ( 5 , 250 , 250 )
BLUE = ( 0 , 0 , 190 )
BROWN = ( 100 , 40 , 0 ) 
GREEN = ( 0 , 220 , 0 ) 
ORANGE = ( 190 , 110 , 0 ) 
PINK = ( 250 , 40 , 80 ) 
RED = ( 220 , 0 , 0 ) 
SANDAL = ( 210 , 160 , 0 ) 
VIOLET = ( 190 , 30 , 220 )  
YELLOW = ( 180 , 240 , 0 )

# print text in pygame 
def printpg( writing , color , x , y , font_size ):
    font_style = pg.font.SysFont( None , int( font_size ) )
    text = font_style.render( str( writing ) , True , color )
    screen.blit( text , ( x , y ) )

def loop( ):
    done = True
    count = 0
    while done:
        # fill screen
        screen.fill( BLACK )
        for event in pg.event.get(  ):
            mousepos = pg.mouse.get_pos(  )
        if event.type == pg.QUIT:
            done = False
            break
        #printpg( writing , color , x , y , font_size )
        printpg( "Hello World" , RED , 0 , 0 , 25 )
        printpg( str( count ) , BLUE , 100 , 100 , 30 )
        string = "Screen \n Height = " + str( height ) + " \n Width = "+ str( width )
        printpg( string , GREEN , 0 , 150 , 35 )
        count += 1
        # screen update
        pg.display.flip(  )
    
loop( )

