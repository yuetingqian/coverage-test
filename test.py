from code import mymd5
import md5
import unittest
class md5Test(unittest.TestCase):
    def test_md5_obj(self):
        self.assertNotEqual(mymd5(), md5.new('123'))

    def test_md5_hexdigest(self):
        self.assertEqual(mymd5().hexdigest(), md5.new('123').hexdigest())

if __name__ == '__main__':
    unittest.main()
