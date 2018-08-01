import HTMLTestRunner
import os
import unittest
import time
from testsuits.ganzhou.ganzhou_login import GanzhouLogin
from testsuits.ganzhou.add_production_archives import AddProduction

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('..')) + '/testreport/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

# 构建suite
suite = unittest.TestSuite()
suite.addTest(GanzhouLogin('test_login'))
suite.addTest(AddProduction('test_product_add'))
suite.addTest(AddProduction('test_liutong_add'))

if __name__ =='__main__':

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)

