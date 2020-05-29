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

# location
image_location = "image/"

# number of frames per second
clock = pg.time.Clock(  )

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

# loop
def loop( ):
    # class image initialise
    # image( image name with image type ) 
    # name = "img" , type = ".png" 
    img = image( "img.png" )
    # images name array
    imgsary = [ "img1" , "img2" , "img3" ]
    # images( image name array , image type )
    # image name array = [ "img1" , "img2" , "img3" , "img4" , "img5" ] , image type = ".png"
    imgs = images( imgsary , ".png" )
    done = True
    count = 0
    while done:
        # fill screen
        screen.fill( ( 0 , 0 , 0 ) )
        x = 100
        y = 100
        for event in pg.event.get(  ):
            mousepos = pg.mouse.get_pos(  )
        if event.type == pg.QUIT:
            done = False
            break
        '''
        flip = 1 ( horizontal flip ) ,
        flip = 2 ( vertical flip ) , 
        flip = 3 ( horizontal and vertical flip ) , 
        flip = 0 ( none )
        angle = 0 to 360
        '''
        # picture( image name and image type , x , y , widt , heig , angle , flip )
        picture( "img.png" , x , y , 100 , 100 , 0 , 0 )
        # img.picture( x , y , widt , heig , angle , flip )
        img.picture( x*2 , y , 100 , 100 , 0 , 0 )
        # img.picture( imgsary[ count ] , x , y , widt , heig , angle , flip )
        imgs.picture( imgsary[ count ] , x , y*3 , 300 , 100 , 0 , 0 )
        # update count
        count += 1
        if count >= len( imgsary ):
            count = 0
        # screen update
        pg.display.flip(  )
        clock.tick( 5 )
    # don't forget to delete the classes after usage because it catches storage
    del img
    del imgs

loop(  )


# function image
'''
1 . can be used when the image is needed only once
2 . it take time for the image to be loaded
3 . so when used again and again it stops the program from execution 
'''

# class image
'''
1 . can be used when the image is needed often but a single image
2 . image is already loaded and only sets the x , y position , angle and flip 
3 . so it consumes time and memory
4 . delete the class image after its use to free up space for other variables
'''

# class images
'''
1 . can be used when the image is needed often but a multiple image
2 . same advantage as in class image
3 . used for changing image motion in game with time by using count
'''




