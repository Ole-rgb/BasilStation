import RPi.GPIO as GPIO
from time import sleep


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16,GPIO.OUT)

def pump(duration):
    setup()
    GPIO.output(17, True)
    sleep(3)
    GPIO.output(17, False)
    cleanup()

def cleanup():
    GPIO.cleanup()