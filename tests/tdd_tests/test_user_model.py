from unittest import TestCase
from app.user_model import User


class TestUserModel(TestCase):
    def setUp(self) -> None:
        self.usr_obj = User()

    def test_set_user(self):
        actual = self.usr_obj.set_user("guest")
        expected = "guest"
        self.assertEqual(expected, actual)
