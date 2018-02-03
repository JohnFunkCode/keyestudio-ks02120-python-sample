from gpiozero import LED
from time import sleep

def blink_led_once( blink_frequency ):
    """turns the led on for 1/2 the time specified in blink_frequency, then it off for the same amount of time."""
    myLED=LED(17)

    myLED.on()
    sleep(blink_frequency /2)
    myLED.off()
    sleep(blink_frequency /2 )

def blink_led_forever():
    """blink the led once per second in a never ending loop"""
    while True:
        blink_led_once(1)

if __name__ == "__main__":
    print("This will make the LED blink forever")
    blink_led_forever()
