#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
# SDA: Pin3
# SCL: Pin5

import time
from rgb1602Packge import rgb1602 as LCD

thisChar = 'a'

if __name__ == '__main__':

    lcd = LCD.LCD1602()
    lcd.cursor()

    while True:
        if thisChar == 'm':
            lcd.rightToLeft()

        if thisChar == 's':
            lcd.leftToRight()

        if thisChar > 'z':
            lcd.home()
            thisChar = 'a'

        lcd.write(thisChar)

        thisChar = ord(thisChar)
        thisChar += 1
        thisChar = chr(thisChar)
        time.sleep(0.5)
