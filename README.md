# KodiBlinkt!

This is a proper addon implementation of Pimoroni Blinkt! hardware for Kodi running on Raspberry Pi.

[Read more on Pimoroni Blinkt!](https://shop.pimoroni.com/products/blinkt)

## There are 3 modes of operation.
If XBMC player is playing, 8 LEDs light up green and show progress of media played with number of LEDs glowing green with according brightness.

If XBMC player is buffering, 8 LEDs light up yellow with constant minimum brightness.

If XBMC player is not playing, each LED shows system statistics.

### Idle mode
* First LED - Glows in white and changes brightness from fade in to fade out and vice versa, aka breathing, between 8AM and 8PM. Fixed low brightness during night.
* Second, third, fourth and fifth LED - Glow orange and show CPU usage per core in according brightness.
* Sixth LED - Glows red with brightness set as percentage of current temperature over maximum. Maximum CPU temperature is set as 100 Celsius.
* Seventh LED - Glows blue and shows memory used in brigthness.
* Eight LED - Glows purple and shows FPS out of max 100in according brightness.

## TODO:
* Optimize horrible Python code written during the weekend hype hackathon.
* Figure out how to dynamically link and deploy RPi.GPIO for Kodi from unofficial Kodi repo.
* Build UI and user settings using xbmcgui building blocks.
* Provide several animations and settings per mode or for each mode.
* Build and provide a ZIP and try to submit to some repo online with permission from pirates.
