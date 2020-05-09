from Ray import Ray
from Vector import Vector
from Sphere import Sphere
from Triangle import Triangle
from Plane import Plane
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

redSphere = Sphere(numpy.array([2.5,6.5,-10]),2.1,(250,0,0))
greenSphere = Sphere(numpy.array([-2.5,6.5,-10]),2.1,(0,250,0))
blueSphere = Sphere(numpy.array([0,2,-10]),2.1,(0,0,250))
triangle = Triangle(numpy.array([2.5,6.5,-10]), numpy.array([-2.5, 6.5, -10]), numpy.array([0,2,-10]),(255,255,0))
plane = Plane(numpy.array([0, 10, 0]), numpy.array([0, -10, -3]),(170,170,170))

objectlist = [redSphere, greenSphere, blueSphere,triangle, plane]
light = numpy.array([30,30,10])
def phong_Shader():
    ambient = 0.2
    specular = 0.5

def trace_Ray(level, ray):
    hitPointData = intersect(level, ray, maxlevel)

    if hitPointData:
        return shade(level, hitPointData)

    return BACKGROUND_COLOR

def shade(level, hitPointData):
    directColor = computeDirectLight(hitPointData)

    reflectedRay = computeReflectedRay(hitPointData)
    reflectedColor = traceRay(level+1, reflectedRay)

    return directColor + reflection * reflectedColor

def ray_Casting(camera):

    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            ray = camera.calc_CameraRay(x,y)
            maxdist = float('inf')
            color = BACKGROUND_COLOR
            for object in objectlist:
                hitdist = object.intersectionParameter(ray)

                if hitdist and hitdist < maxdist and hitdist > 0:
                    maxdist = hitdist
                    """color = object.colorAt(ray)"""
                    color = object.colorAt(hitdist)
            image.putpixel((x,y), color)


def main():
    v1 = Vector(1, 2, 3)
    v2 = Vector(-2, 1, -3)
    v3 = v1.kreuzprodukt(v2)
    print(v1 * 2)

    e = numpy.array([0,1.8,10])
    c = numpy.array([0,3,0])
    up = numpy.array([0,1,0])
    fieldOfView = 45

    camera = Camera(e,c,up,fieldOfView)
    camera.setup_CamerView(IMAGE_WIDTH,IMAGE_HEIGHT)
    ray_Casting(camera)
    image.show()

if __name__ == '__main__':
    main()

