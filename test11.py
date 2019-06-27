import time
from neopixel import *
from PIL import Image, ImageDraw, ImageFont
import argparse
import signal
import sys

LED_COUNT      = 256
LED_PIN        = 21
LED_FREQ_HZ    = 800000
LED_DMA        = 10
LED_BRIGHTNESS = 20
LED_INVERT     = False
LED_CHANNEL    = 0
LED_STRIP      = ws.WS2811_STRIP_GRB

def displayGIF(strip, imageName, wait_ms=500):
        im = Image.open(imageName)
        width = im.size[0]
        height = im.size[1]

        try:
                while 1:
                        buf = im.convert('RGB')
                        i = 0

                        for x in range(0, width):
                                for y in range(0, height):
                                        if x%2 != 0:
                                                r,g,b = buf.getpixel((x,7-y))
                                        else:
                                                r,g,b = buf.getpixel((x,y))

                                        strip.setPixelColor(i, Color(r, g, b))
                                        i += 1
                        strip.show()
                        im.seek(im.tell()+1)
                        time.sleep(im.info["duration"]/1000.0)
        except EOFError:
                pass


if __name__ == '__main__':

    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

    strip.begin()

    while True:


            displayGIF(strip, "gifs/type10.gif")
