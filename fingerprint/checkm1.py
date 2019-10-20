"""

PyFingerprint

Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>

All rights reserved.
https://gitmemory.com/issue/bastianraschke/pyfingerprint/70/480343013
"""

import hashlib

from pyfingerprint.pyfingerprint import PyFingerprint

def check():

    ## Tries to search the finger 

    try:

        finger = PyFingerprint('/dev/ttyUSB0')


        print('Waiting for finger...')


        ## Wait that finger is read

        while ( finger.readImage() == False ):

            pass


        ## Converts read image to characteristics and stores it in charbuffer 1

        finger.convertImage(0x01)


        ## Searchs template

        result = finger.searchTemplate()
        print(result)


        positionNumber = result[0]

        accuracyScore = result[1]


        if ( positionNumber == -1 ):
            return (False)
            print('no match found!')


        else:
            return (True)
            print('Found template at position #' + str(positionNumber))

            



    except Exception as e:
        return (False)
        print('Operation failed!')

        print('Exception message: ' + str(e))

        exit(1)   
