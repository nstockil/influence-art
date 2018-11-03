from picamera import PiCamera
from datetime import datetime

def takePhoto():
    filename = "sketch_{0:%Y}-{0:%m}-{0:%d}-{0:%H}-{0:%M}.png".format(datetime.now())
    camera = PiCamera()
    camera.capture("home/influence/sketchbook/{0}.png".format(filename))
    camera.close()