#!/usr/bin/env python

import xbmc

import math
import time
import datetime

from blinkt import set_pixel, show, clear

#LED POSITIONS
LED_STATUS_BREATHE = 0
LED_CPU_CORE_1 = 1
LED_CPU_CORE_2 = 2
LED_CPU_CORE_3 = 3
LED_CPU_CORE_4 = 4
LED_CPU_TEMPERATURE = 5
LED_MEMORY_USED = 6
LED_FPS = 7

#LED BRIGHTNESS PER POSITION
LED_STATUS_BRIGHTNESS = 0.0
LED_CPU_CORE_1_BRIGHTNESS = 0.0
LED_CPU_CORE_2_BRIGHTNESS = 0.0
LED_CPU_CORE_3_BRIGHTNESS = 0.0
LED_CPU_CORE_4_BRIGHTNESS = 0.0
LED_CPU_TEMPERATURE_BRIGHTNESS = 0.0
LED_MEMORY_USED_BRIGHTNESS = 0.0
LED_FPS_BRIGHTNESS = 0.0

#LED COLOR PER POSITION
COLOR_BREATHE = [255, 255, 255]
COLOR_CPU_USAGE = [202, 161, 47]
COLOR_CPU_TEMPERATURE = [204, 0, 0]
COLOR_MEMORY_USED = [0, 102, 204]
COLOR_FPS = [153, 51, 255]

#HELPER VARS
increasing = True

if __name__ == '__main__':
    monitor = xbmc.Monitor()

    while not monitor.abortRequested():
        if monitor.waitForAbort(0.175):
            clear()
            show()
            break
        else:    
            if xbmc.Player().isPlaying():
                currentTime = xbmc.Player().getTime()
                totalTime = xbmc.Player().getTotalTime()
                if currentTime > 0.0 and totalTime > 0.0:
                    timePercent = (currentTime/totalTime)
                    if timePercent > 0.000 and timePercent < 0.125:
                        for i in range(8):
                            if i in range(1,8):
                                 set_pixel(i , 0, 255, 0, 0.0)
                            else:
                                 if timePercent <= 0.1:
                                     timePercent = 0.1
                                 set_pixel(i, 0, 255, 0, timePercent)
                    if timePercent >= 0.125 and timePercent < 0.250:
                        for i in range(8):
                            if i in range(2,8):
                                 set_pixel(i , 0, 255, 0, 0.0)
                            else:
                                 set_pixel(i, 0, 255, 0, timePercent)
                    if timePercent >= 0.250 and timePercent < 0.275:
                        for i in range(8):
                            if i in range(3,8):
                                 set_pixel(i , 0, 255, 0, 0.0)
                            else:
                                 set_pixel(i, 0, 255, 0, timePercent)
                    if timePercent >= 0.275 and timePercent < 0.500:
                        for i in range(8):
                            if i in range(4,8):
                                 set_pixel(i , 0, 255, 0, 0.0)
                            else:
                                 set_pixel(i, 0, 255, 0, timePercent)

                    if timePercent > 0.500 and timePercent < 0.625:
                        for i in range(8):
                            if i in range(5,8):
                                 set_pixel(i , 0, 255, 0, 0.0)
                            else:
                                 set_pixel(i, 0, 255, 0, timePercent)
                    if timePercent >= 0.625 and timePercent < 0.750:
                        for i in range(8):
                            if i in range(6,8):
                                 set_pixel(i , 0, 255, 0, 0.0)
                            else:
                                 set_pixel(i, 0, 255, 0, timePercent)
                    if timePercent >= 0.750 and timePercent < 0.875:
                        for i in range(8):
                            if i in range(7,8):
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

                cpuUsage = xbmc.getInfoLabel('System.CpuUsage')
                cpuUsageParsed = []
                cpuUsageSplitted = cpuUsage.split("%")
                for cpu in cpuUsageSplitted:
                    core = cpu[6:].strip()
                    if core:
                        cpuUsageParsed.append(core)
            
                LED_CPU_CORE_1_BRIGHTNESS = float(cpuUsageParsed[0])/100.0
                LED_CPU_CORE_2_BRIGHTNESS = float(cpuUsageParsed[1])/100.0
                LED_CPU_CORE_3_BRIGHTNESS = float(cpuUsageParsed[2])/100.0
                LED_CPU_CORE_4_BRIGHTNESS = float(cpuUsageParsed[3])/100.0

                cpuTemperature = xbmc.getInfoLabel('System.CPUTemperature')
                cpuTemperature = cpuTemperature[:-3]
                LED_CPU_TEMPERATURE_BRIGHTNESS = float(cpuTemperature)/100.0
                
                memoryUsed = xbmc.getInfoLabel('System.Memory(used.percent)')
                memoryUsed = memoryUsed[:-1]
                LED_MEMORY_USED_BRIGHTNESS = float(memoryUsed)/100.0

                fps = xbmc.getInfoLabel('System.FPS')
                LED_FPS_BRIGHTNESS = float(fps)/100.0

                set_pixel(LED_STATUS_BREATHE, COLOR_BREATHE[0], COLOR_BREATHE[1], COLOR_BREATHE[2], LED_STATUS_BRIGHTNESS)
                set_pixel(LED_CPU_CORE_1, COLOR_CPU_USAGE[0], COLOR_CPU_USAGE[1], COLOR_CPU_USAGE[2], LED_CPU_CORE_1_BRIGHTNESS)
                set_pixel(LED_CPU_CORE_2, COLOR_CPU_USAGE[0], COLOR_CPU_USAGE[1], COLOR_CPU_USAGE[2], LED_CPU_CORE_2_BRIGHTNESS)
                set_pixel(LED_CPU_CORE_3, COLOR_CPU_USAGE[0], COLOR_CPU_USAGE[1], COLOR_CPU_USAGE[2], LED_CPU_CORE_3_BRIGHTNESS)
                set_pixel(LED_CPU_CORE_4, COLOR_CPU_USAGE[0], COLOR_CPU_USAGE[1], COLOR_CPU_USAGE[2], LED_CPU_CORE_4_BRIGHTNESS)
                set_pixel(LED_CPU_TEMPERATURE, COLOR_CPU_TEMPERATURE[0], COLOR_CPU_TEMPERATURE[1], COLOR_CPU_TEMPERATURE[2], LED_CPU_TEMPERATURE_BRIGHTNESS)            
                set_pixel(LED_MEMORY_USED, COLOR_MEMORY_USED[0], COLOR_MEMORY_USED[1], COLOR_MEMORY_USED[2], LED_MEMORY_USED_BRIGHTNESS)
                set_pixel(LED_FPS, COLOR_FPS[0], COLOR_FPS[1], COLOR_FPS[2], LED_FPS_BRIGHTNESS)

            show()
