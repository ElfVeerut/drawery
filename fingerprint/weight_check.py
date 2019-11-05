#Copyright https://github.com/tatobari

#! /usr/bin/python2

import time
import sys

EMULATE_HX711=False

referenceUnit = 1
if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)
# If you're experiencing super random values, change these values to MSB or LSB until to get more stable values.
# The first parameter is the order in which the bytes are used to build the "long" value.
# The second paramter is the order of the bits inside each byte.
hx.set_reading_format("MSB", "MSB")

# HOW TO CALCULATE THE REFFERENCE UNIT
# To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
# In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
# and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
hx.set_reference_unit(60)
#hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()

def checkWeight():
    while True:
    # to use both channels
    #hx.tare_A()
    #hx.tare_B()
    
        try:
        # These three lines are usefull to debug wether to use MSB or LSB in the reading formats
        # for the first parameter of "hx.set_reading_format("LSB", "MSB")".
        # Comment the two lines "val = hx.get_weight(5)" and "print val" and uncomment these three lines to see what it prints.
        
        # np_arr8_string = hx.get_np_arr8_string()
        # binary_string = hx.get_binary_string()
        # print binary_string + " " + np_arr8_string
            while True:
                weight = []
                count = 0
                for _ in range(15):
                    val = max(0, int(hx.get_weight(5)))
                    weight.append(val)
                    print(weight)
                #print(weight)
                check = weight[0]
                for i in weight:
                    if i > check + 5 or i < check-5: break
                    count += 1
                if count == 15:
                    return True
            hx.power_down()
            hx.power_up()
            time.sleep(1)

        except (KeyboardInterrupt, SystemExit):
            cleanAndExit()

