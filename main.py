from PIL import Image
import math

def distance_halo(image_name, targetX, targetY, modifyer):
    image = Image.open(image_name)

    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            red = pixels[x,y][0]
            blue = pixels[x,y][1]
            green = pixels[x,y][2]
            #calculates distane and therfore color for each color
            darkness_mod =  int(math.sqrt( (targetX - x)**2 + (targetY - y)**2 ) / modifyer)
            pixels[x,y] = (red - darkness_mod, blue - darkness_mod, green - darkness_mod)

    image.save(image_name[:-4] + "_distance_halo.png")

distance_halo("statue.png", 150, 150, 3)

