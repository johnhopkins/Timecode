class Timecode(object):

    def __init__ (self, frames):
        '''
        Init timecode object with a number of frames
        '''
        try:
            assert isinstance(frames, int)
        except AssertionError:
            frames = 0
        self.frames = frames

    def getFrames(self):
        '''
        Return frames
        '''
        return self.frames

    def setFrames(self, frames):
        '''
        Alter number of frames within a Timecode object
        '''
        try:
            assert isinstance(frames, int)
            self.frames = frames
        except AssertionError:
            self.frames = self.frames

    def getTimecode(self, framerate):
        '''
        Converts frames into Hours, Minutes and Seconds
        and returns a human readable timecode string
        '''
        hrs = self.frames / (3600*framerate)
        mins = self.frames / (60*framerate) % 60
        secs = self.frames / framerate % 60
        frms = self.frames % framerate
        
        return '{0:02d}:{1:02d}:{2:02d}:{3:02d}'.format(hrs,mins,secs,frms)

    def setTimecode(self, timecode, framerate):
        '''
        Takes a timecode formatted string and converts
        it into a number of frames and stores it within the object
        '''
        #this setter method needs work to ensure string passed
        #in is in the particular format '00:00:00:00'
        
        try:
            assert isinstance(timecode, str)
            self.frames = sum(f * int(t) for f,t in zip((3600*framerate, 60*framerate, framerate, 1), timecode.split(':')))
        except AssertionError:
            self.frames = self.frames
