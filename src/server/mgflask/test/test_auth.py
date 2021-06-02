import unittest
import os
import sys
import requests


sys.path.insert(1, os.path.join(sys.path[0], '../..'))
from mgflask import app
from mgflask.db import Base, engine, db_session
from mgflask.models import User
from mgflask.auth import (
    test_users,
    get_user,
)

host = "http://127.0.0.1:5000"
endpoint = "/auth"
BASE_URL = host + endpoint
REGISTER_URL = BASE_URL + "/register"
LOGIN_URL = BASE_URL + "/login"


class AuthTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global client
        client = app.test_client()
        app.testing=True

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(bind=engine)
        if engine.url=="sqlite:///mgflask.db":  #avoid deleting production data
           Base.metadata.drop_all(bind=engine)

    def setUp(self):
        self.post_data1 = {
            "username": "Barry Allen",
            "password": "flash123"
        }
        self.post_data2 = {
            "username": "Clark Kent",
            "password": "Superman!2@#"
        }
        Base.metadata.create_all(bind=engine)
    
    def tearDown(self):
        Base.metadata.drop_all(bind=engine)
    
    def test_register_user(self):
        """
        Tests registering a user and upon 
        retrieval should have the same username
        """
        x = client.post(REGISTER_URL, json=self.post_data1)

        user_expected = db_session.query(User).filter_by(username=self.post_data1["username"]).first()
        self.assertEqual(x.status_code, 201)
        self.assertIsNotNone(user_expected)
        self.assertEqual("Barry Allen", user_expected.username)
        
    def test_register_already_registered_user(self):
        """
        Tests registering a user that is already registered
        """
        register_1 = client.post(REGISTER_URL, json = self.post_data2)
        user_expected = db_session.query(User).filter_by(username=self.post_data2["username"]).first()

        self.assertEqual(register_1.status_code, 201)
        self.assertIsNotNone(user_expected)
        register_2 = client.post(REGISTER_URL, json = self.post_data2)
        self.assertEqual(register_2.status_code, 401)
        self.assertEqual(register_2.get_json()["msg"],
                            "User already registered")
    
    def test_register_no_username(self):
        """
        Tests registering a user with 
        improper parameter of no username
        """
        corrupt_data = {"username": "", "password": "passwoor123"}
        corrupt_post = client.post(REGISTER_URL, json = corrupt_data)
        self.assertEqual(corrupt_post.status_code, 401)
        self.assertEqual(corrupt_post.get_json()["msg"], "Username is required")

    def test_register_no_password(self):
        """
        Tests registering a user with the improper parameters 
        of an empy password
        """
        corrupt_data = {"username": "noPassword", "password": ""}
        corrupt_post = client.post(REGISTER_URL, json = corrupt_data)
        self.assertEqual(corrupt_post.status_code, 401)
        self.assertEqual(corrupt_post.get_json()["msg"], "Password is required.")
    
    def test_login_no_user(self):
        """
        Tests login input on user not in the database
        """
        post_data = client.post(LOGIN_URL, json=self.post_data1)
        self.assertEqual(post_data.status_code, 401)
        self.assertEqual(post_data.get_json()["msg"], "Incorrect username.")

    def test_login_valid(self):
        "Tests valid login user if user is registered"
        register_1 = client.post(REGISTER_URL, json = self.post_data1)
        self.assertEqual(register_1.status_code, 201)
    
        post_data = client.post(LOGIN_URL, json=self.post_data1)
        self.assertEqual(post_data.status_code, 201)
        self.assertEqual(post_data.get_json()["msg"], "Login Successful")

    def test_user_not_registered(self):
        "Tests valid login user if other user is registered"
        register_1 = client.post(REGISTER_URL, json = self.post_data1)
        self.assertEqual(register_1.status_code, 201)

        post_data = client.post(LOGIN_URL, json=self.post_data2)
        self.assertEqual(post_data.status_code, 401)
        self.assertEqual(post_data.get_json()["msg"], "Incorrect username.")

    def test_wrong_password(self):
        "Tests valid login user if user is registered"
        register_1 = client.post(REGISTER_URL, json = self.post_data1)
        self.assertEqual(register_1.status_code, 201)

        self.post_data1["password"] = "not_barry214"

        post_data = client.post(LOGIN_URL, json=self.post_data1)
        self.assertEqual(post_data.status_code, 401)
        self.assertEqual(post_data.get_json()["msg"], "Incorrect password.")

    
        
if __name__ == '__main__':
    unittest.main()

os.remove("./mgflask.db")
