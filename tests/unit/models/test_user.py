from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user=UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test', 'This is not the correct username')
        self.assertEqual(user.password, 'abcd', 'This password is incorrect, please try again')
