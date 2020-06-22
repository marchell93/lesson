import unittest
from bowling import Bowling, BowlingModify


class MyBowlingTest(unittest.TestCase):

    def setUp(self):
        self.gaming_bowling = Bowling()
        self.gaming_bowling_modify = BowlingModify()

    def test_normal(self):
        self.gaming_bowling.get_scope('X71-9X7/45-3-65/X')
        self.assertEqual(self.gaming_bowling.total_score, 125)

    def test_strike(self):
        self.gaming_bowling.get_scope('XXXXXXXXXX')
        self.assertEqual(self.gaming_bowling.total_score, 200)

    def test_spare(self):
        self.gaming_bowling.get_scope('4/4/4/4/4/4/4/4/4/4/')
        self.assertEqual(self.gaming_bowling.total_score, 150)

    def test_count(self):
        self.gaming_bowling.get_scope('45454545454545454545')
        self.assertEqual(self.gaming_bowling.total_score, 90)

    def test_raise_second_shot_strike(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_scope('X7XXXXXXXX')

    def test_raise_null_in_game_result(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_scope('XXXXXXX00XX')

    def test_raise_greater_than_10_frames(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_scope('XXXXXXXXXXX')

    def test_raise_first_shot_spare(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_scope('XXXXX/6XXXX')

    def test_raise_incorrect_char(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_scope('Xa/XXXXXXXXX')

    def test_raise_less_than_10_frames(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_scope('XXXXXXXX')

    def test_raise_greater_equally_10_points(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling.get_scope('XXXXXXXXX82')

    # -------------------Тесты для внешнего рынка-------------------

    def test_normal_modify(self):
        self.gaming_bowling_modify.get_scope('X71-9X7/45-3-65/X')
        self.assertEqual(self.gaming_bowling_modify.total_score, 117)

    def test_strike_modify(self):
        self.gaming_bowling_modify.get_scope('XXXXXXXXXX')
        self.assertEqual(self.gaming_bowling_modify.total_score, 270)

    def test_spare_modify(self):
        self.gaming_bowling_modify.get_scope('4/4/4/4/4/4/4/4/4/4/')
        self.assertEqual(self.gaming_bowling_modify.total_score, 136)

    def test_count_modify(self):
        self.gaming_bowling_modify.get_scope('45454545454545454545')
        self.assertEqual(self.gaming_bowling_modify.total_score, 90)

    def test_raise_second_shot_strike_modify(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling_modify.get_scope('X7XXXXXXXX')

    def test_raise_null_in_game_result_modify(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling_modify.get_scope('XXXXXXX00XX')

    def test_raise_greater_than_10_frames_modify(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling_modify.get_scope('XXXXXXXXXXX')

    def test_raise_first_shot_spare_modify(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling_modify.get_scope('XXXXX/6XXXX')

    def test_raise_incorrect_char_modify(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling_modify.get_scope('Xa/XXXXXXXXX')

    def test_raise_less_than_10_frames_modify(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling_modify.get_scope('XXXXXXXX')

    def test_raise_greater_equally_10_points_modify(self):
        with self.assertRaises(ValueError):
            self.gaming_bowling_modify.get_scope('XXXXXXXXX82')


if __name__ == '__main__':
    unittest.main()
