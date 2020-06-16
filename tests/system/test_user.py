from models.user import UserModel
from tests.base_test import BaseTest
import json  # convert dictionaries to json and send our API

# what we would like to test


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client: # we need a client to send request - post etc
            with self.app_context(): # save things to db
                response = client.post('/register', data={'username': 'test', 'password': '1234'})  # sent to API
                # resources/user.py

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message': 'User created successfully.'},
                                     json.loads(response.data)) # request is a dictionary which needs to convert to JSON

    def test_register_and_login(self):
        with self.app() as client: # we need a client to send request - post etc
            with self.app_context(): # save things to db
                client.post('/register', data={'username': 'test', 'password': '1234'})
                auth_response = client.post('/auth',
                                           data=json.dumps({'username': 'test', 'password': '1234'}),
                                           headers={'Content-Type': 'application/json'})

                self.assertIn('access_token', json.loads(auth_response.data).keys())  # auth request will return
                # response access token in a list. we will validate from the 'access_token' string appears in that
                # list should be true

    def test_register_duplicate_user(self):
        with self.app() as client:  # we need a client to send request - post etc
            with self.app_context():  # save things to db
                client.post('/register', data={'username': 'test', 'password': '1234'})
                response = client.post('/register', data={'username': 'test', 'password': '1234'})

                self.assertEqual(response.status_code, 400)  # resources/store.py file code for this
                self.assertDictEqual({'message': 'A user with that username already exists'},
                                     json.loads(response.data))
