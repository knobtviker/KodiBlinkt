#!/usr/bin/env python

import xbmc
import xbmcgui

import math
import time
import datetime

from blinkt import set_pixel, show, clear

#LED POSITIONS
LED_STATUS_BREATHE = 0
LED_CPU_TEMPERATURE = 1

#LED BRIGHTNESS PER POSITION
LED_STATUS_BRIGHTNESS = 0.0
LED_CPU_TEMPERATURE_BRIGHTNESS = 0.0

#LED COLOR PER POSITION
COLOR_BREATHE = [255, 255, 255]
COLOR_CPU_TEMPERATURE = [255, 0, 0]

#HELPER VARS
increasing = True

'''
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
                for i in range(8):
                    if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7:
                         set_pixel(i , 0, 255, 0, 0.0)
                    else:
                         set_pixel(i, 0, 255, 0, timePercent)
            if timePercent >= 0.125 and timePercent < 0.250:
                for i in range(8):
                    if i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7:
                         set_pixel(i , 0, 255, 0, 0.0)
                    else:
                         set_pixel(i, 0, 255, 0, timePercent)
            if timePercent >= 0.250 and timePercent < 0.275:
                for i in range(8):
                    if i == 3 or i == 4 or i == 5 or i == 6 or i == 7:
                         set_pixel(i , 0, 255, 0, 0.0)
                    else:
                         set_pixel(i, 0, 255, 0, timePercent)
            if timePercent >= 0.275 and timePercent < 0.500:
                for i in range(8):
                    if i == 4 or i == 5 or i == 6 or i == 7:
                         set_pixel(i , 0, 255, 0, 0.0)
                    else:
                         set_pixel(i, 0, 255, 0, timePercent)

            if timePercent > 0.500 and timePercent < 0.625:
                for i in range(8):
                    if i == 5 or i == 6 or i == 7:
                         set_pixel(i , 0, 255, 0, 0.0)
                    else:
                         set_pixel(i, 0, 255, 0, timePercent)
            if timePercent >= 0.625 and timePercent < 0.750:
                for i in range(8):
                    if i == 6 or i == 7:
                         set_pixel(i , 0, 255, 0, 0.0)
                    else:
                         set_pixel(i, 0, 255, 0, timePercent)
            if timePercent >= 0.750 and timePercent < 0.875:
                for i in range(8):
                    if i == 7:
                         set_pixel(i , 0, 255, 0, 0.0)
                    else:
                         set_pixel(i, 0, 255, 0, timePercent)
            if timePercent >= 0.875 and timePercent < 1.000:
                for i in range(8):
                    set_pixel(i , 0, 255, 0, timePercent)
        else:
            #this block is for intermediate state before playing
            for i in range(8):
                set_pixel(i , 255, 255, 0, 0.1)
    else:
        #this block is for stats when not playing.
        now = datetime.datetime.now().time()
        start = datetime.time(8,00)
        end = datetime.time(20,00)
        if start <= now <= end:
            if increasing:
                LED_STATUS_BRIGHTNESS += 0.1
            else:
                LED_STATUS_BRIGHTNESS -= 0.1
 
            if (LED_STATUS_BRIGHTNESS >= 0.9):
                increasing = False
 
            if (LED_STATUS_BRIGHTNESS <= 0.1):
                increasing = True
        else:
            LED_STATUS_BRIGHTNESS = 0.1

        cpuTemperature = xbmc.getInfoLabel('System.CPUTemperature')
        cpuTemperature = cpuTemperature[:-3]
        LED_CPU_TEMPERATURE_BRIGHTNESS = float(cpuTemperature)/100.0
        set_pixel(LED_STATUS_BREATHE, COLOR_BREATHE[0], COLOR_BREATHE[1], COLOR_BREATHE[2], LED_STATUS_BRIGHTNESS)
        set_pixel(LED_CPU_TEMPERATURE, COLOR_CPU_TEMPERATURE[0], COLOR_CPU_TEMPERATURE[1], COLOR_CPU_TEMPERATURE[2], LED_CPU_TEMPERATURE_BRIGHTNESS)
        set_pixel(2, 0, 0, 0, 0.0)
        set_pixel(3, 0, 0, 0, 0.0)
        set_pixel(4, 0, 0, 0, 0.0)
        set_pixel(5, 0, 0, 0, 0.0)            
        set_pixel(6, 0, 0, 0, 0.0)
        set_pixel(7, 0, 0, 0, 0.0)

    show()
    time.sleep(0.175)
