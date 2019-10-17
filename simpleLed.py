import RPi.GPIO as gpio
import time

green = 23
yellow = 24
red = 25

gpio.setmode(gpio.BCM)
gpio.setup(green, gpio.OUT)
gpio.setup(yellow, gpio.OUT)
gpio.setup(red, gpio.OUT)

gpio.output(green, 1)
gpio.output(yellow, 0)
gpio.output(red, 0)
time.sleep(0.5)

gpio.output(green, 0)
gpio.output(yellow, 1)
time.sleep(0.5)

gpio.output(yellow, 0)
gpio.output(red, 1)
time.sleep(0.5)

print("Blink Finished")
gpio.cleanup()
