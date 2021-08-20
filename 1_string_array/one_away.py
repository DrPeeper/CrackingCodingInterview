# One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

def one_away(str1, str2):
    if len(str1) > len(str2):
        longer = str1
        shorter = str2
    elif len(str1) < len(str2):
        longer = str2
        shorter = str1
    else:
        edit_count = 0
        for index in range(len(str1)):
            if str1[index] != str2[index]:
                edit_count += 1
        return edit_count <= 1

    edit_count = 0
    longer_length = len(longer)
    shorter_length = len(shorter)
    longer_count = 0
    shorter_count = 0

    while longer_count < longer_length and shorter_count < shorter_length:
        if longer[longer_count] == shorter[shorter_count]:
            shorter_count += 1
            longer_count += 1
        else:
            longer_count += 1
            edit_count += 1

    if longer_count != longer_length:
        edit_count += longer_length - longer_count
    else:
        edit_count += shorter_length - shorter_count
    return edit_count <= 1

import unittest
import random
import string
class Test(unittest.TestCase):
    def add(self, test_str):
        index = random.randint(0, len(test_str) - 1)
        letter = random.choice(string.ascii_lowercase + string.ascii_uppercase)
        test_str = test_str[:index] + letter + test_str[index:]
        return test_str

    def subtract(self, test_str):
        if not test_str:
            return ''
        index = random.randint(0, len(test_str) - 1)
        test_str = test_str[:index] + test_str[index + 1:]
        return test_str

    def replace(self, test_str, edits):
        edited = []
        edits = len(test_str) if len(test_str) < edits else edits
        for _ in range(edits):
            index = random.randint(0, len(test_str) - 1)
            while index in edited:
                index = random.randint(0, len(test_str) - 1)
            edited.append(index)
            letter = random.choice(string.ascii_lowercase + string.ascii_uppercase)
            while letter == test_str[index]:
                letter = random.choice(string.ascii_lowercase + string.ascii_uppercase)
            test_str = test_str[:index] + letter + test_str[index + 1:]
        return test_str

    max_string_length = 10
    num_tests = 100
    max_edits = 10
    def one_away_test(self):
        test_str = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=random.randint(2, self.max_string_length)))

        self.assertTrue(one_away(test_str, test_str))
        self.assertTrue(one_away(test_str, self.add(test_str)))
        self.assertTrue(one_away(test_str, self.subtract(test_str)))
        self.assertTrue(one_away(test_str, self.replace(test_str, 1)))

        test_str2 = test_str + ''
        edits = random.randint(2, self.max_edits)
        for _ in range(edits):
            test_str2 = self.add(test_str2)
        self.assertFalse(one_away(test_str, test_str2))
        
        test_str2 = test_str + ''
        test_str2 = self.replace(test_str2, edits)
        self.assertFalse(one_away(test_str, test_str2))

        test_str2 = test_str + ''
        for _ in range(edits):
            test_str2 = self.subtract(test_str2)
        self.assertFalse(one_away(test_str, test_str2))

    def test(self):
        for _ in range(self.num_tests):
            self.one_away_test()
