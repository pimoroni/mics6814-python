#!/usr/bin/env python3
import sys
from mics6814 import MICS6814

print("""led.py - Set the RGB LED

Basic example of setting the RGB status LED on the MICS6814 breakout.

""")

if len(sys.argv) < 4:
    print("Usage: {} <r> <g> <b>".format(sys.argv[0]))
    sys.exit(1)

mics = MICS6814()
mics.set_pwm_period(4096)
mics.set_brightness(0.1)

r, g, b = [int(c) for c in sys.argv[1:]]

mics.set_led(r, g, b)
