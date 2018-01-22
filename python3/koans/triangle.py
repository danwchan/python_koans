#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py

def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    # pass
    triangle = [a, b, c]
    try:
        if min(triangle) <= 0:
            raise TriangleError("one or more sides are equal to or less than zero")
        elif sum(sorted(triangle)[:2]) <= max(triangle):
            raise TriangleError("any of the two sides are not equal to the other")
        else:
            pass
    except TriangleError as ex:
            raise ex
    else:
        trimetric = len(set(triangle))
        if  trimetric == 1:
            return "equilateral"
        elif trimetric == 2:
            return "isosceles"
        else:
            return "scalene"

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
