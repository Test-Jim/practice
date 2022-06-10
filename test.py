import unittest
import requests
class seleniumTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.s=requests.session()
        self.url='http://127.0.0.1:5000/get_baidu'

    def test_geturl(self):
        resp=self.s.get(url=self.url)
        secs=resp.content
        take_time=resp.elapsed.microseconds/1000000
        self.assertTrue(take_time<1, msg='请求时间超过1s')
        self.assertIs(secs,'//www.baidu.com/mg/bd_logo1.png','imageUrl error')

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()