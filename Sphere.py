import numpy

def normalize(vector):
    normal = numpy.linalg.norm(vector)

    if normal == 0:
        return vector

    return vector/normal

class Sphere(object):

    def __init__(self,center,radius,rgb):
        self.center = center
        self.radius = radius
        self.rgb = rgb

    def __repr__(self):
        return 'Sphere (%s,%s)' %(repr(self.center), self.radius)

    def intersectionParameter(self, ray):
        co = self.center - ray.origin
        v = numpy.dot(co,ray.direction)
        discriminant = v*v - numpy.dot(co,co) + self.radius * self.radius

        if discriminant < 0:
            return None

        else:
            return v - numpy.sqrt(discriminant)


    def normalAt(self, p):
        return normalize(p - self.center)

    def colorAt(self,ray):
        return self.rgb


    