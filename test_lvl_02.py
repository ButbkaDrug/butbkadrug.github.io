import unittest
import os
from lvl_01 import main

class testLevel(unittest.TestCase):
    def test_book_content(self):
        path = os.path.join('castle', 'second_floor', 'library')
        list_of_titles = os.listdir(path)
        list_of_titles.sort(key = lambda x: len(x))
        title = list_of_titles.pop()
        path_to_file = os.path.join(path, title)
        with open(path_to_file) as file:
            results = file.read()

        self.assertEqual(
                main(),
                results,
                'Результаты не совпадают. Что-то пошло не так с чтением')

if __name__ == '__main__':
    unittest.main()
