from code import mymd5
import md5
import unittest
class md5Test(unittest.TestCase):
    def test_md5(self):
        self.assertEqual(mymd5(), md5.new('1234'))

if __name__ == '__main__':
    unittest.main()
