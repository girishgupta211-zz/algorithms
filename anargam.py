import unittest


# Write a function that accepts a word (string) and a list of words (list or tuple of strings) and return
# back a list with the valid anagrams for the word inside the given words list.
def get_anagrams(word, word_list):
    li = []
    word = sorted(word)
    for ana in word_list:
        if word == sorted(ana):
            li.append(ana)
    return li


class TestAnagrams(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(get_anagrams('abc', ['abc', 'cba', 'ba']), ['abc', 'cba'])

    def test_negative(self):
        self.assertNotEqual(get_anagrams('abc', ['abc', 'cba', 'ba']), ['ba'])


if __name__ == '__main__':
    unittest.main()
