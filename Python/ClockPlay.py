#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

from datetime import datetime, timedelta
from time import sleep

def timeToString(time:datetime = datetime.now()):
    """ Converts a time to a word sting in swedish """

    result = ""

    _hour = time.hour
    if (_hour > 12) : 
        _hour = _hour -12

    if (_hour == 1):
       result = "ETT"
    elif(_hour == 2):
        result = "Två"
    elif(_hour == 3):
        result = "Tre"
    elif(_hour == 4):
        result = "Fyra"
    elif(_hour == 5):
        result = "Fem"
    elif(_hour == 6):
        result = "Sex"
    elif(_hour == 7):
        result = "Sju"
    elif(_hour == 8):
        result = "Åtta"
    elif(_hour == 9):
        result = "Nio"
    elif(_hour == 10):
        result = "Tio"
    elif(_hour == 11):
        result = "Elva"
    elif(_hour == 12):
        result = "Tolv"

    _minute = time.minute
    if (_minute == 0):
        print(f'Klockan är hel')
    elif (_minute <= 1):
        print(f'Klockan är en minut över. ({_minute})')
    elif (_minute <=  2):
        print(f'Klockan är två minuter över. ({_minute})')
    elif (_minute <=  3):
        print(f'Klockan är tre minuter över. ({_minute})')
    elif (_minute <=  5):
        print(f'Klockan är fem minuter över. ({_minute})')
    elif (_minute <= 10):
        print(f'Klockan är tio minuter över. ({_minute})')
    elif (_minute <= 15):
        print(f'Klockan är kvart över. ({_minute})')
    elif (_minute <= 30):
        print(f'Klockan är halv. ({_minute})')

    elif (_minute <= 31):
        print(f'Klockan är en minut över halv. ({_minute})')
    elif (_minute <=  32):
        print(f'Klockan är två minuter över halv. ({_minute})')
    elif (_minute <=  33):
        print(f'Klockan är tre minuter över halv. ({_minute})')
    elif (_minute <=  35):
        print(f'Klockan är fem minuter över halv. ({_minute})')
    elif (_minute <= 40):
        print(f'Klockan är tio minuter över halv. ({_minute})')

    elif (_minute <= 45):
        print(f'Klockan är kvart i. ({_minute})')
    elif (_minute <= 50):
        print(f'Klockan är tio minuter i. ({_minute})')
    elif (_minute <=  55):
        print(f'Klockan är fem minuter i. ({_minute})')

    elif (_minute <=  57):
        print(f'Klockan är tre minuter i. ({_minute})')
    elif (_minute <=  58):
        print(f'Klockan är två minuter i. ({_minute})')
    elif (_minute <= 59):
        print(f'Klockan är en minut i. ({_minute})')

    else:
        print(f'Klockan är {_minute}')
    return result


def main():
    """ Main entry point of the app """

    time = datetime.strptime("03/02/21 16:30", "%d/%m/%y %H:%M")
    print(time)
    while(True):
        time =  time + timedelta(minutes=1)
        tt = timeToString(time)
        #print(f'time : {timeToString(time)}')
        sleep(1)



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()