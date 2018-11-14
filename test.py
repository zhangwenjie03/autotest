# coding:utf-8

'''
Created on2018-11-14
@auther: zhang.wenjie
project：使用unittest框架编写测试用例思路
'''

import unittest

class Test(unittest.TestCase):
    print 'abc'
    def setUp(self):
        self.number = int(raw_input('enter a number:'))

    def test_case1(self):
        print self.number
        self.assertEqual(self.number,10,msg='your input is not 10')

    def test_case2(self):
        print self.number
        self.assertEqual(self.number,20,msg='your input is not 20')

    @unittest.skip('暂时跳过用例3的测试')
    def test_case3(self):
        print self.number
        self.assertEqual(self.number,30,msg='your input is not 30')

    def tearDown(self):
        print 'Test over'

# suite = unittest.TestSuite()
# discover = unittest.defaultTestLoader.discover(r'C:\Python27\my_python',pattern='test.py')
# suite.run(discover)

if __name__ == '__main__':
    unittest.main()
