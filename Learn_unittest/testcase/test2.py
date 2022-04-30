# -*-coding: utf-8-*-

import unittest


class Test2(unittest.TestCase):
    # 默认运行规格： 1>A>a
    def test11(self):
        print(11)

    def testAA(self):
        print("AA")

    def testaa(self):
        print("aa")


if __name__ == '__main__':
    # 第一步，创建一个套件对象
    suite = unittest.TestSuite()
    # 第二步，添加用例
    suite.addTest(Test2("testaa"))
    suite.addTest(Test2("testAA"))
    suite.addTest(Test2("test11"))
    # 第三步，用例运行器
    runner = unittest.TextTestRunner()

    runner.run(suite)  # 将套件放入运行器
