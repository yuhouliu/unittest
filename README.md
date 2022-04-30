# unittest
 unittest测试框架学习
unittest测试框架：
用于python项目中，可以用来创建测试套件，可以用于单元自动化测试(模块)、接口自动化测试(接口)、功能自动化测试(UI)等等。

一、unittest执行测试用例4种方法：

1、unittest.main()

2、加入容器中执行
    suite = unittest.TestSuite()
    suite.addTest(TestClass("test_method1"))
    suite.addTest(TestClass("test_method2"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

3、同时测试多个类
    suite = unittest.TestSuite()
    load = unittest.TestLoader()
    suite.addTest(load.loadTestsFromTestCase(TestClass1))
    suite.addTest(load.loadTestsFromTestCase(TestClass2))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

4、通过discover加载某路径下所有测试用例
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

通过HTMLTestRunner执行所有测试用例：
HTMLTestRunner.py文件下载位置：http://tungwaiyip.info/software/HTMLTestRunner.html(python2格式)
下载后放入python安装目录Lib目录下即可。
discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
testcases = discover
# file指的时html文件的绝对路径
runer = HTMLTestRunner.HTMLTestRunner(stream=file,
                                      title="自动化测试报告",
                                      description="测试用例执行详情")
runer.run(testcases)
