import unittest

from foo.bar import bar


class TestBar(unittest.TestCase):
    def test_bar(self):
        self.assertEqual(bar(), "bar")