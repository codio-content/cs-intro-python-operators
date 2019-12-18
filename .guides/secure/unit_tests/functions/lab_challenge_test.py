import unittest
import lab_challenge

class Test_to_upper(unittest.TestCase):
    def test_to_upper(self):
        """Test student work"""
        self.assertEqual(to_upper("student work"), "STUDENT WORK")
        self.assertEqual(to_upper("Calvin and Hobbes"), "CALVIN AND HOBBES")
        self.assertEqual(to_upper("TEXAS RANGERS"), "TEXAS RANGERS")