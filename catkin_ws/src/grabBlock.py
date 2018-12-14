from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

def grab():

    #making sure the arm is reset
    pwm.set_pwm(4, 0, 350)
    pwm.set_pwm(3, 0, 0)
    pwm.set_pwm(2, 0, 150)
    pwm.set_pwm(1, 0, 650)
    pwm.set_pwm(0, 0, 500)
    time.sleep(1)

    #wake up
    for x in range(200):
        pwm.set_pwm(1, 0, (650-x))
        time.sleep(.001)
    time.sleep(1)
    for x in range (200):
        pwm.set_pwm(2, 0, 200+x)
        time.sleep(.001)
    time.sleep(1)

    # rotate arm
    pwm.set_pwm(3, 0, 350)
    time.sleep(1)

    #move a little lower
    for x  in range(100):
        pwm.set_pwm(1, 0, 450-x)
        time.sleep(.001)
    time.sleep(1)

    #open arm
    for x in range(200):
        pwm.set_pwm(4, 0, 350-x)
        time.sleep(.0001)
    time.sleep(1)

    #down to grab
    for x in range(180):
        pwm.set_pwm(1, 0, 350-x)
        time.sleep(.001)
    time.sleep(1)

    #close arm
    for x in range(200):
        pwm.set_pwm(4, 0, 150+x)
        time.sleep(.0001)
    time.sleep(1)

    #lift up
    for x in range(230):
        pwm.set_pwm(1,0,170+x)
        time.sleep(.001)
    for x in  range(250):
        pwm.set_pwm(2, 0, 400-x)
        time.sleep(.001)
    for x in  range(250):
        pwm.set_pwm(1, 0, 450+x)
        time.sleep(.001)
