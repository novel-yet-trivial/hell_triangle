#!/usr/bin/env python

from unittest import TestCase, main as unittest_main
from hell_triangle import InvalidTriangle, HellTriangle


class HellTriangleTests(TestCase):
    """
        Class used to test several situations that can occur when
         using the "HellTriangle" class.

        The names of the functions should be self-explanatory
         about what is being tested.
    """

    @classmethod
    def setUpClass(self):
        self.ht = HellTriangle()


    def test_validation_with_an_empty_triangle(self):
        with self.assertRaises(InvalidTriangle) as context_manager:
            self.ht.set_triangle([])

        ex = context_manager.exception
        self.assertEqual(str(ex), "Triangle is empty or was not set.")


    def test_validation_with_string_instead_of_list(self):
        with self.assertRaises(InvalidTriangle) as context_manager:
            self.ht.set_triangle("Invalid")

        ex = context_manager.exception
        self.assertEqual(str(ex), "Triangle must be an instance of 'list'.")


    def test_validation_with_string_in_some_lines(self):
        with self.assertRaises(InvalidTriangle) as context_manager:
            triangle = [
                [2],
              [3, 4],
             "Invalid",
            ]
            self.ht.set_triangle(triangle)

        ex = context_manager.exception
        self.assertEqual(
            str(ex),
            "All elements of the triangle must be an instance of 'list'."
        )


    def test_validation_with_string_in_some_elements(self):
        with self.assertRaises(InvalidTriangle) as context_manager:
            triangle = [
                [2],
              [3, "4"],
            ]
            self.ht.set_triangle(triangle)

        ex = context_manager.exception
        self.assertEqual(
            str(ex),
            "All elements of all lines must be an instance of 'int' or 'float'."
        )


    def test_validation_with_invalid_triangle_structure(self):
        with self.assertRaises(InvalidTriangle) as context_manager:
            triangle = [
                [2],
              [3, 4],
              [5, 6],
            ]
            self.ht.set_triangle(triangle)

        ex = context_manager.exception
        self.assertEqual(
            str(ex),
            'Invalid line size, was expecting size 3, got size 2 on line 2.'
        )


    def test_result_with_only_one_line(self):
        triangle = [
          [2],
        ]
        self.ht.set_triangle(triangle)

        result = self.ht.find_maximum_value_possible()
        self.assertEqual(result, 2)


    def test_result_with_sample_triangle(self):
        triangle = [
             [6],
            [3,5],
           [9,7,1],
          [4,6,8,4],
        ]
        self.ht.set_triangle(triangle)

        result = self.ht.find_maximum_value_possible()
        self.assertEqual(result, 26)


if __name__ == "__main__":
    unittest_main(verbosity=2)
