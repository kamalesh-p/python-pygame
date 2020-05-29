''' DON'T CHANGE ANYTHING '''
''' [ '''

try:
    # used in mobile phone in pydroid3 application
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
    import pygame as pg
except:
    # used in system applications
    import pygame as pg

""" SCREEN DETAILS """

# initialise  
pg.init(  )
scrx = int( 640 )
scry = scrx
screen = pg.display.set_mode( ( scrx , scry ) )

# Get screen width and height
width = screen.get_width(  )
height = screen.get_height(  )

# number of frames per second
clock = pg.time.Clock(  )

# find computer or phone
computer = False
if ( scrx == width and scry == height ) or ( scry == width and scrx == height ):
    computer = True

""" LOCATION """

image_location = "image/"
audio_location = "audio/"
file_location = "file/"

""" COLORS """

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

class colour:
    def __init__( self , BRIGHT , DARK , DIRTY , LIGHT , PURE ):
        self.BRIGHT = BRIGHT
        self.DARK = DARK
        self.DIRTY = DIRTY
        self.LIGHT = LIGHT
        self.PURE = PURE

BLUEc = colour( ( 0 , 5 , 90 ) , ( 0 , 10 , 130 ) , ( 0 , 30 , 50 ) , ( 0 , 70 , 230 ) , ( 10 , 10 , 250 ) )
BROWNc = colour( ( 200 , 30 , 0 ) , ( 160 , 20 , 0 ) , ( 180 , 40 , 0 ) , ( 160 , 60 , 0 ) , ( 170 , 80 , 0 ) )
GREENc = colour( ( 10 , 230 , 0 ) , ( 10 , 90 , 10 ) , ( 10 , 50 , 0 ) , ( 0 , 180 , 0 ) , ( 0 , 250 , 100 ) )
ORANGEc = colour( ( 250 , 160 , 0 ) , ( 180 , 70 , 0 ) , ( 180 , 110 , 0 ) , ( 180 , 100 , 0 ) , ( 190 , 70 , 0 ) )
PINKc = colour( ( 250 , 30 , 100 ) , ( 250 , 120 , 130 ) , ( 250 , 160 , 170 ) , ( 250 , 100 , 160 ) , ( 250 , 10 , 100 ) )
REDc = colour( ( 210 , 20 , 0 ) , ( 160 , 30 , 0 ) , ( 180 , 10 , 0 ) , ( 200 , 40 , 0 ) , ( 210 , 10 , 0 ) )
SANDALc = colour( ( 250 , 190 , 120 ) , ( 180 , 140 , 0 ) , ( 180 , 150 , 0 ) , ( 200 , 160 , 50 ) , ( 190 , 190 , 0 ) )
VIOLETc = colour( ( 180 , 20 , 190 ) , ( 180 , 0 , 110 ) , ( 190 , 40 , 140 ) , ( 180 , 20 , 250 ) , ( 190 , 0 , 140 ) )
YELLOWc = colour( ( 200 , 250 , 20 ) , ( 180 , 180 , 0 ) , ( 180 , 210 , 0 ) , ( 180 , 250 , 60 ) , ( 250 , 210 , 0 ) )

""" DRAW SHAPES """

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

""" PRINT TEXT """

# print text in pygame 
def printpg( writing , color , x , y , font_size ):
    font_style = pg.font.SysFont( None , int( font_size ) )
    text = font_style.render( str( writing ) , True , color )
    screen.blit( text , ( x , y ) )

""" AUDIO """

# audio function
def song( audioname ):
    try:
        pg.mixer.Sound( audio_location + audioname ).play
    except:
        print( "ERROR : " + audioname + " is not avaiabe. Audio can't be played ")

# audio class
class audios:
    def __init__( self , audio , soundExt ):
        self.SOUNDS = {  }
        self.soundExt = soundExt
        for i in range( 0 , len( audio ) ):
            try:
                self.SOUNDS[ audio_location + audio[ i ] ] = pg.mixer.Sound( audio[ i ] + soundExt )
            except:
                self.SOUNDS[ audio[ i ] ] = audio[ i ] + soundExt
                print( "ERROR : " + self.SOUNDS[ audio[ i ] ] + "number = " + str( i ) + " audio is not available in class audios initialise " )
    def song( self , audio ):
        if self.SOUNDS[ audio ] != audio + self.soundExt:
            self.SOUNDS[ audio ].play(  )
        else:
            print( "ERROR : " + self.SOUNDS[ audio ] + " unable to play audio " )

"""IMAGE"""

# image display in function
def picture( img , x , y , widt , heig , angle , flip ):
        try:
            img1 = pg.image.load( image_location + img )
            img2 = pg.transform.scale( img1 , ( widt , heig ) )
            img3 = pg.transform.rotate( img2 , angle )
            if flip == 1:
                horizontal_flip = True
                vertical_flip = False
            elif flip == 2:
                horizontal_flip = False
                vertical_flip = True
            elif flip == 3:
                horizontal_flip = True
                vertical_flip = True
            else:
                horizontal_flip = False
                vertical_flip = False
            img4 = pg.transform.flip( img3 , horizontal_flip , vertical_flip )
            img4rect = img4.get_rect(  )
            img4rect.x = x
            img4rect.y = y
            screen.blit( img4 , img4rect )
        except:
            print( "ERROR : " + str( img ) + " is not available ")

# image class 
class image:
    def __init__( self , img ):
        try:
            self.img1 = pg.image.load( image_location + img )
        except:
            self.img1 = img
            print( "ERROR : " + str( img ) + " is not available while initialising class image " )
    def picture( self , x , y , widt , heig , angle , flip ):
        try:
            img2 = pg.transform.scale( self.img1 , ( widt , heig ) )
            img3 = pg.transform.rotate( img2 , angle )
            if flip == 1:
                horizontal_flip = True
                vertical_flip = False
            elif flip == 2:
                horizontal_flip = False
                vertical_flip = True
            elif flip == 3:
                horizontal_flip = True
                vertical_flip = True
            else:
                horizontal_flip = False
                vertical_flip = False
            img4 = pg.transform.flip( img3 , horizontal_flip , vertical_flip )
            img4rect = img4.get_rect(  )
            img4rect.x = x
            img4rect.y = y
            screen.blit( img4 , img4rect )
        except:
            print( "ERROR : " + str( self.img1 ) + " is not available while loading class image " )

# class for array of images
class images:
    def __init__( self , img , imageExt ):
        self.IMAGES = {  }
        for i in range( 0 , len( img ) ):
            try:
                self.IMAGES[ img[ i ] ] = pg.image.load( image_location + img[ i ] + imageExt )
            except:
                self.IMAGES[ img[ i ] ] = img[ i ] + imageExt
                print( "ERROR : " + str( img[ i ] ) + "image array number = " + str( i ) + " is not available while initialising class images " )
    def picture( self , image_name , x , y , widt , heig , angle , flip ):
        try:
            img2 = pg.transform.scale( self.IMAGES[ image_name ] , ( widt , heig ) )
            img3 = pg.transform.rotate( img2 , angle )
            if flip == 1:
                horizontal_flip = True
                vertical_flip = False
            elif flip == 2:
                horizontal_flip = False
                vertical_flip = True
            elif flip == 3:
                horizontal_flip = True
                vertical_flip = True
            else:
                horizontal_flip = False
                vertical_flip = False
            img4 = pg.transform.flip( img3 , horizontal_flip , vertical_flip )
            img4rect = img4.get_rect(  )
            img4rect.x = x
            img4rect.y = y
            screen.blit( img4 , img4rect )
        except:
            print( "ERROR : " + str( self.IMAGES[ image_name ] ) + " is not available while loading class images " )

""" CONTROLS """

# mouse and keyboard control
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

""" START """

def start( speed ):
    clock.tick( speed ) # number of frames per second
    pg.display.flip( ) # update screen 
    screen.fill( BLACK ) # fill screen black

''' ] '''

# global variables
''' 

TYPE YOUR CLASSES , VARIABLES AND FUNCTIONS HERE

TYPE YOUR CLASSES , VARIABLES AND FUNCTIONS HERE

TYPE YOUR CLASSES , VARIABLES AND FUNCTIONS HERE 

TYPE YOUR CLASSES , VARIABLES AND FUNCTIONS HERE

TYPE YOUR CLASSES , VARIABLES AND FUNCTIONS HERE

'''
speed = 5 # speed = 0 is faster 

def loop(  ):
    done = True
    mousex = 0 ; mousey = 0 ; keys = 0
    while done:
        start( speed )
        mousedetail = mousecontrol( False ) 
        if mousedetail[ 0 ] and mousedetail[ 1 ]:
            mousex = mousedetail[ 0 ]
            mousey = mousedetail[ 1 ]
        keys = mousedetail[ 2 ]
        if keys == "quit":
            done = False
            break
        """
        WRITE YOUR PROGRAMMING HERE
        
        WRITE YOUR PROGRAMMING HERE
        
        WRITE YOUR PROGRAMMING HERE
        
        WRITE YOUR PROGRAMMING HERE
        
        WRITE YOUR PROGRAMMING HERE
        
        """
    # don't forget to delete the class variables after usage because it catches storage
    # use del variable_name

loop(  )








