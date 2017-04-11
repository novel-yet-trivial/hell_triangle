# Hell Triangle
A project to solve the "Hell Triangle" problem.


# Description
Given a triangle of numbers, find the maximum total from top to bottom.

Example:

       6
      3 5
     9 7 1
    4 6 8 4


In this triangle the maximum total is 6 + 5 + 7 + 8 = 26.

An element can only be summed with one of the two nearest elements in the next row, so the element 3 in row 2 can be summed with 9 and 7, but not with 1.


# Usage
The program was made using python and was tested using versions 2.7.12, 3.5.2 and 3.6.1.
You can run the program by instantiating the 'HellTriangle' class found in hell_triangle.py as follows:

    from hell_triangle import HellTriangle
    ht = HellTriangle()

After that, you can pass a list of numbers (int or floats) to the class, the structure must be a list, and each line of the triangle must also be a list.
To pass the triangle found in the description:

    triangle = [[6], [3,5], [9,7,1], [4,6,8,4]]
    ht.set_triangle(triangle)

When calling the 'set_triangle' function, a subsequent call to the 'validate_triangle' function will be made.
During the validation, if the triangle has anything wrong, the 'InvalidTriangle' exception will be raised.
After setting the triangle, you can get the result by calling the 'find_maximum_value_possible' function, as follows:

    ht.find_maximum_value_possible()

# Test Cases

A number of tests cases can be found in the 'hell_triangle_tests' file.
To run the tests, simple run `./hell_triangle_tests.py` from the terminal.
