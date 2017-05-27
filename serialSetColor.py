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
    lcd.printLCD("Set color")

    while True:
        count = ser.inWaiting()
        if count:
            recv = ser.read(count)
            if len(recv) == 11:
                r = int(recv[:3])
                g = int(recv[4:7])
                b = int(recv[8:11])

                lcd.setRGB(r, g, b)
                print "r=",r
                print "g=",g
                print "b=",b

        ser.flushInput()
        time.sleep(0.1)