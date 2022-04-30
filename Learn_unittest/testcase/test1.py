# -*-coding: utf-8-*-

import unittest


class Test1(unittest.TestCase):
    # 默认运行规格： 1>A>a
    def test1(self):
        print(1)

    def testA(self):
        print("A")

    def testa(self):
        print("a")


if __name__ == '__main__':
    unittest.main()
