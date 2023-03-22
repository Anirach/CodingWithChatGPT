import unittest
import string
import random
from password_generator import generate_password

class TestGeneratePassword(unittest.TestCase):

    def test_password_length(self):
        """
        Test that generated password has correct length
        """
        length = 12
        password = generate_password(length)
        self.assertEqual(len(password), length)

    def test_password_chars(self):
        """
        Test that generated password only contains allowed characters
        """
        length = 12
        chars = string.ascii_letters + string.digits + string.punctuation
        password = generate_password(length)
        for char in password:
            self.assertIn(char, chars)
    
if __name__ == '__main__':
    unittest.main()
