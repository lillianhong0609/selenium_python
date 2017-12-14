# coding:utf-8
# ###下面三行代码python2报告出现乱码时候可以加上####
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')
import unittest
from common import HTMLTestRunner
import os
# 用例的地址
case_path = os.path.join(os.getcwd(), "test_case")
print case_path
# 加载所有的用例
discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern="test_*.py", top_level_dir=None)
# print discover

# 执行所有用例,生成txt文本报告
# runner = unittest.TextTestRunner()
# runner.run(discover)

# 时间戳 获取电脑时间 不建议添加
# now_time = time.strftime('%Y_%m_%d %H_%M_%S')
# 指定报告存放路径
report_path = os.path.join(os.getcwd(), "report\\report.html")
print  report_path
# 打开路径,写入
op = open(report_path,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=op, title=u'测试报告', description=u'用例执行情况')
# 生成报告
runner.run(discover)
op.close()