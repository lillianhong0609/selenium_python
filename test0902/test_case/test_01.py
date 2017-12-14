# coding:utf-8
from selenium import webdriver
import unittest
import time
class TestCase1(unittest.TestCase):
    '''测试百度查询'''
    # 用例有相同的前置条件
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Firefox()
        # 打开baidu页面
        url = 'https://www.baidu.com'
        self.driver.get(url)
    # 定义测试名称
    def test_01(self):
        u'''python+selenium教程'''
        # 鼠标移动到某个元素
        self.driver.find_element_by_id("kw").send_keys(u"python+selenium教程")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        # 打印测试结果
        t = self.driver.title
        print t
        # 判断测试结果与预期结果是是否一致 进行断言
        # 期望结果
        hope = u"python+selenium教程_百度搜索"
        self.assertEqual(t, hope)
        # 定义测试名称
    def test_02(self):
        u'''python+fiddler教程'''
        # 鼠标移动到某个元素
        self.driver.find_element_by_id("kw").send_keys(u"python+fiddler教程")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        # 打印测试结果
        t = self.driver.title
        print t
        # 判断测试结果与预期结果是是否一致 进行断言
        # 期望结果
        hope = u"教程_百度搜索"
        self.assertEqual(t, hope)
    # 后置操作
    def tearDown(self):
        self.driver.quit()

class TestCase2(unittest.TestCase):
    '''测试百度查询'''
        # 用例有相同的前置条件
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Firefox()
        # 打开baidu页面
        url = 'https://www.baidu.com'
        self.driver.get(url)
    # 定义测试名称
    def test_01(self):
        u'''python教程'''
        # 鼠标移动到某个元素
        self.driver.find_element_by_id("kw").send_keys(u"python教程")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        # 打印测试结果
        t = self.driver.title
        print t
        # 判断测试结果与预期结果是是否一致 进行断言
        # 期望结果
        hope = u"python教程_百度搜索"
        self.assertEqual(t, hope)
        # 定义测试名称
    def test_02(self):
        # 鼠标移动到某个元素
        u'''fiddler教程'''
        self.driver.find_element_by_id("kw").send_keys(u"fiddler教程")
        self.driver.find_element_by_id("su").click()
        time.sleep(5)
        # 打印测试结果
        t = self.driver.title
        print t
        # 判断测试结果与预期结果是是否一致 进行断言
        # 期望结果
        hope = u"fiddler教程_百度搜索"
        self.assertEqual(t, hope)
    # 后置操作
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    # 同时执行多个类
    unittest.main()
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
    # suite = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner(verbosity=2).run(suite)