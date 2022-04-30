# -*-coding: utf-8-*-

import unittest

class Test_XH(unittest.TestCase):

    def test1(self):
        print(1)

    def test2(self):
        print(2)

    def test3(self):
        print(3)


class Test_WY(unittest.TestCase):

    def test4(self):
        """这是测试用例4"""
        print(4)

    def test5(self):
        """这是测试用例5"""
        print(5)

    def test6(self):
        """这是测试用例6"""
        print(6)


if __name__ == '__main__':
    # 创建套件
    suite = unittest.TestSuite()
    # 创建load对象，用于加载指定的类(与test2的不同点)
    load = unittest.TestLoader()
    suite.addTest(load.loadTestsFromTestCase(Test_WY))

    runer = unittest.TextTestRunner()
    runer.run(suite)