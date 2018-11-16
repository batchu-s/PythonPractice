# Printing the area of the circle given the radius at user prompt.
from math import pi
radius = float(input("Enter the radius of the circle:"))
area = pi * (radius**2)
print("The Area of the circle is:" + str(round(area, 2)))