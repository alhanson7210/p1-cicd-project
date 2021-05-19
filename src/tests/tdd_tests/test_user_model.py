from src.app.user_model import User
from unittest import TestCase

class TestUserModel(TestCase):
    def setUp(self) -> None:
        self.usr_obj = User()

    def test_set_user(self):
        self.usr_obj.set_user("guest")
        actual = self.usr_obj.curr_user
        expected = "guest"
        self.assertEqual(expected, actual)
