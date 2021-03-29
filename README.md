# Raytracer

Raytracer for a Computer Graphics class. Implemented with a backwards raytracing algorithm 
and the phong lighting model.

## How to use?

There are these given methods in main():

**1.) render_Squirrel()\
2.) process_Render()\
3.) thread_Render()\
4.) ray_Casting(camera)**

Execute one of the methods to either render 1.) the Squirrel, with 2.) Processing, 
with 3.) Threading or the base scene with 4.) three spheres, a triangle and checkered floor.
Don't forget to comment out the other methods while you use one of these methods.

Render times:\
400x400px Sphere,Triangle,Floor Scene: \
normal:54,205 seconds\
Threading/Processing: ~220 seconds

200x 200px Squirrel:\
Normal without reflections: 48 minutes

![png](https://github.com/Frank-Pham/Raytracer/blob/master/Reflection_Spheres.png)

