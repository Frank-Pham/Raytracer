import numpy
from Ray import Ray

class Camera(object):

    def __init__(self, e, c, up, fov):
        self.e = e
        self.c = c
        self.up = up
        self.fov = fov

        #TODO Normalisieren
        self.f = (c - e)/(numpy.linalg.norm(c - e))
        self.s = numpy.cross(self.f,up) / (numpy.linalg.norm(numpy.cross(self.f , up)))
        self.u = numpy.cross(self.s,self.f)


    def setup_CamerView(self,imageWidth,imageHeight):
        self.aspectRatio = imageWidth / imageHeight
        self.alpha = self.fov / 2
        self.height = 2 * numpy.tan(self.alpha)
        self.width = self.aspectRatio * self.height

        self.pixelWidth = self.width / (imageWidth - 1)
        self.pixelHeight = self.height / (imageHeight - 1)

    def calc_CameraRay(self,x,y):

        xcomp = self.s * (x * self.pixelWidth - self.width / 2)
        ycomp = self.u * (y * self.pixelHeight - self.height / 2)
        return Ray(self.e, self.f + xcomp + ycomp)




