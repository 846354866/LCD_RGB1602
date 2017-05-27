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
        lcd.stopBlink()
        time.sleep(3)

        lcd.blink()
        time.sleep(3)