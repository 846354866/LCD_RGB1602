#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
# SDA: Pin3
# SCL: Pin5

import time
from rgb1602Packge import rgb1602 as LCD


def breath(lcd, colorAddr):
    for i in range(255):
        lcd.setPWM(colorAddr, i)
        time.sleep(0.005)
    time.sleep(0.5)

    for i in range(255):
        lcd.setPWM(colorAddr, 255-i)
        time.sleep(0.005)
    time.sleep(0.5)

if __name__ == '__main__':

    lcd = LCD.LCD1602()
    lcd.printLCD("Gradual change!")

    while True:
        breath(lcd, LCD.REG_RED)
        breath(lcd, LCD.REG_GREEN)
        breath(lcd, LCD.REG_BLUE)
