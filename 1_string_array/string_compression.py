# String Compression: Implement a method to perform basic string compression using the counts of repeated characters.

def compress_loop(string):
    if len(string) == 1:
        return string + '1'
    index = 1
    letter_count = 1
    current_letter = string[0]
    while index < len(string):
        if current_letter == string[index]:
            letter_count += 1
            index += 1
        else:
            current_letter = string[index]
            string = string[:index] + str(letter_count) + string[index:]
            index += len(str(letter_count)) + 1
            letter_count = 1
    return string + str(letter_count)


import unittest
class Test(unittest.TestCase):
    letter_count = 10
    max_duplicates = 10
    num_tests = 1000

    def create_final_string(self):
        import string
        import random
        test_string = ''
        test_string_final = ''
        past_letter = ''
        for _ in range(self.letter_count):
            duplicates = random.randint(1, self.max_duplicates)
            next_letter = random.choice(string.ascii_uppercase + string.ascii_lowercase)
            while next_letter == past_letter:
                next_letter = random.choice(string.ascii_uppercase + string.ascii_lowercase)
            past_letter = next_letter
            sub_string_list = [next_letter] * duplicates
            test_string = test_string + ''.join(sub_string_list)
            test_string_final = test_string_final + ''.join(sub_string_list + [str(duplicates)])
        return (test_string, test_string_final)

    def compress_test(self):
        test_info = self.create_final_string()
        self.assertEqual(compress_loop(test_info[0]), test_info[1])

    def test(self):
        for test_num in range(self.num_tests):
            self.compress_test()
