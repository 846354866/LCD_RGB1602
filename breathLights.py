#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
# SDA: Pin3
# SCL: Pin5

import time
from rgb1602Packge import rgb1602 as LCD


def breath(lcd):
    count = range(256)
    for i in count:
        lcd.setRGB(i, 000, i)
        time.sleep(0.005)

    count.reverse()
    for i in count:
        lcd.setRGB(i, 000, i)
        time.sleep(0.005)

if __name__ == '__main__':

    lcd = LCD.LCD1602()
    lcd.printLCD("Breath lights!")

    while True:
        breath(lcd)
