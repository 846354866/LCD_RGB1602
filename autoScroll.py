#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
# SDA: Pin3
# SCL: Pin5

import time
from rgb1602Packge import rgb1602 as LCD

if __name__ == '__main__':

    lcd = LCD.LCD1602()

    while True:
        lcd.setCursor(0, 0)
        for i in range(10):
            lcd.printLCD(i)
            time.sleep(0.5)

        lcd.setCursor(16, 1)
        lcd.autoscroll()
        for i in range(10):
            lcd.printLCD(i)
            time.sleep(0.5)
        lcd.noAutoscroll()

        lcd.clear()
