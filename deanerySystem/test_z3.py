import sys
import unittest
from day_z3 import Day
from term_z3 import Term


class Test_TestDeanerySystem(unittest.TestCase):
    def test_earlierThan(self):
        self.assertFalse(Term(Day.TUE, 10, 15).earlierThan(Term(Day.MON, 10, 00)))
        self.assertFalse(Term(Day.MON, 10, 15).earlierThan(Term(Day.MON, 10, 14)))
        self.assertFalse(Term(Day.MON, 11, 15).earlierThan(Term(Day.MON, 10, 18)))
        self.assertTrue(Term(Day.MON, 11, 15).earlierThan(Term(Day.MON, 11, 18)))

    def test_laterThan(self):
        self.assertTrue(Term(Day.TUE, 10, 15).laterThan(Term(Day.MON, 10, 00)))
        self.assertTrue(Term(Day.MON, 10, 15).laterThan(Term(Day.MON, 10, 14)))
        self.assertTrue(Term(Day.MON, 11, 15).laterThan(Term(Day.MON, 10, 18)))
        self.assertFalse(Term(Day.MON, 11, 15).laterThan(Term(Day.MON, 11, 18)))

    def test_term_equals(self):
        self.assertTrue(Term(Day.MON, 7, 00).equals(Term(Day.MON, 7, 00)))
        self.assertFalse(Term(Day.WED, 10, 15).equals(Term(Day.WED, 10, 18)))
        self.assertFalse(Term(Day.WED, 10, 15).equals(Term(Day.WED, 11, 15)))
        self.assertFalse(Term(Day.WED, 10, 15).equals(Term(Day.MON, 10, 15)))
        self.assertFalse(Term(Day.WED, 10, 15).equals(Term(Day.MON, 10, 17)))

    def test_term_str(self):
        self.assertEqual(str(Term(Day.MON, 7, 8)), "Poniedziałek 7:08-8:38 [90]")


if __name__ == '__main__':
    unittest.main()
