# write a program to findout which triangle is bigger from 2 triangle. accept base and height from user. 
# Area= 0.5 * base * height
'''
steps
1)take iputs from user for triangle1
    height1=height of triangel1
    base1=base of triangle1
2)find area of triangle 1
    Area1=0.5 * base1 * height1
3)take input from user for triangle2
    height2=height of triangel2
    base2=base of triangle2
4)find area of triangle 2
    Area2=0.5 * base2 * height2
5)compare area of both triangle
if Area1>Area2:
    print("triangle1 is bigger than triangle2")
else:
    print("triangle2 is bigger than triangle1")
'''

height1=float(input("heaight of triangle 1:"))
base1=float(input("base of triangle1:"))

aria_triangle1=0.5 * base1 * height1
print("Area of triangle1:",aria_triangle1)

height2=float(input("heaight of triangle 1:"))
base2=float(input("base of triangle1:"))

aria_triangle2=0.5 * base2 * height2
print("Area of triangle2:",aria_triangle2)

if aria_triangle1>aria_triangle2:
    print("triangle1 is bigger")
else:
    print("triangle2 is bigger")