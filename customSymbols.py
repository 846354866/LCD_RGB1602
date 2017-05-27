#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
# SDA: Pin3
# SCL: Pin5

import smbus
import time
import rgb1602 as LCD

heart = [
    0b00000,
    0b01010,
    0b11111,
    0b11111,
    0b11111,
    0b01110,
    0b00100,
    0b00000
]

smiley = [
    0b00000,
    0b00000,
    0b01010,
    0b00000,
    0b00000,
    0b10001,
    0b01110,
    0b00000
]

frownie = [
    0b00000,
    0b00000,
    0b01010,
    0b00000,
    0b00000,
    0b00000,
    0b01110,
    0b10001
]

armsDown = [
    0b00100,
    0b01010,
    0b00100,
    0b00100,
    0b01110,
    0b10101,
    0b00100,
    0b01010
]

armsUp = [
    0b00100,
    0b01010,
    0b00100,
    0b10101,
    0b01110,
    0b00100,
    0b00100,
    0b01010
]

if __name__ == '__main__':

    lcd = LCD.LCD1602()
    lcd.customSymbol(0, tuple(heart))
    lcd.customSymbol(1, tuple(smiley))
    lcd.customSymbol(2, tuple(frownie))
    lcd.customSymbol(3, tuple(armsDown))
    lcd.customSymbol(4, tuple(armsUp))

    lcd.setCursor(0, 0)
    lcd.printLCD("I ")
    lcd.write(0)
    lcd.printLCD(" Raspberry Pi! ")
    lcd.write(1)

    while True:
        lcd.setCursor(4, 1)
        lcd.write(3)
        time.sleep(0.2)
        lcd.setCursor(4, 1)
        lcd.write(4)
        time.sleep(0.2)
