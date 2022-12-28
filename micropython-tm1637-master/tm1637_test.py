# MicroPython TM1637 quad 7-segment LED display driver examples

# WeMos D1 Mini -- 4 Digit Display
# D1 (GPIO5) ----- CLK
# D2 (GPIO4) ----- DIO
# 3V3 ------------ VCC
# G -------------- GND

import tm1637
import time
from machine import Pin
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))

while True:
    # show "12:59"
    for i in range (99):
        tm.numbers(i, i)
        
        time.sleep(.1)
        #tm.number((i + i))
        time.sleep(.1)
       
        

