import numpy

def normalize(vector):
    normal = numpy.linalg.norm(vector)

    if normal == 0:
        return vector

    return vector/normal


class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = normalize(direction)

    def __repr__(self):
        return 'Ray(%s,%s' %(repr(self.origin), repr(self.direction))

    def pointAtParameter(self, t):
        return self.origin + self.direction.scale(t)

    def normalized(self):
        #TODO
        pass
