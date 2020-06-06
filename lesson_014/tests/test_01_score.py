import unittest
from bowling import Bowling


class MyBowlingTest(unittest.TestCase):

    def setUp(self):
        self.gaming_bowling = Bowling()

    def test_normal(self):
        self.gaming_bowling.get_scope('X71-9X7/45-3-65/')
        self.assertEqual(self.gaming_bowling.total_score, 105)

    def test_strike(self):
        self.gaming_bowling.get_scope('X')
        self.assertEqual(self.gaming_bowling.total_score, 20)

    def test_spare(self):
        self.gaming_bowling.get_scope('4/')
        self.assertEqual(self.gaming_bowling.total_score, 15)

    def test_count(self):
        self.gaming_bowling.get_scope('45')
        self.assertEqual(self.gaming_bowling.total_score, 9)

    def test_raise_second_shot_strike(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_scope('X7XXXXXXXX')

    def test_raise_first_shot_spare(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_scope('XXXXX/6XXXX')

    def test_raise_null_in_game_result(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_scope('XXXXXXX00XX')

    def test_raise_greater_than_10_frames(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_scope('XXXXXXXXXXX')


if __name__ == '__main__':
    unittest.main()
