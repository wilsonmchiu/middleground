import unittest
from flask import current_app
from mgflask.db import Base
from mgflask.models import User
from mgflask.auth import register,login
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

test_engine = create_engine('sqlite:///test.db')
test_db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=test_engine))

Base.query = test_db_session.query_property()
Base.metadata.create_all(bind=test_engine)

print('Created the test database structure')

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.post_data1 = {
            "username": "Barry Allen",
            "password": "flash123"
        }
        self.post_data2 = {
            "username": "Clark Kent",
            "password": "Superman!2@#"
        }

    def testRegisterEmptyDB(self):
        """
        Tests registering a user and upon retrieval should have the same username
        """
        return


    def testRegisterSameUserDB(self):
        """
        Tests that a user register on a username that already exists 
        properly throws an error
        """
        return
        






if __name__ == '__main__':
    unittest.main()

