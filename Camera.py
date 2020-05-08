import numpy
from Ray import Ray

class Camera(object):

    def __init__(self, e, c, up):
        self.e = e
        self.c = c
        self.up = up

        #TODO Normalisieren
        self.f = (c - e)/numpy.linalg.norm((c - e))
        self.s = self.f.cross(up)/numpy.linalg.norm(self.f.cross(up))
        self.u = self.s.cross(self.f)

    def calc_Settings(self,imageWidth,imageHeight):
        aspectRatio = imageWidth / imageHeight

        fieldOfView = 45
        alpha = fieldOfView / 2
        height = 2* numpy.tan(alpha)
        width = aspectRatio * height

        pixelWidth = width / (imageWidth - 1)
        pixelHeight = height / (imageHeight - 1)

        for y in range(imageHeight):
            for x in range(imageWidth):
                xcomp = self.s.scale(x * pixelWidth - width / 2)
                ycomp = self.u.scale(y * pixelHeight - height / 2)
                ray = Ray(self.e, self.f + xcomp + ycomp)



