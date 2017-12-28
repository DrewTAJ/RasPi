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

def drawA(minX, minY, maxY, width, height, colour):
        maxX = minX + width

        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, minY + (height / 2)),
                (maxX - 4, minY + (height / 2)),
                (maxX - 4, maxY),
                (maxX, maxY),
                (maxX, minY)
        ]
        draw.rectangle((minX + 4, minY + 4, maxX - 4, minY + 4 + 7), fill=0, outline=colour)
        drawByCoords(coords, colour)

def drawB(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX - 4, maxY),
                (maxX, maxY - 4),
                (maxX, minY + (height / 2) + 4),
                (maxX - 4, minY + (height / 2)),
                (maxX, minY + (height / 2) - 4),
                (maxX, minY + 4),
                (maxX - 4, minY)
        ]
        drawByCoords(coords, colour)

        coords = [
                (minX + 4, minY + 4),
                (minX + 4, minY + (height / 2) - 2),
                (maxX - 8, minY + (height / 2) - 2),
                (maxX - 4, minY + (height / 2) - 4),
                (maxX - 4, minY + 8),
                (maxX - 8, minY + 4)
        ]
        drawByCoords(coords, colour)

        coords = [
                (minX + 4, minY + (height / 2) + 2),
                (minX + 4, maxY - 4),
                (maxX - 8, maxY - 4),
                (maxX - 4, maxY - 8),
                (maxX - 4, minY + (height / 2) + 6),
                (maxX - 8, minY + (height / 2) + 2)
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

def drawD(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX - 4, maxY),
                (maxX, maxY - 4),
                (maxX, minY + 4),
                (maxX - 4, minY)
        ]
        drawByCoords(coords, colour)

        coords = [
                (minX + 4, minY + 4),
                (minX + 4, maxY - 4),
                (maxX - 8, maxY - 4),
                (maxX - 4, maxY - 8),
                (maxX - 4, minY + 8),
                (maxX - 8, minY + 4),
        ]
        drawByCoords(coords, colour)

def drawE(minX, minY, maxY, width, height, colour):
        maxX = minX + width

        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - 4),
                (minX + 4, maxY - 4),
                (minX + 4, minY + (height / 2) + 2),
                (maxX, minY + (height / 2) + 2),
                (maxX, minY + (height / 2) - 2),
                (minX + 4, minY + (height / 2) - 2),
                (minX + 4, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)
        

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

def drawG(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - (height / 2)),
                (minX + 8, maxY - (height / 2)),
                (minX + 8, maxY - (height / 2) + 4),
                (maxX - 4, maxY - (height / 2) + 4),

                (maxX -4, maxY - 4),
                (minX + 4, maxY - 4),
                (minX + 4, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawH(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, (minY + (height / 2)) + 1),
                (maxX - 4, (minY + (height / 2)) + 1),
                (maxX - 4, maxY),
                (maxX, maxY),
                (maxX, minY),
                (maxX - 4, minY),
                (maxX - 4, (minY + (height / 2)) - 2),
                (minX + 4, (minY + (height / 2)) - 2),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawI(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, minY + 4),

                (minX + (width / 2) - 2, minY + 4),
                (minX + (width / 2) - 2, maxY - 4),

                (minX, maxY - 4),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - 4),

                (minX + (width / 2) + 2, maxY - 4),
                (minX + (width / 2) + 2, minY + 4),

                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawJ(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, minY + 4),
                (minX + (width / 2) - 1, minY + 4),
                (minX + (width / 2) - 1, maxY - 4),
                (minX + 3, maxY - 4),
                (minX + 3, minY + (height / 2) - 2),
                (minX, minY + (height / 2) - 2),
                (minX, maxY),
                (minX + (width / 2) + 3, maxY),
                (minX + (width / 2) + 3, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawK(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),

                (minX + 4, maxY - (height / 2) + 2),
                (maxX - 5, maxY - (height / 2) + 2),

                (maxX - 4, maxY - (height / 2) + 4),
                (maxX - 4, maxY),
                (maxX, maxY),
                (maxX, minY + (height / 2) + 4),

                (maxX - 2, minY + (height / 2) + 1),

                (maxX, minY + (height / 2) - 3),
                (maxX, minY),
                (maxX - 4, minY),
                (maxX - 4, minY + (height / 2) - 4),

                (maxX - 5, minY + (height / 2) - 1),
                (minX + 4, minY + (height / 2) - 1),

                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawL(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - 4),
                (minX + 4, maxY - 4),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawN(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),

                (minX + 4, minY + 12),

                (maxX - 4, maxY),

                (maxX, maxY),
                (maxX, minY),
                (maxX - 4, minY),

                (maxX - 4, maxY - 12),

                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawO(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        draw.rectangle((minX, minY, maxX, maxY), fill=0, outline=colour)
        draw.rectangle((minX + 4, minY + 4, maxX - 4, maxY - 4), fill=0, outline=colour)

def drawP(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, minY + (4 * 3)),
                (maxX, minY + (4 * 3)),
                (maxX, minY)
        ]
        draw.rectangle((minX + 4, minY + 4, maxX - 4, minY + 8), fill=0, outline=colour)
        drawByCoords(coords, colour)

def drawR(minX, minY, maxY, width, height, colour):
        maxX = minX + width

        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),

                (minX + 4, minY + (height / 2)),
                (maxX - 8, minY + (height / 2)),
                (maxX - 8, maxY),
                (maxX - 4, maxY),
                (maxX - 4, minY + (height / 2)),

                (maxX, minY + (height / 2) - 4),
                (maxX, minY + 4),
                (maxX - 4, minY)
        ]
        drawByCoords(coords, colour)

        coords = [
                (minX + 4, minY + 3),
                (minX + 4, (minY + (height / 2)) - 3),
                (maxX - 7, (minY + (height / 2)) - 3),
                (maxX - 4, (minY + (height / 2)) - 6),
                (maxX - 4, minY + 6),
                (maxX - 7, minY + 4)
        ]
        drawByCoords(coords, colour)

def drawS(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, minY + (height / 2) + 2),
                (maxX - 4, minY + (height / 2) + 2),
                (maxX - 4, maxY - 4),
                (minX, maxY - 4),
                (minX, maxY),
                (maxX, maxY),
                (maxX, minY + (height / 2) - 2),
                (minX + 4, minY + (height / 2) - 2),
                (minX + 4, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawT(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, minY + 4),
                (minX + (width / 2) - 2, minY + 4),
                (minX + (width / 2) - 2, maxY),
                (minX + (width / 2) + 2, maxY),
                (minX + (width / 2) + 2, minY + 4),
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

def drawV(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),

                ((minX + (width / 2)) - 2, maxY),

                ((minX + (width / 2)) + 2, maxY),

                (maxX, minY),
                (maxX - 4, minY),
                (minX + (width / 2), maxY - 4),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawX(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                ((minX + (width / 2)) - 2, (height / 2)),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + (width / 2), (height / 2) + 2),
                (maxX - 4, maxY),
                (maxX, maxY),
                (minX + (width / 2) + 2, (height / 2)),
                (maxX, minY),
                (maxX - 4, minY),
                (minX + (width / 2), (height / 2) - 2),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawZ(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, minY + 4),
                (maxX - 4, minY + 4),
                (minX, maxY - 4),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - 4),
                (minX + 4, maxY - 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

letterMethods = {
        "A":drawA,
        "B":drawB,
        "C":drawC,
        "D":drawD,
        "E":drawE,
        "F":drawF,
        "G":drawG,
        "H":drawH,
        "I":drawI,
        "J":drawJ,
        "K":drawK,
        "L":drawL,
#        "M":drawM,
        "N":drawN,
        "O":drawO,
        "P":drawP,
#        "Q":drawQ,
        "R":drawR,
        "S":drawS,
        "T":drawT,
        "U":drawU,
        "V":drawV,
#        "W":drawW,
        "X":drawX,
#        "Y":drawY,
        "Z":drawZ
}

def drawWord(word):
        width = 15
        height = 31
        spacing = 2
        word_spacing = 10

        minX = 0
        minY = 0

        maxX = width
        maxY = height

        for letter in word:
                if letter != "":
                        if letterMethods[letter]:
                                letterMethods[letter](minX, minY, maxY, width, height, 1)

        # # Then scroll image across matrix...
        # for n in range(64 * 2, -((second_word_start + (width + spacing) * 2) + width), -1): # Start off top-left, move off bottom-right
        #         matrix.Clear()
        #         # IMPORTANT: *MUST* pass image ID, *NOT* image object!
        #         matrix.SetImage(image.im.id, n, 0)
        #         time.sleep(0.05)

        # matrix.Clear()

def drawWords(text):
        words = text.split(" ")
        spacing = 0
        for word in words:
                if word != "":
                        drawWord(word)


def drawFuckOff():
        width = 15
        height = 31
        spacing = 2
        word_spacing = 10

        minX = 0
        minY = 0

        maxX = width
        maxY = height

        # letterMethods["K"](minX, minY, maxY, width, height, "blue")
        letterMethods["R"](minX, minY, maxY, width, height, "blue")

        # letterMethods["F"](minX, minY, maxY, width, height, "blue")
        # letterMethods["U"](width + spacing, minY, maxY, width, height, "blue")
        # letterMethods["C"]((width + spacing) * 2, minY, maxY, width, height, "blue")
        # letterMethods["K"]((width + spacing) * 3, minY, maxY, width, height, "blue")

        second_word_start = (((width + spacing) * 3) + width) + word_spacing

        # letterMethods["O"](second_word_start, minY, maxY, width, height, "blue")
        # letterMethods["F"](second_word_start + width + spacing, minY, maxY, width, height, "blue")
        # letterMethods["F"](second_word_start + (width + spacing) * 2, minY, maxY, width, height, "blue")

        # drawF(minX, minY, maxY, width, height, "blue")
        # drawU(width + spacing, minY, maxY, width, height, "blue")
        # drawC((width + spacing) * 2, minY, maxY, width, height, "blue")
        # drawK((width + spacing) * 3, minY, maxY, width, height, "blue")

        

        # drawO(second_word_start, minY, maxY, width, height, "blue")
        # drawF(second_word_start + width + spacing, minY, maxY, width, height, "blue")
        # drawF(second_word_start + (width + spacing) * 2, minY, maxY, width, height, "blue")

        # Then scroll image across matrix...
        for n in range(64 * 2, -((second_word_start + (width + spacing) * 2) + width), -1): # Start off top-left, move off bottom-right
                matrix.Clear()
                # IMPORTANT: *MUST* pass image ID, *NOT* image object!
                matrix.SetImage(image.im.id, n, 0)
                time.sleep(0.05)

        matrix.Clear()

drawFuckOff()