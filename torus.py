#!/usr/bin/env python

# ME499-S20 Python Lab 0 Problem 3
# Programmer: Jacob Gray
# Last Edit: 4/1/2020

from math import pi  # Import pi from math library

ir = 3  # Inner radius of torus from CG
oor = 4  # Outer radius of torus from CG

r = (oor - ir) / 2  # Radius of circular cross section of torus
h = 2 * pi * (ir + r)  # Length of effective cross sectional area

print((pi * r ** 2) * h)  # Print volume of torus
