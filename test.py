import unittest
import requests
class seleniumTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.s=requests.session()
        self.url='http://127.0.0.1:5000/get_baidu'

    def test_geturl(self):#单元测试方法
        resp=self.s.get(url=self.url)
        secs=resp.content
        take_time=resp.elapsed.microseconds/1000000
        self.assertTrue(take_time<1, msg='请求时间超过1s')#断言时间是否超过1s
        self.assertIs(secs,'//www.baidu.com/mg/bd_logo1.png','图片地址不一致')#断言返回是否一致

    @classmethod
    def tearDownClass(self):
        pass

if __name__ == '__main__':
    unittest.main()