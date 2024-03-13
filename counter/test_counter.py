"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter

class TestCounter(unittest.TestCase):

    def test_is_singleton(self):
        counter1 = Counter()
        counter2 = Counter()
        self.assertIs(counter1, counter2)

    def test_all_ref_share_same_count(self):
        counter1 = Counter()
        counter2 = Counter()
        counter1.increment()
        self.assertEqual(counter1.count, counter2.count)

if __name__ == '__main__':
    unittest.main()