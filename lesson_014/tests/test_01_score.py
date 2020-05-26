import unittest
from bowling import Bowling, StateBowling


class MyBowlingTestCase(unittest.TestCase):

    def test_normal(self):
        state = StateBowling()
        gaming_bowling = Bowling(state)
        gaming_bowling.get_scope('X4/71X4--6415/X11')
        self.assertEqual(state.result, 115)

    def test_strike(self):
        state = StateBowling()
        gaming_bowling = Bowling(state)
        gaming_bowling.get_scope('X')
        self.assertEqual(state.result, 20)

    def test_spare(self):
        state = StateBowling()
        gaming_bowling = Bowling(state)
        gaming_bowling.get_scope('4/')
        self.assertEqual(state.result, 15)

    def test_count(self):
        state = StateBowling()
        gaming_bowling = Bowling(state)
        gaming_bowling.get_scope('41')
        self.assertEqual(state.result, 5)


if __name__ == '__main__':
    unittest.main()
