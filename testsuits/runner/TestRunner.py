import testsuits
import unittest
from testsuits.ganzhou.ganzhou_login import GanzhouLogin
from testsuits.ganzhou.add_production_archives import AddProduction


suite = unittest.TestSuite()
suite.addTest(GanzhouLogin('test_login'))
suite.addTest(AddProduction('test_product_add'))
suite.addTest(AddProduction('test_liutong_add'))

# 执行类下所有用例
# suite1 = unittest.TestSuite(unittest.makeSuite(AddProduction))

# 执行包下所有用例
# suite = unittest.TestLoader().discover("testsuites")

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
