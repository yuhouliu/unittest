# -*-coding: utf-8-*-
'''
实战功能：webui测试
'''

from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
# EC判断模块
from selenium.webdriver.support import expected_conditions as EC
#显性等待
from selenium.webdriver.support.wait import WebDriverWait


class TestShop(unittest.TestCase):

    def SetUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://39.98.138.157/shopxo/index.php?=/index/user/logininfo.html")

    def test1(self):
        self.driver.find_element(By.NAME, "accounts").send_keys("gaocab")  # 用户名
        self.driver.find_element(By.NAME, "pwd").send_keys("123456")   #密码
        self.driver.find_element(By.XPATH, '//*[text()="登录" and @type=submit"]').click()
        log_text = self.driver.find_element(By.XPATH, '//*[text()="登录成功"]').text
        WebDriverWait(self.driver, 5)
        print(log_text)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()