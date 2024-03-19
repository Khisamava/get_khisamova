import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setwarnings(False)

pwm = GPIO.PWM(21, 100)
pwm.start(0)

try:
    while True:
        rate = input()
        if rate == 'q':
            break
        try:
            duty_cycle = float(rate)
            if duty_cycle < 0 or duty_cycle > 100:
                print('Please enter number between 0 and 100')
                continue 
        except ValueError:
            print('Please enter number between 0 and 100')
            continue 
        dc = int(rate)
        pwm.start(dc)
        volt = 3.3*dc/100
        print(volt)
except KeyboardInterrupt:
    pass
finally:
    GPIO.output(21, 0)
    GPIO.cleanup()

