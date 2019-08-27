#coding=utf-8
import unittest
import os
class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path = os.path.join(os.getcwd(),'case')
        #匹配查找测试用例文件（unittest_*.py），并将查找到的测试用例组装到测试套件
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()