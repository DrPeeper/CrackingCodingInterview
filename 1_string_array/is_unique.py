# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def is_unique_hash(string):
    # O(n) using a hash table with O(alphabet_size) space.
    dups = {}
    for char in string:
        if char in dups:
            return False
        dups[char] = None
    return True

def is_unique_barray(string):
    # Use a boolean array O(n).
    # Boolean array will fit lowercase letters which have an ordinal range of 97-122 (range of 26).
    barray = [0] * 26
    for char in string:
        # 'a' has ordinal value of 97, and every sequential character is one more than the previous.
        if barray[ord(char) - 97]:
            return False
        barray[ord(char) - 97] = 1
    return True

def is_unique_sort(string):
    # O(nlogn) because of the sorting.
    # This algorithm only requires extra space if the sorting algorithm does.
    string_list = sorted(string)
    for index in range(len(string_list) - 1):
        if string_list[index] == string_list[index + 1]:
            return False
    return True

def is_unique_var(string):
    # O(n^2) with O(1) space.
    for var_index in range(len(string)):
        for cmp_index in range(var_index + 1, len(string)):
            if string[var_index] == string[cmp_index]:
                return False
    return True

def is_unique_pythonic(string):
    # O(n^2) pythonic.
    for index in range(len(string)):
        if string[index] in string[index + 1:]:
            return False
    return True

import unittest
import string
import random
class Test(unittest.TestCase):
    string_length = 26

    def create_string_unique(self):
        # Function will not work if string_length is greater than 26.
        not_used = {}
        for char in string.ascii_lowercase:
            not_used[char] = None

        s = ''
        for _ in range(self.string_length):
            letter = random.choice(list(not_used.keys()))
            s = ''.join([s, letter])
            del not_used[letter]
        return s

    def create_non_unique_string(self):
        s = ''.join(random.choices(string.ascii_lowercase, k=self.string_length))
        index = random.randint(0, self.string_length - 1)
        dup_index = random.randint(0, self.string_length - 1)
        while index == dup_index:
            dup_index = random.randint(0, self.string_length - 1)
        return s[:index] + s[dup_index] + s[index + 1:]

    number_of_tests = 1000
    def test(self):
        self.assertFalse(self.string_length > 26)
        functions = [is_unique_hash, is_unique_barray, is_unique_sort, is_unique_var, is_unique_pythonic]
        
        for _ in range(self.number_of_tests):
            for function in functions:
                self.assertTrue(function(self.create_string_unique()))
                self.assertFalse(function(self.create_non_unique_string()))
