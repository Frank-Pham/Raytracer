import numpy
import threading
import time
import math
class Vector:
    """Klasse die Vektoren darstellen soll.(Ortsvektor als standard gesetzt)"""
    def __init__(self,x = 0.0 ,y = 0.0, z= 0.0):
        self.x = x
        self.y = y
        self.z = z

    def vector_length(self):
        return math.sqrt((self.x**2+self.y**2+self.z**2))

    def kreuzprodukt(self,other):
        return self.x * other.x + self.y * other.y + self.z + other.z

    def __repr__(self):
        return f"X: {self.x} | Y: {self.y} | Z: {self.z}"

v1 = Vector(1,-2,-2)
v2 = Vector(2,-1,-2)

print(v1.kreuzprodukt(v2))