import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)


def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    while True:
        a = input()
        if a == 'q':
            exit()
        elif a.isdigit() and int(a) %1 == 0 and 0 <= int(a) <= 255:
            GPIO.output(dac, decimal2binary(int(a)))
            print(int(a)/256*3.3)
        else:
            print('Please enter positive integer number less then 255')

except ValueError:
    print('Please enter positive integer number less then 255')
except KeyboardInterrupt:
    print('finish')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
