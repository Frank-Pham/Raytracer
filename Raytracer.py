from Ray import Ray
from Vector import Vector
from Sphere import Sphere
from Camera import Camera
import numpy
import threading
import time
import math
from PIL import Image

IMAGE_WIDTH = 400
IMAGE_HEIGHT = 400
BACKGROUND_COLOR = (0,0,0)

image = Image.new('RGB', (IMAGE_WIDTH,IMAGE_HEIGHT))

def ray_Casting():
    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            ray = calcRay(x, y)
            maxdist = float('inf')
            color = BACKGROUND_COLOR
            for object in objectlist:
                hitdist = object.intersectionParameter(ray)

            if hitdist < maxdist:
                maxdist = hitdist
                color = object.colorAt(ray)
        image.putpixel((x,y), color)


def main():
    v1 = Vector(1, 2, 3)
    v2 = Vector(-2, 1, -3)
    v3 = v1.kreuzprodukt(v2)
    print(v1 * 2)

if __name__ == '__main__':
    main()

