#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
# SDA: Pin3
# SCL: Pin5

import smbus
import time
import rgb1602 as LCD

if __name__ == '__main__':

    lcd = LCD.LCD1602()
    lcd.printLCD("Hello world!")

    while True:
        lcd.noDisplay()
        time.sleep(0.5)

        lcd.blink()
        time.sleep(0.5)
