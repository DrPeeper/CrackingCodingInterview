# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_loop(image):
    rotated_image = []
    x = len(image[0]) - 1
    while x >= 0:
        new_row = []
        for y in range(len(image)):
            new_row.append(image[y][x])
        rotated_image.append(new_row)
        x -= 1
    return rotated_image

def rotate_str_comprehension(image):
    return [[image[j][i] for j in range(len(image))] for i in range(len(image) - 1, -1, -1)]

import unittest
class Test(unittest.TestCase):
    def test(self):
        img_test = [[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12],
                     [13,14,15,16]]

        img_result = [[4, 8, 12, 16],
                      [3, 7, 11, 15],
                      [2, 6, 10, 14],
                      [1, 5, 9, 13]]

        self.assertEqual(rotate_loop(img_test), img_result)
        self.assertEqual(rotate_str_comprehension(img_test), img_result)
