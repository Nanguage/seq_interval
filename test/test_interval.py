import unittest
import sys

sys.path.insert(0, "../")
from seq_interval import Interval

class IntervalTestCase(unittest.TestCase):

    def setUp(self):
        """
        iv1 |---------->
            1          10

        iv2      |----------->
                 5           15

        iv3   |----->
              3     8

        iv4             |------------->
                        11            20
        """
        self.iv1 = Interval(1, 10)
        self.iv2 = Interval(5, 15)
        self.iv1_r = Interval(10, 1)
        self.iv2_r = Interval(15, 5)
        self.iv3 = Interval(3, 8)
        self.iv4 = Interval(11, 20)

    def tearDown(self):
        for i in dir(self):
            if i.startswith('iv'):
                delattr(self, i)

    def test_len_method(self):
        self.assertEqual(len(self.iv1), 10)
        self.assertEqual(len(self.iv1_r), 10)
        self.assertEqual(len(self.iv3), 6)

    def test_eq_ne_operator(self):
        self.assertTrue(self.iv1 == Interval(1, 10))
        self.assertFalse(self.iv1 != Interval(1, 10))
        self.assertTrue(self.iv1 != self.iv2)
        self.assertFalse(self.iv1 == self.iv2)
        self.assertTrue(self.iv1 != self.iv1_r)
        self.assertFalse(self.iv1 == self.iv1_r)

    def test_gt_lt_operator(self):
        self.assertFalse(self.iv2 > self.iv1)
        self.assertFalse(self.iv1 < self.iv2)
        self.assertTrue(self.iv1 < self.iv4)
        self.assertTrue(self.iv1_r < self.iv4)
        self.assertTrue(self.iv4 > self.iv1_r)
        self.assertTrue(self.iv4 > self.iv1_r)
        self.assertTrue(self.iv4 > self.iv3)

    def test_ge_le_operator(self):
        self.assertTrue(self.iv2 >= self.iv1)
        self.assertTrue(self.iv1 <= self.iv2)
        self.assertTrue(self.iv1 <= self.iv4)
        self.assertTrue(self.iv4 >= self.iv1_r)

    def test_add_operator(self):
        self.assertEqual(self.iv1 + self.iv2, Interval(1, 15)) 
        self.assertEqual(self.iv1_r + self.iv2_r, Interval(15, 1))
        with self.assertRaises(ValueError):
            self.iv1 + self.iv2_r
        with self.assertRaises(ValueError):
            self.iv3 + self.iv4

    def test_sub_operator(self):
        with self.assertRaises(ValueError):
            self.iv1 - self.iv2_r
        with self.assertRaises(ValueError):
            self.iv3 - self.iv4
        with self.assertRaises(ValueError):
            self.iv1 - self.iv3
        self.assertEqual(self.iv1 - self.iv2, Interval(1, 4)) 
        self.assertEqual(self.iv2 - self.iv1, Interval(11, 15)) 
        self.assertEqual(self.iv1_r - self.iv2_r, Interval(4, 1))
        self.assertEqual(self.iv2_r - self.iv1_r, Interval(15, 11))
        self.assertEqual(self.iv1 - Interval(1, 5), Interval(6, 10))
        self.assertEqual(self.iv1 - Interval(6, 10), Interval(1, 5))

    def test_contain_operator(self):
        with self.assertRaises(TypeError):
            "test" in self.iv1
        self.assertTrue(self.iv3 in self.iv1)
        self.assertTrue(Interval(1, 1) in self.iv1)
        self.assertTrue(Interval(10, 10) in self.iv1)
        self.assertTrue(5 in self.iv1)
        self.assertTrue(5.0 in self.iv1)
        self.assertFalse(self.iv4 in self.iv1)
        self.assertFalse(12 in self.iv1)
        self.assertFalse(12.0 in self.iv1)

    def test_reverse_method(self):
        iv1_cp = self.iv1.copy()
        self.iv1.reverse()
        self.assertEqual(self.iv1, self.iv1_r)
        self.iv2.reverse()
        self.assertEqual(self.iv2, self.iv2_r)
        self.assertNotEqual(self.iv1, iv1_cp)

    def test_is_intersect_with_method(self):
        self.assertTrue(self.iv1.is_intersect_with(self.iv2))
        self.assertTrue(self.iv2.is_intersect_with(self.iv1))
        self.assertTrue(self.iv1.is_intersect_with(self.iv1))
        self.assertTrue(self.iv1.is_intersect_with(self.iv1_r))
        self.assertFalse(self.iv3.is_intersect_with(self.iv4))

    def test_is_adjacent_with_method(self):
        self.assertTrue(self.iv1.is_adjacent_with(self.iv4))
        self.assertTrue(self.iv1_r.is_adjacent_with(self.iv4))
        self.assertTrue(self.iv4.is_adjacent_with(self.iv1))
        self.assertTrue(self.iv4.is_adjacent_with(self.iv1_r))
        self.assertFalse(self.iv1.is_adjacent_with(self.iv2))
        self.assertFalse(self.iv1_r.is_adjacent_with(self.iv2))
        self.assertFalse(self.iv3.is_adjacent_with(self.iv4))

if __name__ == "__main__":
    unittest.main()
