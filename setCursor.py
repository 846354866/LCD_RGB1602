#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
# SDA: Pin3
# SCL: Pin5

import smbus
import time
import rgb1602 as LCD

numRows = 2
numCols = 16

if __name__ == '__main__':

    lcd = LCD.LCD1602()

    while True:
        for c in range(ord('a'), ord('z')+1):
            for i in range(numRows):
                for n in range(numCols):
                    lcd.setCursor(n, i)
                    lcd.write(chr(c))
                    time.sleep(0.1)
