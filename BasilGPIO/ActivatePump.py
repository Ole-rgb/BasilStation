import RPi.GPIO as GPIO
from time import sleep


def __setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16,GPIO.OUT)

def pump(duration):
    __setup()
    GPIO.output(17, True)
    sleep(3)
    GPIO.output(17, False)
    __cleanup()

def __cleanup():
    GPIO.cleanup()