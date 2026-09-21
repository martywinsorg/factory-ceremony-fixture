import unittest

from slug import join_words


class ExistingTests(unittest.TestCase):
    def test_join_words(self):
        self.assertEqual(join_words(["one", "two"]), "one-two")
