from unittest import TestCase
from app.database_model import DatabaseManager, DatabaseComponent

class TestDatabaseModel(TestCase):
    def setUp(self) -> None:
        self.bdm_obj = DatabaseManager()

    def test_init_fields(self):
        expected_message = "Database Components created"
        expected_start_state = False
        expected_db_type = type(DatabaseComponent)
        actual_message = self.bdm_obj.message
        actual_start_state = self.bdm_obj.started
        actual_db_type = type(self.bdm_obj.database)
        self.assertEqual(expected_message, actual_message)
        self.assertTrue(expected_start_state == actual_start_state)
        self.assertTrue(expected_db_type == actual_db_type)
