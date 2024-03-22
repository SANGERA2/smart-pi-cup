#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0
device = 0
logging.basicConfig(level=logging.DEBUG)
try:
    # display with hardware SPI:
    ''' Warning!!!Don't creation of multiple displayer objects!!! '''
    #disp = LCD_2inch.LCD_2inch(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_2inch.LCD_2inch()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()
    #Set the backlight to 100
    disp.bl_DutyCycle(100)

    logging.info("show image " + sys.argv[1])
    image = Image.open(sys.argv[1])
    image = image.rotate(180)
    disp.ShowImage(image)
    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)

secs = 5
try:
    secs = int(sys.argv[2])
except:
    print("Using default time")
time.sleep(secs)
