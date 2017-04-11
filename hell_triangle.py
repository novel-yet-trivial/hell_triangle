class InvalidTriangle(Exception):
    """Auxiliary class used to raise validation errors on triangles."""

    pass


class HellTriangle():
    """
        A class used to solve the 'Hell Triangle' problem.
        The problem is as follows:

        "Given a triangle of numbers, find the maximum total from top to bottom.
        Example:

           6
          3 5
         9 7 1
        4 6 8 4


        In this triangle the maximum total is 6 + 5 + 7 + 8 = 26.

        An element can only be summed with one of the two nearest
         elements in the next row, so the element 3 in row 2 can be
         summed with 9 and 7, but not with 1."
    """

    triangle = []

    def set_triangle(self, triangle):
        """
            Function to set the 'triangle' attribute of the class
             and validate it.
        """

        self.triangle = triangle
        self.validate_triangle()


    def validate_triangle(self):
        """
            Function to validate the triangle.
            It checks for five things:
            1 - If the triangle is an instance of 'list'.
            2 - If the triangle is not empty.
            3 - If all the elements of the triangle are also instances of 'list'.
            4 - If all the elements of all lines are instances of 'int' or 'float'.
            5 - If every line of the triangle is one unity bigger than the last one.

            If any of the conditions fails, an 'InvalidTriangle' exception is raised.
        """

        if not isinstance(self.triangle, list):
            raise InvalidTriangle("Triangle must be an instance of 'list'.")

        if not self.triangle:
            raise InvalidTriangle("Triangle is empty or was not set.")

        if not all([isinstance(line, list) for line in self.triangle]):
            raise InvalidTriangle(
                "All elements of the triangle must be an instance of 'list'."
            )

        past_line_size = None
        for i, line in enumerate(self.triangle):
            line_size = len(line)

            for element in line:
                if not (isinstance(element, int) or isinstance(element, float)):
                    raise InvalidTriangle(
                        "All elements of all lines must be an instance of 'int' or 'float'."
                    )

            if past_line_size is not None:
                if line_size != past_line_size + 1:
                    raise InvalidTriangle(
                        "Invalid line size, was expecting size %d, got size %d on line %d."
                        % (past_line_size+1, line_size, i)
                    )

            past_line_size = line_size


    def find_maximum_value_possible(self):
        """
            The main function that does the calculation.
            It does that by replacing every line, except the last one, with
             the contents of the line, plus the biggest element from the
             possible elements in the line below.
            At the end of the process, the value in the first line will be
             the solution of the problem.

            For example, lets assume we have the following triangle I:

                  06
                03  05
              09  07  01
            04  06  08  04



            At the end of the first loop, we will have the new triangle II:

                  06
                03  05
              15  15  09
            04  06  08  04



            If we ignore the last line of the Triangle II, the two triangles
             have the same information to solve this problem.

            Continuing with the process, we will then have the Triangle III:

                  06
                18  20
              15  15  09
            04  06  08  04



            And the triangle IV:

                  26
                18  20
              15  15  09
            04  06  08  04



            After that, the program will exit the loops and the
             element in the postion (0, 0) of the triangle will
             be the solution of our problem.
        """

        for current_line in range(-2, (len(self.triangle)+1)*-1, -1):
            for x in range(len(self.triangle[current_line])):
                left_value = self.triangle[current_line + 1][x]
                right_value = self.triangle[current_line + 1][x + 1]
                bigger_value = max(left_value, right_value)
                self.triangle[current_line][x] += bigger_value

        return self.triangle[0][0]
