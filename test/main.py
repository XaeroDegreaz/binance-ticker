import unittest

from src.main import parse_symbols, get_streams_from_symbols


class MainTestCase(unittest.TestCase):
    def test_parse_symbols(self):
        self.assertEqual(parse_symbols('1, 1,2,A,    B'), {'1', '2', 'a', 'b'})

    def test_get_streams_from_symbols(self):
        self.assertEqual(get_streams_from_symbols({'1', '2', 'a', 'b'}), {'1@bookTicker', '2@bookTicker', 'a@bookTicker', 'b@bookTicker'})


if __name__ == '__main__':
    unittest.main()
