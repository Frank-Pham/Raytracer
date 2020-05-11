from Ray import Ray
from Vector import Vector
from Sphere import Sphere
from Triangle import Triangle
from Plane import Plane
from Camera import Camera
from Light import Light
from Checkerboard import CheckerboardMaterial
import numpy
import threading
import multiprocessing
import time
import math
from PIL import Image

IMAGE_WIDTH = 300
IMAGE_HEIGHT = 300
BACKGROUND_COLOR = (0,0,0)
CHECKERBOARD = CheckerboardMaterial(0,0,0)

image = Image.new('RGB', (IMAGE_WIDTH,IMAGE_HEIGHT))

"""Kamera-Settings"""
e = numpy.array([0,1.8,10])
c = numpy.array([0,1,0])
up = numpy.array([0,-1,0])
fieldOfView = 45

"""UP Vektor in Minusbereich dreht das Eichhörnchen"""
camera = Camera(e,c,up,fieldOfView)


redSphere = Sphere(numpy.array([2.5,6.5,-10]),2.1,(250,0,0))
greenSphere = Sphere(numpy.array([-2.5,6.5,-10]),2.1,(0,250,0))
blueSphere = Sphere(numpy.array([0,2,-10]),2.1,(0,0,250))
triangle = Triangle(numpy.array([2.5,6.5,-10]), numpy.array([-2.5, 6.5, -10]), numpy.array([0,2,-10]),(255,255,0))
plane = Plane(numpy.array([0, 10, 0]), numpy.array([0, -10, -2]),CHECKERBOARD)

objectlist = [redSphere, greenSphere, blueSphere,triangle, plane]
light = Light(numpy.array([-40,-40,10]),(255,255,255))

maxlevel = 1
shadow_ambient = 0.1
no_shadow_ambient = 0.5
diffusion = 0.5
specular = 0.5
exp_shiny = 10
reflection = 0.2

def normalize(vector):
    normal = numpy.linalg.norm(vector)

    if normal == 0:
        return vector
    return vector/normal


def trace_Ray(level, ray):
    hitPointData = intersect(level, ray, maxlevel)

    if hitPointData is not None and level <= maxlevel:
        return shade(level, hitPointData)

    return BACKGROUND_COLOR


def shade(level, hitPointData):
    directColor = compute_DirectLight(hitPointData)
    reflectedRay = computeReflectedRay(hitPointData)
    reflectedColor = trace_Ray(level+1, reflectedRay)

    return directColor + reflection * numpy.array(reflectedColor)


def compute_DirectLight(hitPointData):
    color = BACKGROUND_COLOR
    current_obj = hitPointData[0]
    if hitPointData[0] and current_obj is not None:
        intersec_Point = hitPointData[1]
        intersec_Light = Ray(intersec_Point, normalize(light.position - intersec_Point))
        in_shadow = check_Shadow(current_obj,intersec_Light)
        if in_shadow == True:
            """color = numpy.array(hitPointData[0].rgb) * shadow_ambient"""
            color = phong_Shader(intersec_Point,hitPointData,shadow_ambient)
        else:
            color = phong_Shader(intersec_Point, hitPointData, no_shadow_ambient)

    return color


def computeReflectedRay(hitPointData):
    obj = hitPointData[0]
    intersec_Point = hitPointData[1]
    ray_Vector = hitPointData[3]

    n_Vec = normalize(obj.normalAt(intersec_Point))
    il_refl = normalize(ray_Vector.direction - 2* numpy.dot(ray_Vector.direction,n_Vec)*n_Vec)
    reflected_Ray = Ray(intersec_Point, il_refl)

    return reflected_Ray


def check_Shadow(current_obj,intersecLight):

    for obj in objectlist:
        if obj is not None and obj is not current_obj:
            check_Obj = obj.intersectionParameter(intersecLight)

            if check_Obj is not None and check_Obj > 0:
                return True
    return False


def phong_Shader(intersec_Point,hitPointData, ambient):

    obj = hitPointData[0]

    if isinstance(obj,Plane):
        obj_color = numpy.array(obj.rgb.baseColorAt(intersec_Point))

    else:
        obj_color = numpy.array(obj.rgb)

    light_material = numpy.array(light.rgb) #Lichtfarbe in Numpyarray umwandeln zum rechnen

    i_to_l = normalize(light.position - intersec_Point) # Schnittpunkt der Kugel zum Licht
    n_Vec = normalize(obj.normalAt(intersec_Point))
    il_refl = i_to_l - (2* abs(numpy.dot(n_Vec,i_to_l))*n_Vec) #Einfallswinkel = Ausfallswinkel - i_to_l reflektierender Vektor
    d = normalize(intersec_Point - camera.e)

    color_out = obj_color * ambient + light_material * diffusion * numpy.dot(i_to_l,n_Vec)+ light_material * specular * (numpy.dot(il_refl, -d)**exp_shiny)
    return color_out



def ray_Casting(camera):

    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            ray = camera.calc_CameraRay(x,y)
            color = trace_Ray(0, ray)
            color_tuple = (int(color[0]),int(color[1]),int(color[2]))

            image.putpixel((x,y), color_tuple)


def intersect(level,ray,maxlevel):
    maxdist = float('inf')
    hitObj = None
    for object in objectlist:
        hitdist = object.intersectionParameter(ray)

        if hitdist and hitdist < maxdist and hitdist > 0:
            maxdist = hitdist
            hitObj = (object, ray.pointAtParameter(maxdist), maxdist,ray)
    return hitObj

def render_Squirrel():
    global objectlist

    tri_Array = []
    tri_Points = []

    with open("squirrel_aligned_lowres.obj") as squirrel_Data:

        for line in squirrel_Data:
            data = line.split()

            if data[0] == 'v':
                tri_Points.append(numpy.array([float(data[1]), float(data[2]), float(data[3])]))

            elif data[0] == 'f':
                triangle1 = Triangle(tri_Points[int(data[1])-1],tri_Points[int(data[2])-1],tri_Points[int(data[3])-1], (160,160,160))
                tri_Array.append(triangle1)

    objectlist = tri_Array

def process_Render():
    """
    Multiprocessing Methode: Dauert deutlich länger. (Wegen dem starten der einzelnen Prozesse?)
    :return:
    """
    multiprocess = []

    for counter in range(4):
        p = multiprocessing.Process(target=ray_Casting(camera))
        p.start()
        multiprocess.append(p)

    for process in multiprocess:
        process.join()

def thread_Render():
    threads_list = []

    for counter in range(4):
        t = threading.Thread(target = ray_Casting(camera))
        t.start()
        threads_list.append(t)

    for thread in threads_list:
        thread.join()

def main():
    start_timer = time.perf_counter()
    camera.setup_CamerView(IMAGE_WIDTH,IMAGE_HEIGHT)

    render_Squirrel()
    #process_Render()
    #thread_Render()
    ray_Casting(camera)

    finish_timer = time.perf_counter()
    image.show()
    #image.save("Reflection_Spheres.png")
    image.save("Squirrel.png")
    print(f'Renderzeit: {round(finish_timer - start_timer, 3)} Sekunden')



if __name__ == '__main__':
    main()

