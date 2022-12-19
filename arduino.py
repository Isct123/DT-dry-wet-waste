import pyfirmata
import time

board = pyfirmata.Arduino('COM4')

led = board.get_pin('d:13:o')

def on():
    led.write(1)

def off():
    led.write(0)