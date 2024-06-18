#Neal Aicinena CPSC 230-03
from cmath import pi

#asks the user to input a radius value and stores it as radius
radius = float(input("enter a radius: "))

#computes the area and volume of a sphere given the users inputed radius
area = 4 * pi * (radius ** 2)
volume = (4 / 3) * pi * (radius ** 3)

#prints to the user the area and volume of the sphere
print("the area of a sphere with that radius is", area, "units squared")
print("the volume of a sphere with that radius is:", volume, "units cubed")