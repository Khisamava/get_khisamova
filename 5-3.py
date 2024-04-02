import RPi.GPIO as gpio
from time import sleep
gpio.setmode(gpio.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def desimal2binary(value):
    return[int(elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    value = 0
    for i in range(7, -1, -1):
        value += 2**i
        dacc = []
        dacc = desimal2binary(value)
        gpio.output(dac, dacc)
        sleep(0.001)
        compvalue = gpio.input(comp)
        if compvalue == gpio.HIGH:
            value -= 2**i
    return value

try:
    while True:
        a = int(adc()/256*8)
        b = [0]*(8-a)+[1]*a
        print(a, b)
        gpio.output(leds, b)

finally:
    gpio.cleanup()
