#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
# SDA: Pin3
# SCL: Pin5

import time
from rgb1602Packge import rgb1602 as LCD

if __name__ == '__main__':

    lcd = LCD.LCD1602()
    lcd.printLCD("Hello world!")

    while True:
        time.sleep(1)

        for i in range(12):
            lcd.scrollDisplayLeft()
            time.sleep(0.2)

        for i in range(31):
            lcd.scrollDisplayRight()
            time.sleep(0.2)

        for i in range(16):
            lcd.scrollDisplayLeft()
            time.sleep(0.2)

        time.sleep(1)
