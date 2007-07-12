import unittest
from ctypes import *

class BytesTest(unittest.TestCase):
    def test_c_char(self):
        x = c_char(b"x")
        x.value = b"y"
        c_char.from_param(b"x")
        (c_char * 3)(b"a", b"b", b"c")

    def test_c_wchar(self):
        x = c_wchar(b"x")
        x.value = b"y"
        c_wchar.from_param(b"x")
        (c_wchar * 3)(b"a", b"b", b"c")

if __name__ == '__main__':
    unittest.main()
