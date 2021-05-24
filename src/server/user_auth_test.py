import unittest

from mgflask.models import User
from mgflask.db import db_session


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.user_1 = User(username="Barry Allen", password="password123")
        self.user_2 = User("Clark Kent ", "Superman!@#")

    def test_register(self):
        test_user = User(username="John Doe",
                         password="test123")
        db_session.add(test_user)
        db_session.commit()
        same_user = User.query.filter_by(username="John Doe").first()
        self.assertEqual(test_user.username, same_user.username)




if __name__ == '__main__':
    unittest.main()

