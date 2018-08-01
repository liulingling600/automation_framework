import unittest
from framework.browser_engine import BrowerEngine
from pageobjects.ganzhou.home_page import HomePage
from testsuits.ganzhou.ganzhou_login import GanzhouLogin
import time

class AddProduction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        brower = BrowerEngine(cls)
        cls.driver = brower.open_browser(cls)
        GanzhouLogin.test_login(cls)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_product_add_1(self):
        homePage = HomePage(self.driver)
        time.sleep(2)
        homePage.click_btn(homePage.business_archives_manage)
        time.sleep(1)
        homePage.click_btn(homePage.producte_archives_manage)
        time.sleep(1)
        homePage.change_frame(homePage.iframe_production)
        time.sleep(2)
        homePage.click_btn(homePage.add)

    def test_liutong_add_2(self):
        homePage = HomePage(self.driver)
        time.sleep(2)
        homePage.click_btn(homePage.business_archives_manage)
        time.sleep(1)
        homePage.click_btn(homePage.liutong_archives_manage)
        time.sleep(1)
        homePage.change_frame(homePage.iframe_liutong)
        time.sleep(2)
        homePage.click_btn(homePage.add)

if __name__ == '__main__':
    unittest.main()