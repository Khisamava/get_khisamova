import RPi.GPIO as gpio
import sys
from time import sleep
gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def desimal2binary(value):
    return[int(elem) for elem in bin(value)[2:].zfill(8)]

def ads():


   for i in range(256):
        dacc = desimal2binary(i)
        gpio.output(dac, dacc)
        sleep(0.001)
        compvalue = gpio.input(comp)
        if compvalue == 1:
            return i
   return 256

try:
    while True:
        i = ads()
        print(i, '{:.2f}v'.format(3.3*i/256))


finally:
    gpio.output(dac, 0)
    gpio.cleanup()
