from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'abcd')

            self.assertIsNone(UserModel.find_by_username('test'))  #checks DB to make sure the username not visible
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()  #saves to DB

            self.assertIsNotNone(UserModel.find_by_username('test'))  #checks DB to make sure username is visible
            self.assertIsNotNone(UserModel.find_by_id(1))
