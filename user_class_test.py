import unittest
from user_class import User


class MyTestCase(unittest.TestCase):
    """
    Tests for User class
    """

    def test_create_user_ideal(self):
        """
        Create a class instance with the name and age of a user
        Test that sex is m, age is 16
        """
        new_user = User('m', 16)
        self.assertEqual(new_user.sex, 'm')
        self.assertEqual(new_user.age, 16)

    def test_create_user_incorrect_age_type(self):
        """
        Test that call of instantiation of class with
        not integer age raises the type error
        """
        incorrect_ages = ['11', 0.11, print, {'age': 11}, [11, 12, 13]]
        for element in incorrect_ages:
            self.assertRaises(TypeError, User.__init__, 'm', element)

    def test_create_user_incorrect_sex_value(self):
        """
        Test that call of instantiation of class with
        incorrect sex raises the value error
        """
        incorrect_sex = ['boy', 'girl', 1, 0, ['m', 'f']]
        for sex in incorrect_sex:
            self.assertRaises(TypeError, User.__init__, sex, 16)


if __name__ == '__main__':
    unittest.main()
