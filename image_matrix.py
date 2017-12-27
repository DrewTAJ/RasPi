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
image = Image.new("1", (64 * 10, 32)) # Can be larger than matrix if wanted!!
draw  = ImageDraw.Draw(image)    # Declare Draw instance before prims
# Draw some shapes into image (no immediate effect on matrix)...

def drawF(minX, minY, maxX, maxY, width, height, colour):
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 5, maxY),
                (minX + 5, (minY + (height / 2)) + 5),
                (maxX, (minY + (height / 2)) + 5),
                (maxX, minY + (height / 2)),
                (minX + 5,  minY + (height / 2)),
                (minX + 5, minY + 5),
                (maxX, minY + 5),
                (maxX, minY)
        ]

        for index, coord in enumerate(coords): 
                if index == (len(coords) - 1):
                        draw.line((coords[0], coords[index]), fill=colour)
                else:
                        draw.line((coords[index], coords[index + 1]), fill=colour)

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
        width = 16
        height = 32

        minX = 0
        minY = 0

        maxX = width
        maxY = height

        drawF(minX, minY, maxX, maxY, width, height, 1)
        # drawU(minX + width + 1, maxX + (width * 2) + 1)
        # drawC(maxX + (width * 2) + 1, maxX + (width * 3) + 1)
        # drawK(maxX + (width * 3) + 1, maxX + (width * 4) + 1)

        # drawO(maxX + (width * 5) + 1, maxX + (width * 6) + 1)
        # drawF(maxX + (width * 6) + 1, maxX + (width * 7) + 1)
        # drawF(maxX + (width * 7) + 1, maxX + (width * 8) + 1)

drawFuckOff()

# Then scroll image across matrix...
for n in range(64 * 2, -32, -1): # Start off top-left, move off bottom-right
        matrix.Clear()
        # IMPORTANT: *MUST* pass image ID, *NOT* image object!
        matrix.SetImage(image.im.id, n, 0)
        time.sleep(0.05)

matrix.Clear()