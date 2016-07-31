# KodiBlinkt!

This is a proper addon implementation of Pimoroni Blinkt! hardware for Kodi running on Raspberry Pi.

[Read more on Pimoroni Blinkt!](https://shop.pimoroni.com/products/blinkt)

## There are 3 modes of operation.
If XBMC player is playing, 8 LEDs light up green and show progress of media played with number of LEDs glowing green with according brightness.

If XBMC player is buffering, 8 LEDs light up yellow with constant minimum brightness.

If XBMC player is not playing, each LED shows system statistics.

### Idle mode
* First LED - Glows in white and changes brightness from fade in to fade out and vice versa, aka breathing. 


## TODO:
* Add more system stats for idle mode using xbmc InfoLabels.
* Optimize horrible Python code written during the weekend hype hackathon.
* Figure out how to dynamically link and deploy RPi.GPIO for Kodi from unofficial Kodi repo.
* Build UI and user settings using xbmcgui building blocks.
* Provide several animations and settings per mode or for each mode.
* Build and provide a ZIP and try to submit to some repo online with permission from pirates.
