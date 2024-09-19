from PIL import ImageDraw
from PIL import Image
import math
import random

def distance_halo(image_name, targetX, targetY, modifyer):
    image = Image.open(image_name)

    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            red = pixels[x,y][0]
            blue = pixels[x,y][1]
            green = pixels[x,y][2]
            #calculates distane and therfore color for each color
            darkness_mod =  int((math.sqrt((targetX - x)**2 + (targetY - y)**2 )) / modifyer)
            pixels[x,y] = (red - darkness_mod, blue - darkness_mod, green - darkness_mod)

    image.save(image_name[:-4] + "_distance_halo.png")





def pointillism(image_name):
    image = Image.open(image_name)

    pixels = image.load()
    canvas = Image.new("RGB",(image.size[0],image.size[1]), "white")

    for i in range(120000):
            #random pixels and color
            x = random.randint(1, image.width-1)
            y = random.randint(1, image.height-1)
            red = pixels[x,y][0]
            blue = pixels[x,y][1]
            green = pixels[x,y][2]

            #draws circles
            size = random.randint(5,8)
            ellipsebox=[(x,y),(x+size,y+size)]
            draw = ImageDraw.Draw(canvas)
            draw.ellipse(ellipsebox,fill=(pixels[x,y][0],pixels[x,y][1],pixels[x,y][2]))
            del draw


    canvas.save(image_name[:-4] + "pointillism.png")

pointillism("statue.png")

