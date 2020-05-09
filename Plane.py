import numpy

def normalize(vector):
    normal = numpy.linalg.norm(vector)

    if normal == 0:
        return vector

    return vector/normal

class Plane(object):

    def __init__(self, point, normal, rgb):
        self.point = point
        self.normal = normalize(normal)
        self.rgb = rgb

    def __repr__(self):
        return 'Plane(%s,%s)' %(repr(self.point), repr(self.normal))

    def intersectionParameter(self, ray):
        op = ray.origin - self.point
        a = numpy.dot(op,self.normal)
        b = numpy.dot(ray.direction,self.normal)

        if b:
            return -a/b
        else:
            return None

    def normalAt(self, p):
        return self.normal

    def colorAt(self, ray):
        return tuple(x+int(ray) for x in self.rgb)
        """return self.rgb"""
