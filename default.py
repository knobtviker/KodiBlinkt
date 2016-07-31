#!/usr/bin/env python

import xbmc
import xbmcgui

import math
import time

from blinkt import set_pixel, show

#LED POSITIONS
LED_STATUS_BREATHE = 0
LED_CPU_TEMPERATURE = 1

#LED BRIGHTNESS PER POSITION
LED_STATUS_BRIGHTNESS = 0.0
#LED_CPU_TEMPERATURE_BRIGHTNESS = 0.0

#LED COLOR PER POSITION
COLOR_BREATHE = [255, 255, 255]
COLOR_CPU_TEMPERATURE = [255, 0, 0]

#HELPER VARS
increasing = True

'''
title = xbmc.getInfoLabel('System.CPUTemperature') 60oC
line1 = xbmc.getInfoLabel('System.CpuUsage') long ass strings, parse by %
line2 = xbmc.getInfoLabel('System.Memory(used.percent)') 15%
line3 = xbmc.getInfoLabel('System.FPS') izracunaj  koliko posto od 100 max fps
'''

while True:
    if xbmc.Player().isPlaying():
        currentTime = xbmc.Player().getTime()
        totalTime = xbmc.Player().getTotalTime()
        if currentTime > 0.0 and totalTime > 0.0:
            timePercent = (currentTime/totalTime)
            if timePercent > 0.000 and timePercent < 0.125:
                set_pixel(0, 0, 255, 0, timePercent)
                set_pixel(1, 0, 255, 0, 0.0)
                set_pixel(2, 0, 255, 0, 0.0)
                set_pixel(3, 0, 255, 0, 0.0)
                set_pixel(4, 0, 255, 0, 0.0)
                set_pixel(5, 0, 255, 0, 0.0)
                set_pixel(6, 0, 255, 0, 0.0)
                set_pixel(7, 0, 255, 0, 0.0)
            if timePercent >= 0.125 and timePercent < 0.250:
                set_pixel(0, 0, 255, 0, timePercent)
                set_pixel(1, 0, 255, 0, timePercent)
                set_pixel(2, 0, 255, 0, 0.0)
                set_pixel(3, 0, 255, 0, 0.0)
                set_pixel(4, 0, 255, 0, 0.0)
                set_pixel(5, 0, 255, 0, 0.0)
                set_pixel(6, 0, 255, 0, 0.0)
                set_pixel(7, 0, 255, 0, 0.0)
            if timePercent >= 0.250 and timePercent < 0.275:
                set_pixel(0, 0, 255, 0, timePercent)
                set_pixel(1, 0, 255, 0, timePercent)
                set_pixel(2, 0, 255, 0, timePercent)
                set_pixel(3, 0, 255, 0, 0.0)
                set_pixel(4, 0, 255, 0, 0.0)
                set_pixel(5, 0, 255, 0, 0.0)
                set_pixel(6, 0, 255, 0, 0.0)
                set_pixel(7, 0, 255, 0, 0.0)
            if timePercent >= 0.275 and timePercent < 0.500:
                set_pixel(0, 0, 255, 0, timePercent)
                set_pixel(1, 0, 255, 0, timePercent)
                set_pixel(2, 0, 255, 0, timePercent)
                set_pixel(3, 0, 255, 0, timePercent)
                set_pixel(4, 0, 255, 0, 0.0)
                set_pixel(5, 0, 255, 0, 0.0)
                set_pixel(6, 0, 255, 0, 0.0)
                set_pixel(7, 0, 255, 0, 0.0)
            if timePercent > 0.500 and timePercent < 0.625:
                set_pixel(0, 0, 255, 0, timePercent)
                set_pixel(1, 0, 255, 0, timePercent)
                set_pixel(2, 0, 255, 0, timePercent)
                set_pixel(3, 0, 255, 0, timePercent)
                set_pixel(4, 0, 255, 0, timePercent)
                set_pixel(5, 0, 255, 0, 0.0)
                set_pixel(6, 0, 255, 0, 0.0)
                set_pixel(7, 0, 255, 0, 0.0)
            if timePercent >= 0.625 and timePercent < 0.750:
                set_pixel(0, 0, 255, 0, timePercent)
                set_pixel(1, 0, 255, 0, timePercent)
                set_pixel(2, 0, 255, 0, timePercent)
                set_pixel(3, 0, 255, 0, timePercent)
                set_pixel(4, 0, 255, 0, timePercent)
                set_pixel(5, 0, 255, 0, timePercent)
                set_pixel(6, 0, 255, 0, 0.0)
                set_pixel(7, 0, 255, 0, 0.0)
            if timePercent >= 0.750 and timePercent < 0.875:
                set_pixel(0, 0, 255, 0, timePercent)
                set_pixel(1, 0, 255, 0, timePercent)
                set_pixel(2, 0, 255, 0, timePercent)
                set_pixel(3, 0, 255, 0, timePercent)
                set_pixel(4, 0, 255, 0, timePercent)
                set_pixel(5, 0, 255, 0, timePercent)
                set_pixel(6, 0, 255, 0, timePercent)
                set_pixel(7, 0, 255, 0, 0.0)
            if timePercent >= 0.875 and timePercent < 1.000:
                set_pixel(0, 0, 255, 0, timePercent)
                set_pixel(1, 0, 255, 0, timePercent)
                set_pixel(2, 0, 255, 0, timePercent)
                set_pixel(3, 0, 255, 0, timePercent)
                set_pixel(4, 0, 255, 0, timePercent)
                set_pixel(5, 0, 255, 0, timePercent)
                set_pixel(6, 0, 255, 0, timePercent)
                set_pixel(7, 0, 255, 0, timePercent)
        else:
            set_pixel(0, 0, 255, 255, 0.1)
            set_pixel(1, 0, 255, 255, 0.1)            
            set_pixel(2, 0, 255, 255, 0.1)
            set_pixel(3, 0, 255, 255, 0.1)
            set_pixel(4, 0, 255, 255, 0.1)
            set_pixel(5, 0, 255, 255, 0.1)            
            set_pixel(6, 0, 255, 255, 0.1)
            set_pixel(7, 0, 255, 255, 0.1)
    else:
        #this block is for stats when not playing.
        if increasing:
            LED_STATUS_BRIGHTNESS += 0.1
        else:
            LED_STATUS_BRIGHTNESS -= 0.1
 
        if (LED_STATUS_BRIGHTNESS >= 0.9):
            increasing = False
 
        if (LED_STATUS_BRIGHTNESS <= 0.1):
            increasing = True
 
        set_pixel(LED_STATUS_BREATHE, COLOR_BREATHE[0], COLOR_BREATHE[1], COLOR_BREATHE[2], LED_STATUS_BRIGHTNESS)

    show()
    time.sleep(0.175)
