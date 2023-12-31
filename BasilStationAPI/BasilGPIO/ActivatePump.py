import RPi.GPIO as GPIO
from time import sleep


def __setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT,initial=GPIO.LOW)

def pump(duration):
    __setup()
    GPIO.output(17, GPIO.HIGH)
    sleep(duration)
    GPIO.output(17, GPIO.LOW)
    __cleanup()

def __cleanup():
    GPIO.cleanup()