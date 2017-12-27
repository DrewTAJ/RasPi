#!/usr/bin/python
 
# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.
 
# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm
 
import Image
import ImageDraw
import time
from rgbmatrix import Adafruit_RGBmatrix
 
# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 3)
matrix.SetWriteCycles(5)
 
# Bitmap example w/graphics prims
image = Image.new("1", (64 * 7, 32)) # Can be larger than matrix if wanted!!
draw  = ImageDraw.Draw(image)    # Declare Draw instance before prims
# Draw some shapes into image (no immediate effect on matrix)...

width = 16
height = 32

minY = 0
maxY = height

def drawF(minX, maxX):
        draw.line((minX, minY, minX, maxY), fill=1)
        draw.line((minX, maxY, minX + 10, maxY), fill=1)
        draw.line((minX + 10, maxY, minX + 10, maxY - 10), fill=1)
        draw.line((minX + 10, maxY - 10, maxX, maxY - 10), fill=1)
        draw.line((maxX, maxY - 10, maxX, maxY - 15), fill=1)
        draw.line((maxX, maxY - 15, minX + 10, maxY - 15), fill = 1)
        draw.line((minX + 10, maxY - 15, minX + 10, minY + 10), fill=1)
        draw.line((minX + 10, minY + 10, maxX, minY + 10), fill=1)
        draw.line((maxX, minY + 10, maxX, minY), fill=1)
        draw.line((maxX, minY, minX + 10, minY), fill=1)
        draw.line((minX + 10, minY, minX, minY), fill=1)

def drawU(minX, maxX):
        draw.line((minX, minY, minX, maxY), fill=1)
        draw.line((minX, maxY, maxX, maxY), fill=1)
        draw.line((maxX, maxY, maxX, minY), fill=1)
        draw.line((maxX, minY, maxX - (width / 4), minY), fill=1)
        draw.line((maxX - (width / 4), minY, maxX - (width / 4), maxY - (height / 4)), fill=1)
        draw.line((maxX - (width / 4), maxY - (height / 4), minX + (width / 4), maxY - (height / 4)), fill=1)
        draw.line((minX + (width / 4), maxY - (height / 4), minX + (width / 4), minY), fill=1)
        draw.line((minX + (width / 4), minY, minX, minY), fill=1)

def drawC(minX, maxX):
        draw.line((minX, minY, minX, maxY), fill=1)
        draw.line((minX, maxY, maxX, maxY), fill=1)
        draw.line((maxX, maxY, maxX, maxY - (height / 4)), fill=1)
        draw.line((maxX, maxY - (height / 4), minX + (width / 4), maxY - (height / 4)), fill=1)
        draw.line((minX + (width / 4), maxY - (height / 4), minX + (width / 4), minY + (height / 4)), fill=1)
        draw.line((minX + (width / 4), minY + (height / 4), maxX, minY + (height / 4)), fill=1)
        draw.line((maxX, minY + (height / 4), maxX, minY), fill=1)
        draw.line((maxX, minY, minX, minY), fill=1)


def drawK(minX, maxX):
        draw.line((minX, minY, minX, maxY), fill=1)
        draw.line((minX, maxY, minX + (width / 4), maxY), fill=1)
        draw.line((minX + (width / 4), maxY, minX + (width / 4), maxY - (maxY / 4)), fill=1)


        draw.line((maxX, minY, maxX - (width / 4), minY), fill=1)
        draw.line((maxX - (width / 4), minY, minX + (width / 4), minY + (height / 2)), fill=1)
        draw.line((minX + (width / 4), minY + (height / 2), minX + (width /4), minY), fill=1)
        draw.line((minX + (width / 4), minY, minX, minY), fill=1)

def drawO(minX, maxX):
        draw.rectangle((minX, minY, maxX, maxY), fill=0, outline=1)
        draw.rectangle((minX + (width / 4), minY + (height / 4), maxX - (width / 4), maxY - (height / 4)), fill=0, outline=1)

def drawFuckOff():
        minX = 0
        maxX = width

        drawF(minX, maxX)
        drawU(minX + width + 1, maxX + (width * 2) + 1)
        drawC(maxX + (width * 2) + 1, maxX + (width * 3) + 1)
        drawK(maxX + (width * 3) + 1, maxX + (width * 4) + 1)
        drawO(maxX + (width * 4) + 1, maxX + (width * 5) + 1)
        drawF(maxX + (width * 5) + 1, maxX + (width * 6) + 1)
        drawF(maxX + (width * 6) + 1, maxX + (width * 7) + 1)

drawFuckOff()

# Then scroll image across matrix...
for n in range(64 * 2, -32, -1): # Start off top-left, move off bottom-right
        matrix.Clear()
        # IMPORTANT: *MUST* pass image ID, *NOT* image object!
        matrix.SetImage(image.im.id, n, 0)
        time.sleep(0.05)

matrix.Clear()