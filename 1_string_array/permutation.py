# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation_sort(string1, string2):
    # O(nlogn) because the strings are sorted.
    if len(string1) != len(string2):
        return False

    string1 = sorted(string1)
    string2 = sorted(string2)

    for index in range(len(string1)):
        if string1[index] != string2[index]:
            return False
    return True

def check_permutation_hash(string1, string2):
    # O(n) because the characters are tallied in each string.
    if len(string1) != len(string2):
        return False

    from collections import defaultdict
    string1_letter_count = defaultdict(int)

    for char in string1:
        string1_letter_count[char] += 1

    for char in string2:
        string1_letter_count[char] -= 1

    for char_count in list(string1_letter_count.values()):
        if char_count != 0:
            return False
    return True

import unittest
import random
import string
class Test(unittest.TestCase):
    number_of_partition_swaps = 10
    def permutation(self, a_string):
        # Create a permutation of a given string
        
        a_string_copy = '' # Used to ensure that the returned string is not the same as the given string.

        def swap(a_string):
            # Swap two letters in a string
            # string1 and string2 should be the same length.
            index_swap1, index_swap2 = random.sample(range(len(a_string) - 1), 2)
            greater_index = index_swap1 if index_swap1 > index_swap2 else index_swap2
            lower_index = index_swap1 if index_swap1 < index_swap2 else index_swap2
            return a_string[:lower_index] + a_string[greater_index] + a_string[lower_index + 1:greater_index] + a_string[lower_index] + a_string[greater_index + 1:]

        for _ in range(self.number_of_partition_swaps):
            a_string = swap(a_string)

        while a_string == a_string_copy:
            a_string = self.permutation(a_string)
        return a_string

    string_length = 10
    def create_permuted_strings(self):
        # Create two strings which are permutations of each other.
        a_string = ''.join(random.choices(string.ascii_letters, k=self.string_length))
        return a_string, self.permutation(a_string)

    def create_non_permuted_strings(self):
        # Create two strings that are not permutations of each other.
        # Add to one string a character which cannot be found in the other
        a_string = ''.join(random.choices(string.ascii_letters, k=self.string_length))
        random_index = random.randint(0, len(a_string) - 1)
        not_a_permutation = a_string[:random_index] + '!' + a_string[random_index + 1:]
        return a_string, not_a_permutation

    def check_permutation_test(self):
        functions = [check_permutation_sort, check_permutation_hash]
        for function in functions:
            string1, string2 = self.create_permuted_strings()
            self.assertTrue(function(string1, string2))
            string1, string2 = self.create_non_permuted_strings()
            self.assertFalse(function(string1, string2))

    number_of_tests = 1000
    def test(self):
        for _ in range(self.number_of_tests):
            self.check_permutation_test()
