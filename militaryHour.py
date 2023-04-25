#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s) -> str:
    # Write your code here
    retString = ''
    s_substr = s[0:len(s) - 2]
    s_last_2_char = s[-2:]
    hour = (s_substr.split(':')[0]).rjust(2, '0')
    min = s_substr.split(':')[1].rjust(2, '0')
    sec = s_substr.split(':')[2].rjust(2, '0')
    hour = int(hour)

    if s_last_2_char == 'PM':

        if hour == 12:
            retString = str(hour) + ':' + min + ':' + sec

        if hour < 12:
            hour = hour + 12
            strHour = str(hour).rjust(2, '0')
            retString = strHour + ':' + min + ':' + sec
        if hour > 12:
            strHour = str(hour).rjust(2, '0')
            retString = strHour + ':' + str(min).rjust(2, '0') + ':' + str(sec).rjust(2, '0')

    if s_last_2_char == 'AM':
        if hour == 12:
            hour = hour - 12
            strHour = str(hour).rjust(2, '0')
            retString = strHour + ':' + min + ':' + sec

        if hour < 12:
            strHour = str(hour).rjust(2, '0')
            retString = strHour + ':' + min + ':' + sec

    return retString


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
