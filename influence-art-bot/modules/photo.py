from picamera import PiCamera
from datetime import datetime

class sketchbook:
    """
    The sketchbook class is responsible for File I/O and maintaining the sketch book
    """
    
    def __init__ (self):
        self._sketchbookLocation = "home/influence/sketchbook"
        self._sketchformat = "png"

    def takephoto(self):
        """
        Takes a photo and stores it in the sketchbook folder
        """
        filename = "sketch_{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}.png".format(datetime.now())
        camera = PiCamera()
        camera.capture("{0}/{1}.{2}".format(self._sketchbookLocation, filename, self._sketchformat))
        camera.close()