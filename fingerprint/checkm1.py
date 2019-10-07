
"""

PyFingerprint

Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>

All rights reserved.

"""


import hashlib

from pyfingerprint.pyfingerprint import PyFingerprint


## Tries to search the finger and calculate hash

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


    positionNumber = result[0]

    accuracyScore = result[1]


    if ( positionNumber == -1 ):

        print('no match found!')

       # return 'no match found!'

    else:

        print('Found template at position #' + str(positionNumber))

        print('The accuracy score is: ' + str(accuracyScore))



except Exception as e:

    print('Operation failed!')

    print('Exception message: ' + str(e))

    exit(1)