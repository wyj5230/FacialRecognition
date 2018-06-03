import sys, os
import RPi.GPIO as GPIO
import picamera
import time
from upload_image import Upload

class Switch:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN)

    def getState(self):
        return GPIO.input(self.pin)

def main():
    sw = Switch(17)
    state = sw.getState()
    while True:
        #time.sleep(1)
        r = sw.getState()
        if (r != state):
            #camera.vflip = True
            camera = picamera.PiCamera()
            if (r == 1):
                try:
                    # do something with the camera
                    camera.vflip = True
                    camera.start_preview()
                    time.sleep(5)
                    camera.capture(time.asctime() + '_student.jpg')
                    camera.stop_preview()
                finally:
                    camera.close()
                img_path = '/'.join(os.path.realpath(__file__).replace('\\', '/').split('/')[:-1]) + '/2018_student.jpg'
                img_name = '2018_student'
                Upload(img_path, img_name)
                state = r
                print("%s: status is %d", time.asctime(), state)
            else:
                state = r
                print("%s: status is %d", time.asctime(), state)
            
if __name__ == "__main__":
    main()