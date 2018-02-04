"""KS0212 keyestudio RPI 4-channel Relay Shield Python Sample

This code is a very simple Python example demonstrating how to use
the keyestudio KS0212 with a Raspberry Pi 3
"""

from gpiozero import LED
from time import sleep

#define the 4 GPIO lines we want to use
four=LED(4)
twentytwo=LED(22)
six=LED(6)
twentysix=LED(26)

while True:
    #turn relay J2 on then off
    four.on()
    sleep(.5)
    four.off()
    sleep(.5)
    
    #turn relay J3 on then off
    twentytwo.on()
    sleep(.5)
    twentytwo.off()
    sleep(.5)
    
    #turn relay J3 on then off
    six.on()
    sleep(.5)
    six.off()
    sleep(.5)

    #turn relay J4 on then off
    twentysix.on()
    sleep(.5)
    twentysix.off()
    sleep(.5)

