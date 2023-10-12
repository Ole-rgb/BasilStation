import RPi.GPIO as GPIO
from time import sleep


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16,GPIO.OUT)

def pump(duration):
    GPIO.output(17, True)
    sleep(3)
    GPIO.output(17, False)

def cleanup():
    GPIO.cleanup()