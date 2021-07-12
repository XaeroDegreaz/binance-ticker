import unittest

from src.main import parse_symbols, get_streams_from_symbols


class MainTestCase(unittest.TestCase):
    def test_parse_symbols(self):
        self.assertEqual(parse_symbols('1, 1,2,A,    B'), {'1', '2', 'a', 'b'})

    def test_get_streams_from_symbols(self):
        self.assertEqual(get_streams_from_symbols({'1', '2', 'a', 'b'}), {'1@bookTicker', '2@bookTicker', 'a@bookTicker', 'b@bookTicker'})


# I don't know what's wrong, but I can't get this one to run. I have to run the above tests manually... I will figure it out later when I learn more about Py
if __name__ == '__main__':
    unittest.main()
