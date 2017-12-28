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

def drawByCoords(coords, colour):
        for index, coord in enumerate(coords): 
                if index == (len(coords) - 1):
                        draw.line((coords[0], coords[index]), fill=colour)
                else:
                        draw.line((coords[index], coords[index + 1]), fill=colour)

def drawF(minX, minY, maxY, width, height, colour):
        maxX = minX + width

        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, (minY + (height / 2)) + 4),
                (maxX, (minY + (height / 2)) + 4),
                (maxX, minY + (height / 2)),
                (minX + 4, (height / 2)),
                (minX + 4,  minY + (height / 4)),
                (minX + 4, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawU(minX, minY, maxY, width, height, colour):
        maxX = minX + width

        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX, maxY),
                (maxX, minY),
                (maxX - 4, minY),
                (maxX - 4, maxY - 4),
                (minX + 4, maxY - 4),
                (minX + 4, minY)
        ]

        drawByCoords(coords, colour)

def drawC(minX, minY, maxY, width, height, colour):
        maxX = minX + width

        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - 4),
                (minX + 4, maxY - 4),
                (minX + 4, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]

        drawByCoords(coords, colour)

def drawK(minX, minY, maxY, width, height, colour):
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, maxY - 4),

                (minX + 4, minY)
        ]

        drawByCoords(coords, colour)

def drawO(minX, minY, maxY, width, height, colour):
        maxX = minX + width

        draw.rectangle((minX, minY, maxX, maxY), fill=0, outline=1)
        draw.rectangle((minX + 4, minY + 4, maxX - 4, maxY - 4), fill=0, outline=colour)

def drawFuckOff():
        width = 15
        height = 31
        spacing = 2
        word_spacing = 10

        minX = 0
        minY = 0

        maxX = width
        maxY = height

        drawF(minX, minY, maxY, width, height, "blue")
        drawU(width + spacing, minY, maxY, width, height, "blue")
        drawC((width + spacing) * 2, minY, maxY, width, height, "blue")
        drawK((width + spacing) * 3, minY, maxY, width, height, "blue")

        second_word_start = (((width + spacing) * 3) + width) + word_spacing

        drawO(second_word_start, minY, maxY, width, height, "blue")
        drawF(second_word_start + width + spacing, minY, maxY, width, height, "blue")
        drawF(second_word_start + (width + spacing) * 2, minY, maxY, width, height, "blue")

        
        # Then scroll image across matrix...
        for n in range(64 * 2, -((second_word_start + (width + spacing) * 2) + width), -1): # Start off top-left, move off bottom-right
                matrix.Clear()
                # IMPORTANT: *MUST* pass image ID, *NOT* image object!
                matrix.SetImage(image.im.id, n, 0)
                time.sleep(0.05)

        matrix.Clear()

drawFuckOff()