class Vector:
    """Klasse die Vektoren darstellen soll.(Ortsvektor als standard gesetzt)"""
    def __init__(self,x = 0.0 ,y = 0.0, z= 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """

        :param other:
        :return:
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y + other.y, self.z + other.z)

    def __truediv__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x / other , self.y / other , self.z / other)


    def __mul__(self, other):
        """
        Methode zum Multiplizieren von Vektoren mit Zahlen oder das berechnen des Skalarprodukts
        :param other: Entwerder Vektor oder Zahl
        :return: Das Skalarprodukt oder ein neuer Vektor
        """
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z + other.z

        elif isinstance(other, int):
            return Vector(self.x * other, self.y * other, self.z * other)

        elif isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)

        else:
            assert "Typfehler: Vektoren können nur mit Zahlen oder Vektoren multipliziert werden"

    def __rmul__(self, other):
        return self.__mul__(other)


    def vector_length(self):
        return math.sqrt((self.x**2+self.y**2+self.z**2))

    def kreuzprodukt(self,other):
        return Vector(self.y * other. z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def normalize(self):
        return self / self.vector_length()

    def __repr__(self):
        return f"X: {self.x} | Y: {self.y} | Z: {self.z}"