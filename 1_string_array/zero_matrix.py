# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row is set to O.

def zero_matrix_loop(matrix):
    # search for zero
    for j in range(len(matrix)):
        for i in matrix[j]:
            if i == 0:
                matrix[j] = [0 for _ in matrix[j]]
                break
    return matrix

import unittest
class TestRow(unittest.TestCase):
    matrix_height = 10
    matrix_width = 5
    def create_matrix(self):
        import random

        matrix = []
        result_matrix = []

        for _ in range(self.matrix_height):
            row = random.sample(range(1, 100), self.matrix_width)
            matrix.append(row)
            # Decide if normal line or a line with a zero.
            decide_zero = random.randint(0,1)
            if decide_zero:
                matrix[-1][random.randint(0, self.matrix_width - 1)] = 0
                result_matrix.append([0] * self.matrix_width)
            else:
                result_matrix.append(row)
        return matrix, result_matrix

    number_of_tests = 10000
    def test(self):
        for _ in range(self.number_of_tests):
            input_matrix, output_matrix = self.create_matrix()
            self.assertEqual(zero_matrix_loop(input_matrix), output_matrix)

# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.

def zero_matrix_row_column(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            if matrix[j][i] == 0:
                for h in range(len(matrix)):
                    if h != j:
                        matrix[h][i] = None

    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            if matrix[j][i] == 0:
                matrix[j] = [None for _ in range(len(matrix[j]))]
                    
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            if matrix[j][i] == None:
                matrix[j][i] = 0
    return matrix

class TestRowColumn(unittest.TestCase):
    matrix_height = 10
    matrix_width = 5

    def create_matrix(self):
        import random

        matrix = []

        # Decide which rows and columns will be zeros.
        rows = {}
        columns = {}

        most_zeros_allowed = self.matrix_width if self.matrix_width < self.matrix_height else self.matrix_height
        amount_to_be_zero = random.randint(1, most_zeros_allowed - 1)

        for _ in range(amount_to_be_zero):
            row = random.randint(0, self.matrix_height - 1)
            column = random.randint(0, self.matrix_width - 1)

            while row in rows or column in columns:
                row = random.randint(0, self.matrix_height - 1)
                column = random.randint(0, self.matrix_width - 1)

            rows[row] = True
            columns[column] = True

        # Create matrix
        for _ in range(self.matrix_height):
            matrix.append(random.sample(range(1, 100), self.matrix_width))

        for j,i in zip(rows.keys(), columns.keys()):
            matrix[j][i] = 0

        result_matrix = [row[:] for row in matrix]
        
        for row in rows.keys():
            for column in range(len(result_matrix[0])):
                result_matrix[row][column] = 0

        for column in columns.keys():
            for row in range(len(result_matrix)):
                result_matrix[row][column] = 0

        return matrix, result_matrix

    number_of_tests = 1000000
    def test(self):
        for _ in range(self.number_of_tests):
            matrix, result_matrix = self.create_matrix()
            self.assertEqual(zero_matrix_row_column(matrix), result_matrix)
