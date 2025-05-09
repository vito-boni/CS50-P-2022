from CS50p.w2.twttr import shorten


def test_shorten():
    assert shorten ("Hello, World!") == "Hll, Wrld!"
    assert shorten ("I love my little apple!") == " lv my lttl ppl!"
    assert shorten ("123, 123 drink!") == "123, 123 drnk!"

"""
import unittest
from twttr import shorten

class TestShorten(unittest.TestCase):
    def test_shorten(self):
        self.assertEqual(shorten("Hello, World!"), "Hll, Wrld!")
        self.assertEqual(shorten("I love my little apple!"), " lv my lttl ppl!")
        self.assertEqual(shorten("123, 123 drink!"), "123, 123 drnk!")
        # the whole problem was me for not putting the capitalized letters and
        # numbers in this test… oh mon dieu, quelle chance.

if __name__ == "__main__":
    unittest.main()
"""
