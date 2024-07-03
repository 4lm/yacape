import unittest

from entities.user import User

class TestUser(unittest.TestCase):
    def test_password_is_valid(self):
        user = User("testuser", "123")
        self.assertFalse(user.password_is_valid())

        user = User("testuser", "123456")
        self.assertTrue(user.password_is_valid())

if __name__ == '__main__':
    unittest.main()
