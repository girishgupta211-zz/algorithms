import unittest
from collections import Counter


# Write a function that accepts a word (string) and a list of words (list or tuple of strings) and return
# back a list with the valid anagrams for the word inside the given words list.

def is_anagram(string1, string2):
    return Counter(string1) == Counter(string2)
    # builtin function Counter is better than sorted as it will reduce complexity to O(n)
    # return sorted(string1) == sorted(string2)


def get_anagrams(word, words_list):
    # Remove spaces and convert to lower case
    try:
        l_word = word.replace(' ', '').lower()
        return [each for each in words_list if is_anagram(each.replace(' ', '').lower(), l_word)]
    except AttributeError as ex:
        return "input data format is wrong"


class TestAnagrams(unittest.TestCase):
    def test_positive_with_tuple(self):
        self.assertEqual(get_anagrams('abc', ('abc', 'cb a', 'ba')), ['abc', 'cb a'])

    def test_positive_with_list(self):
        self.assertEqual(get_anagrams('parties', ['pastier', 'pirates', 'traipse', 'piratis']),
                         ['pastier', 'pirates', 'traipse'])

    def test_positive_with_space(self):
        self.assertEqual(get_anagrams('Edward Gorey', ['Ogdred Weary', 'Regera Dowdy', 'E G Deadworry']),
                         ['Ogdred Weary', 'Regera Dowdy', 'E G Deadworry'])

    def test_negative(self):
        self.assertNotEqual(get_anagrams('abc', ['abc', 'cba', 'ba']), ['ba'])

    def test_exception(self):
        self.assertRaises(TypeError, get_anagrams(1, [1, 2, 3]), [1])


if __name__ == '__main__':
    unittest.main()
