# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.

from collections import defaultdict
def palindrome_hash(string):
    # A palindrome can be made from any string which has an even number of each character unless the string is an odd number of letters in which case one letter may be unique.
    letter_count = defaultdict(int)

    for char in string:
        letter_count[char] += 1

    # Boolean to check if a unique letter is allowed.
    unique_allowed = False if not len(string) % 2 else True

    for char_count in letter_count.values():
        if char_count % 2:
            if unique_allowed:
                unique_allowed = False
            else:
                return False
    return True

import unittest
import string
import random
class Test(unittest.TestCase):
    max_string_length = 10
    min_string_length = 5
    def create_palindrome(self):
        # create a string which is a permutation of a palindrome.

        string_length = random.randint(self.min_string_length, self.max_string_length)
        test_string = ''
        for _ in range(int(string_length/2)):
            test_string = ''.join([test_string] +  ([random.choice(string.ascii_letters)] * 2))

        if string_length % 2:
            test_string = ''.join([test_string, random.choice(string.ascii_letters)])
        return test_string

    def create_not_palindrome(self):
        test_string = ''.join(random.choices(string.ascii_letters, k=random.randint(self.min_string_length, self.max_string_length)))

        # Replace two indexes with two different characters which cannot be found in original string
        for index, char in zip(random.sample(range(len(test_string)), 2), ['%', '$']):
            test_string = test_string[:index] + char + test_string[index + 1:]
        return test_string

    def palindrome_check_test(self):
        self.assertTrue(palindrome_hash(self.create_palindrome()))
        self.assertFalse(palindrome_hash(self.create_not_palindrome()))

    number_of_tests = 1000
    def test(self):
        for _ in range(self.number_of_tests):
            self.palindrome_check_test()
