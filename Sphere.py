import numpy

def normalize(vector):
    """
    Normalisiert einen Vektor
    :param vector: Vektor
    :return: Gibt normalisierten Vektor wieder
    """
    normal = numpy.linalg.norm(vector)

    if normal == 0:
        return vector

    return vector/normal

class Sphere(object):
    """
    Klasse die ein Objet in der 2d/3d-Welt darstellen soll
    """
    def __init__(self,center,radius,rgb):
        self.center = center
        self.radius = radius
        self.rgb = rgb

    def __repr__(self):
        return 'Sphere (%s,%s)' %(repr(self.center), self.radius)

    def intersectionParameter(self, ray):
        """
        Überprüft Schnittpunkt Objekt zum Lichtstrahl
        :param ray: Lichstrahl von der Kamera in die Szene
        :return: None wenn kein Schnittpunkt oder Schnittpunkt
        """
        co = self.center - ray.origin #Vektor Kreismittelpunkt zum Strahl
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


    