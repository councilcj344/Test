import unittest
from mineflayer_bot import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.log_message = "Test log message"
        self.error_message = "Test error message"

    def test_log(self):
        result = utils.log(self.log_message)
        self.assertEqual(result, f"LOG: {self.log_message}")

    def test_handle_error(self):
        result = utils.handle_error(self.error_message)
        self.assertEqual(result, f"ERROR: {self.error_message}")

if __name__ == '__main__':
    unittest.main()