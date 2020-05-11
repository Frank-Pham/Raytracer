import numpy

class CheckerboardMaterial(object):
    """Klasse für ein Schachbrettmuster-Material"""
    def __init__(self, a, b, c):
        self.baseColor = (255, 255, 255)
        self.otherColor = (0,0,0)
        self.ambientCoefficient = 0.6
        self.specularCoefficient = 0.2
        self.checkSize = 1


    def baseColorAt(self,p):
        v = numpy.array(p)
        v = v*(1.0 / self.checkSize)
        x = v[0]
        y = v[1]
        z = v[2]

        if (int(abs(x) + 0.5) + int(abs(y) + 0.5) + int(abs(z) +0.5)) %2:
            return self.otherColor
        return self.baseColor