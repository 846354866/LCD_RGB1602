#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
# SDA: Pin3
# SCL: Pin5

import time
from rgb1602Packge import rgb1602 as LCD

if __name__ == '__main__':

    lcd = LCD.LCD1602()
    lcd.setRGB(0, 0, 255)
    lcd.printLCD("Hello world!")
    num = 0

    while True:
        lcd.setCursor(0, 1)
        lcd.printLCD(num)
        num += 1
        time.sleep(1)
