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

# polygon
def polygon( array , color ):
    pg .draw.polygon( screen , color , array )

# line
def line( startpoint , endpoint , color , thickness ):
    pg .draw.line( screen , color , startpoint , endpoint , thickness )

# rect
def rect( x , y , color , widt , heig , thickness ):
    pg.draw.rect( screen , color , pg.Rect( x , y , widt , heig ) , thickness )

# circle   
def circle( x , y , color , radius , thickness ):
    pg.draw.circle( screen , color , ( int( x ) , int( y ) ) , int( radius ) , thickness )
   
# ellipse
def ellipse( x , y , color , widt , heig , thickness ):
    try:
        pg.draw.ellipse( screen , color , ( x , y , widt , heig ) , thickness )    
    except:
        print( " ellipse can't be draw in your mobile because the size is very small ")

def loop(  ):
    while True:
        screen.fill( BLACK )
        for event in pg.event.get(  ):
            mousepos = pg.mouse.get_pos(  )
        if event.type == pg.QUIT:
            done = False
            break
        polygon( ( ( 0 , 0 ) , ( 10 , 20 ) , ( 20 , 30 ) , ( 40 , 20 ) , ( 0 , 20 ) ) , GREEN )
        line( ( 0 , 50 ) , ( 100 , 50 ) , RED , 3 )
        thickness = 0 # display a whole diagram
        rect( 100 , 100 , BLUE , 100 , 25 , thickness )
        circle( 50 , 250 , YELLOW , 50 , thickness )
        ellipse( 50 , 350 , VIOLET , 500 , 100 , thickness )
        thickness = 5 # display a outline of diagram
        rect( 100 , 100 , WHITE , 100 , 25 , thickness )
        circle( 50 , 250 , WHITE , 50 , thickness )
        ellipse( 50 , 350 , WHITE , 500 , 100 , thickness )
        pg.display.flip(  )

loop(  )

# these functions are used because we need not type " pg.draw.line( screen , " everytime










