# -*-coding: utf-8-*-

# os管理操作系统目录
import os
import unittest
import HTMLTestRunner

print(os.getcwd())
case_path = os.path.join(os.getcwd(), "testcase")   # case用例目录
print(case_path)
report_path = os.path.join(os.getcwd(), "report")
print(report_path)

# 测试用例
def case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
    return discover


if __name__ == '__main__':
    # 生成html文件的路径
    report_abspath = os.path.join(report_path,"result.html")
    # 音频、视频、html文件属于二进制写入
    with open(report_abspath, 'wb') as file:
        runer = HTMLTestRunner.HTMLTestRunner(stream=file,
                                      title="自动化测试报告",
                                      description="测试用例执行详情")
        runer.run(case())
