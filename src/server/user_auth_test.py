import unittest
import requests
from mgflask.db import Base, engine, db_session
from mgflask.models import User
from mgflask.auth import (
    test_users,
    get_user,
)

print('Created the test database structure')

host = "http://127.0.0.1:5000"
endpoint = "auth"
BASE_URL = host + "/"+endpoint
REGISTER_URL = BASE_URL + "/register"
LOGIN_URL = BASE_URL + "/login"



class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(bind=engine)
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
        Tests registering a user and upon 
        retrieval should have the same username
        """
        x = requests.post(REGISTER_URL, json = self.post_data1)
        user_expected = db_session.query(User).filter_by(username=self.post_data1["username"]).first()

        self.assertEqual(x.status_code, 201)
        self.assertIsNotNone(user_expected)
        self.assertEqual("Barry Allen", user_expected.username)
        
    def testRegisterSameUser(self):
        """
        Tests registering a user that is already registered
        """
        register_1 = requests.post(REGISTER_URL, json = self.post_data2)
        user_expected = db_session.query(User).filter_by(username=self.post_data2["username"]).first()

        self.assertEqual(register_1.status_code, 201)
        self.assertIsNotNone(user_expected)
        register_2 = requests.post(REGISTER_URL, json = self.post_data2)
        self.assertEqual(register_2.status_code, 401)
        self.assertEqual(register_2.json()["msg"],
                            "User already registered")
    
    def testRegisterNoUsername(self):
        """
        Tests registering a user with 
        improper parameter of no username
        """
        corrupt_data = {"username": "", "password": "passwoor123"}
        corrupt_post = requests.post(REGISTER_URL, json = corrupt_data)
        self.assertEqual(corrupt_post.status_code, 401)
        self.assertEqual(corrupt_post.json()["msg"], "Username is required")

    def testRegisterNoPassword(self):
        """
        Tests registering a user with the improper parameters 
        of an empy password
        """
        corrupt_data = {"username": "noPassword", "password": ""}
        corrupt_post = requests.post(REGISTER_URL, json = corrupt_data)
        self.assertEqual(corrupt_post.status_code, 401)
        self.assertEqual(corrupt_post.json()["msg"], "Password is required.")
    
    def testNoUserLogin(self):
        post_data = requests.post(LOGIN_URL, json=self.post_data1)
        self.assertEqual(post_data.status_code, 401)
        self.assertEqual(post_data.json()["msg"], "Incorrect username.")



if __name__ == '__main__':
    unittest.main()

