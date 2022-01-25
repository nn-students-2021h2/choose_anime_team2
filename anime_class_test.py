import unittest
from anime_class import Anime


class MyTestCase(unittest.TestCase):
    """
    Tests for Anime class
    """

    def test_create_anime_ideal(self):
        """
        Create a class instance with the setting and the genre
        Test that setting is space, genre is fantasy
        """
        new_anime = Anime('space', 'fantasy')
        self.assertEqual(new_anime.setting, 'space')
        self.assertEqual(new_anime.genre, 'fantasy')

    def test_create_anime_incorrect_data_type(self):
        """
        Test that call of instantiation of class with
        not str values raises the type error
        """
        incorrect_settings = ['1', 0.11, print, {'setting': 'space'}, ['space']]
        incorrect_genres = ['1', 0.11, set, {'genre': 'fantasy'}, ['fantasy']]
        for element in incorrect_settings:
            self.assertRaises(TypeError, Anime.__init__, element, 'fantasy')
        for element in incorrect_genres:
            self.assertRaises(TypeError, Anime.__init__, 'space', element)


if __name__ == '__main__':
    unittest.main()
