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
audio_location = "audio/"

# number of frames per second
clock = pg.time.Clock(  )

# audio function
def song( audioname ):
    try:
        a = pg.mixer.Sound( audio_location + audioname )
        a.play()
    except:
        print( "ERROR : " + audioname + " is not avaiabe. Audio can't be played ")

# audio class
class audios:
    def __init__( self , audio , soundExt ):
        self.SOUNDS = {  }
        self.soundExt = soundExt
        for i in range( 0 , len( audio ) ):
            try:
                self.SOUNDS[ audio[ i ] ] = pg.mixer.Sound( audio_location + audio[ i ] + soundExt )
            except:
                self.SOUNDS[ audio[ i ] ] = audio[ i ] + soundExt
                print( "ERROR : " + self.SOUNDS[ audio[ i ] ] + "number = " + str( i ) + " audio is not available in class audios initialise " )
    def song( self , audio ):
        if self.SOUNDS[ audio ] != audio + self.soundExt:
            self.SOUNDS[ audio ].play(  )
        else:
            print( "ERROR : " + self.SOUNDS[ audio ] + " unable to play audio " )


def loop( ):
    # class audios initialise
    # audios name array
    aud_array = [ "sound1" , "sound2", "sound3" ]
    # audios( audio name array , sound type )
    # audio name array = [ "sound1" , "sound2" , "sound3" , "sound4" , "sound5" ] , soundtype = ".ogg"
    aud = audios( aud_array , ".ogg" )
    done = True
    i = 0
    while done:
        # fill screen
        screen.fill( ( 0 , 0 , 0 ) )
        for event in pg.event.get(  ):
            mousepos = pg.mouse.get_pos(  )
        if event.type == pg.QUIT:
            done = False
            break
        song( "sound.ogg" )
        # class audios function
        aud.song( aud_array[ i ] ) 
        i += 1
        if i >= len( aud_array ):
            i = 0
        # screen update
        pg.display.flip(  )
        clock.tick( 5 )
    # don't forget to delete the classes after usage because it catches storage
    del aud

loop( )

# audio function
""" Loading audio """
# audios class
""" Loading audio in array but one at a time """


