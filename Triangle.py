import numpy

def normalize(vector):
    normal = numpy.linalg.norm(vector)

    if normal == 0:
        return vector

    return vector/normal

class Triangle(object):
    def __init__(self, a, b, c, rgb):
        self.a = a
        self.b = b
        self.c = c
        self.u = self. b - self.a
        self.v = self.c - self.a
        self.rgb = rgb

    def __repr__(self):
        return 'Triangle(%s,%s,%s)' %(repr(self.a), repr(self.b), repr(self.c))

    def intersectionParameter(self, ray):
        w = ray.origin - self.a
        dv = numpy.cross(ray.direction,self.v)
        dvu = numpy.dot(dv,self.u)

        if dvu == 0.0:
            return None
        wu = numpy.cross(w,self.u)
        r = numpy.dot(dv,w) / dvu
        s = numpy.dot(wu,ray.direction) / dvu

        if 0 <= r and r <= 1 and 0 <= s and s <= 1 and r+s <= 1:
            return numpy.dot(wu,self.v) / dvu
        else:
            return None

    def normalAt(self,p):
        """return self.u.cross(self.v).normalized()"""
        return normalize(numpy.cross(self.u,self.v))

    def colorAt(self,ray):
        return self.rgb
