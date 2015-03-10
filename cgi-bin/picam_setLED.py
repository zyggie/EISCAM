import picamera

with picamera.PiCamera() as camera:
    # Turn the camera's LED off
    camera.led = True
