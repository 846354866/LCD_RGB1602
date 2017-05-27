#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
# SDA: Pin3
# SCL: Pin5

import time
from rgb1602Packge import rgb1602 as LCD
import serial

ser = serial.Serial("/dev/ttyAMA0", 9600)

if __name__ == '__main__':

    lcd = LCD.LCD1602()

    while True:
        count = ser.inWaiting()
        if count:
            time.sleep(0.5)
            lcd.clear()
            
            recv = ser.read(count)
            for i in range(len(recv)):
                lcd.write(recv[i])

        ser.flushInput()
        time.sleep(0.1)
