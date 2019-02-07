# sphere.py
# calculate the volume and surface area of a sphere

import math
from decimal import Decimal

def main():
    # V = (4/3)(pi)(r)^3
    # A = (4)(pi)(r)^2
    radius = float(input("What is the radius of the sphere? "))
    volume = 4/3 * math.pi * radius ** 3
    area = 4 * math.pi * radius ** 2
    print()
    print("The volume of the sphere is", volume)
    print("The surface of the sphere is", area)

main()
