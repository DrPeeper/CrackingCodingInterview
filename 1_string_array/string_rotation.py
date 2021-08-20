# String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one call to isSubstring (e.g., waterbottle is a rotation ofu erbottlewat).

# A rotation is splitting a word into two different parts and rearanging it. For example, waterbottle can be split into x = wat and y = erbottle and rearanged into yx (erbottlewat).

# A rotation, yx, will always be a substring of xyxy.

def is_rotation(s1, s2):
    return s2 in s1 + s1

import unittest
import random
import string
class Test(unittest.TestCase):
    def create_rotation(self, s):
        rotation_point = random.randint(1, len(s) - 1)
        return s[rotation_point:] + s[:rotation_point]

    def create_non_rotation(self, s):
        insertion_point = random.randint(0, len(s) - 1)
        return s[:insertion_point] + '$' + s[insertion_point + 1:]

    string_length = 10
    def rotation_test(self):
        s = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=self.string_length))

        self.assertTrue(is_rotation(s, self.create_rotation(s)))
        self.assertFalse(is_rotation(s, self.create_non_rotation(s)))

    number_of_tests = 100
    def tests(self):
        for _ in range(self.number_of_tests):
            self.rotation_test()
