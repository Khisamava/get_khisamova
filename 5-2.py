import RPi.GPIO as gpio
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
        i = ads()
        print(i, '{:.2f}v'.format(3.3*i/255))


finally:
    gpio.output(dac, 0)
    gpio.cleanup()
